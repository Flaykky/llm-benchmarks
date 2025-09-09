#!/usr/bin/env python3
"""
Tester for shortest path algorithms with memory and time constraints.
Usage: python tester.py executable1 [executable2 ...] [--generate]
"""

import sys
import os
import subprocess
import time
import random
import heapq
from typing import List, Tuple, Dict, Optional
import tempfile
import psutil
import threading
from collections import defaultdict

class MemoryMonitor:
    def __init__(self):
        self.peak_memory = 0
        self.monitoring = False
        self.process = None
    
    def start_monitoring(self, process):
        self.process = process
        self.monitoring = True
        self.peak_memory = 0
        thread = threading.Thread(target=self._monitor)
        thread.daemon = True
        thread.start()
    
    def _monitor(self):
        try:
            p = psutil.Process(self.process.pid)
            while self.monitoring and self.process.poll() is None:
                try:
                    # Get memory info for process and all children
                    memory_info = p.memory_info()
                    current_memory = memory_info.rss / 1024 / 1024  # MB
                    
                    # Include children memory
                    for child in p.children(recursive=True):
                        try:
                            child_memory = child.memory_info()
                            current_memory += child_memory.rss / 1024 / 1024
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
                    
                    self.peak_memory = max(self.peak_memory, current_memory)
                    time.sleep(0.01)  # Check every 10ms
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    break
        except Exception:
            pass
    
    def stop_monitoring(self):
        self.monitoring = False
        return self.peak_memory

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.edges = []  # List of (u, v, weight)
        self.adj = defaultdict(list)  # Adjacency list for reference solution
    
    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))
        self.adj[u].append((v, weight))
    
    def dijkstra_reference(self, source: int) -> List[int]:
        """Reference Dijkstra implementation for correctness checking"""
        dist = [float('inf')] * self.n
        dist[source] = 0
        pq = [(0, source)]
        visited = set()
        
        while pq:
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            
            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        # Convert inf to -1 for consistency with expected output
        return [d if d != float('inf') else -1 for d in dist]

def generate_random_graph(n: int, m: int, max_weight: int = 1000) -> Graph:
    """Generate a random weighted directed graph"""
    graph = Graph(n)
    edges_set = set()
    
    # Ensure some connectivity by adding a path
    for i in range(min(n-1, m//4)):
        u, v = i, i + 1
        weight = random.randint(1, max_weight)
        graph.add_edge(u, v, weight)
        edges_set.add((u, v))
    
    # Add random edges
    while len(edges_set) < m:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v and (u, v) not in edges_set:
            weight = random.randint(1, max_weight)
            graph.add_edge(u, v, weight)
            edges_set.add((u, v))
    
    return graph

def generate_sparse_graph(n: int, m: int, max_weight: int = 1000) -> Graph:
    """Generate a sparse graph optimized for testing"""
    graph = Graph(n)
    
    # Create a tree backbone
    for i in range(1, min(n, m//2)):
        parent = random.randint(0, i-1)
        weight = random.randint(1, max_weight)
        graph.add_edge(parent, i, weight)
        if len(graph.edges) < m//2:
            graph.add_edge(i, parent, weight)
    
    # Add additional random edges
    edges_set = set((u, v) for u, v, _ in graph.edges)
    while len(graph.edges) < m:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v and (u, v) not in edges_set:
            weight = random.randint(1, max_weight)
            graph.add_edge(u, v, weight)
            edges_set.add((u, v))
    
    return graph

def generate_dense_graph(n: int, m: int, max_weight: int = 1000) -> Graph:
    """Generate a dense graph for stress testing"""
    graph = Graph(n)
    max_edges = n * (n - 1)
    m = min(m, max_edges)
    
    edges_set = set()
    while len(edges_set) < m:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v and (u, v) not in edges_set:
            edges_set.add((u, v))
    
    for u, v in edges_set:
        weight = random.randint(1, max_weight)
        graph.add_edge(u, v, weight)
    
    return graph

def write_graph_to_file(graph: Graph, sources: List[int], filename: str):
    """Write graph in the expected input format"""
    with open(filename, 'w') as f:
        f.write(f"{graph.n} {len(graph.edges)} {len(sources)}\n")
        for u, v, w in graph.edges:
            f.write(f"{u} {v} {w}\n")
        f.write(" ".join(map(str, sources)) + "\n")

def read_output(filename: str, n: int, k: int) -> List[List[int]]:
    """Read the output format: K lines, each with N distances"""
    try:
        with open(filename, 'r') as f:
            result = []
            for _ in range(k):
                line = f.readline().strip()
                if not line:
                    return None
                distances = list(map(int, line.split()))
                if len(distances) != n:
                    return None
                result.append(distances)
            return result
    except Exception:
        return None

def run_test(executable: str, graph: Graph, sources: List[int], test_name: str) -> Tuple[bool, float, float, Optional[str]]:
    """Run a single test case"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, "input.txt")
        output_file = os.path.join(tmpdir, "output.txt")
        
        # Write input
        write_graph_to_file(graph, sources, input_file)
        
        # Run the executable
        monitor = MemoryMonitor()
        start_time = time.time()
        
        try:
            with open(output_file, 'w') as outf:
                process = subprocess.Popen(
                    [executable, input_file],
                    stdout=outf,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                monitor.start_monitoring(process)
                stdout, stderr = process.communicate(timeout=30)  # 30 second timeout
                
                end_time = time.time()
                peak_memory = monitor.stop_monitoring()
                
                if process.returncode != 0:
                    return False, 0, 0, f"Process failed with return code {process.returncode}. stderr: {stderr}"
                
        except subprocess.TimeoutExpired:
            process.kill()
            return False, 0, 0, "Timeout (30s)"
        except Exception as e:
            return False, 0, 0, f"Execution error: {str(e)}"
        
        runtime = end_time - start_time
        
        # Read and verify output
        output_data = read_output(output_file, graph.n, len(sources))
        if output_data is None:
            return False, runtime, peak_memory, "Invalid output format"
        
        # Check correctness
        for i, source in enumerate(sources):
            expected = graph.dijkstra_reference(source)
            actual = output_data[i]
            
            if len(actual) != len(expected):
                return False, runtime, peak_memory, f"Wrong output length for source {source}"
            
            for j, (exp, act) in enumerate(zip(expected, actual)):
                if exp != act:
                    return False, runtime, peak_memory, f"Wrong distance from {source} to {j}: expected {exp}, got {act}"
        
        return True, runtime, peak_memory, None

def run_all_tests(executables: List[str], generate_tests: bool = False):
    """Run all test cases"""
    
    # Define test cases
    test_cases = [
        ("Small Random", lambda: generate_random_graph(100, 500), lambda: random.sample(range(100), min(10, 100))),
        ("Medium Sparse", lambda: generate_sparse_graph(1000, 5000), lambda: random.sample(range(1000), min(50, 1000))),
        ("Large Sparse", lambda: generate_sparse_graph(5000, 25000), lambda: random.sample(range(5000), min(200, 5000))),
        ("Medium Dense", lambda: generate_dense_graph(800, 20000), lambda: random.sample(range(800), min(100, 800))),
    ]
    
    if generate_tests:
        # Add stress tests
        test_cases.extend([
            ("Stress Large", lambda: generate_random_graph(15000, 150000), lambda: random.sample(range(15000), min(800, 15000))),
            ("Stress Max", lambda: generate_random_graph(20000, 200000), lambda: random.sample(range(20000), min(1000, 20000))),
        ])
    
    print("=" * 80)
    print("SHORTEST PATH ALGORITHM TESTER")
    print("=" * 80)
    
    results = {exe: {"passed": 0, "total": 0, "total_time": 0, "max_memory": 0} for exe in executables}
    
    for test_name, graph_gen, sources_gen in test_cases:
        print(f"\n--- Test: {test_name} ---")
        
        # Generate test case
        graph = graph_gen()
        sources = sources_gen()
        
        print(f"Graph: {graph.n} vertices, {len(graph.edges)} edges, {len(sources)} sources")
        
        for exe in executables:
            exe_name = os.path.basename(exe)
            print(f"\nTesting {exe_name}:")
            
            success, runtime, memory, error = run_test(exe, graph, sources, test_name)
            results[exe]["total"] += 1
            results[exe]["total_time"] += runtime
            results[exe]["max_memory"] = max(results[exe]["max_memory"], memory)
            
            if success:
                results[exe]["passed"] += 1
                status = "✓"
                color = "\033[92m"  # Green
                error_msg = ""
            else:
                status = "✗"
                color = "\033[91m"  # Red
                error_msg = f" - {error}" if error else ""
            
            print(f"  {color}[{status}] {test_name}{error_msg}\033[0m")
            print(f"      Time: {runtime:.3f}s, Memory: {memory:.1f}MB")
            
            # Check memory constraint
            if memory > 150:
                print(f"      \033[91m⚠ Memory limit exceeded (150MB)\033[0m")
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    for exe in executables:
        exe_name = os.path.basename(exe)
        stats = results[exe]
        pass_rate = (stats["passed"] / stats["total"]) * 100 if stats["total"] > 0 else 0
        avg_time = stats["total_time"] / stats["total"] if stats["total"] > 0 else 0
        
        print(f"\n{exe_name}:")
        print(f"  Tests passed: {stats['passed']}/{stats['total']} ({pass_rate:.1f}%)")
        print(f"  Average time: {avg_time:.3f}s")
        print(f"  Peak memory: {stats['max_memory']:.1f}MB")
        
        if stats["max_memory"] <= 150:
            print(f"  \033[92m✓ Memory constraint satisfied\033[0m")
        else:
            print(f"  \033[91m✗ Memory constraint violated\033[0m")

def main():
    if len(sys.argv) < 2:
        print("Usage: python tester.py executable1 [executable2 ...] [--generate]")
        sys.exit(1)
    
    args = sys.argv[1:]
    generate_tests = "--generate" in args
    if generate_tests:
        args.remove("--generate")
    
    executables = []
    for exe in args:
        if not os.path.isfile(exe):
            print(f"Error: {exe} not found")
            sys.exit(1)
        if not os.access(exe, os.X_OK):
            print(f"Error: {exe} is not executable")
            sys.exit(1)
        executables.append(exe)
    
    if not executables:
        print("Error: No valid executables provided")
        sys.exit(1)
    
    # Set random seed for reproducible tests
    random.seed(42)
    
    run_all_tests(executables, generate_tests)

if __name__ == "__main__":
    main()
