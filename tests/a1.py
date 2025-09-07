import argparse
import os
import subprocess
import time
import psutil
import tempfile
import random

# ------------------ Graph generator ------------------
def generate_graph(n, m, k, filename):
    with open(filename, 'w') as f:
        f.write(f"{n} {m} {k}\n")
        sources = random.sample(range(1, n + 1), k)
        f.write(" ".join(map(str, sources)) + "\n")
        edges = set()
        while len(edges) < m:
            u = random.randint(1, n)
            v = random.randint(1, n)
            if u != v:
                w = random.randint(1, 1000)
                edges.add((u, v, w))
        for u, v, w in edges:
            f.write(f"{u} {v} {w}\n")

# ------------------ Run binary with measurement ------------------
def run_binary(binary, graph_file, timeout=60):
    with open(graph_file, 'r') as fin:
        start = time.time()
        proc = psutil.Popen([binary], stdin=fin, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            max_mem = 0
            while proc.is_running():
                try:
                    mem = proc.memory_info().rss
                    max_mem = max(max_mem, mem)
                except psutil.NoSuchProcess:
                    break
                time.sleep(0.01)
            stdout, stderr = proc.communicate(timeout=timeout)
            retcode = proc.wait()
        except subprocess.TimeoutExpired:
            proc.kill()
            return None, None, None, "timeout"
        end = time.time()
        return retcode, stdout.decode(), max_mem, end - start

# ------------------ Reference checker ------------------
def reference_solver(graph_file):
    # Simple Dijkstra-based correctness checker (slow but fine for small graphs)
    import heapq
    with open(graph_file) as f:
        n, m, k = map(int, f.readline().split())
        sources = list(map(int, f.readline().split()))
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            adj[u].append((v, w))
    results = {}
    for s in sources:
        dist = [float('inf')] * (n+1)
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        results[s] = dist[1:]
    return results

# ------------------ Compare output ------------------
def parse_output(text):
    # Assume output: K lines, each N ints or -1 for INF
    lines = [list(map(int, l.split())) for l in text.strip().splitlines()]
    return lines

def compare_results(ref, out):
    # Flatten ref and out for comparison
    ref_lines = []
    for s, dists in ref.items():
        ref_lines.append([d if d < 10**9 else -1 for d in dists])
    return ref_lines == out

# ------------------ Main ------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('binaries', nargs='+')
    parser.add_argument('--graph', help='Graph file to test')
    parser.add_argument('--generate', action='store_true', help='Generate random graph')
    parser.add_argument('--n', type=int, default=200, help='Vertices')
    parser.add_argument('--m', type=int, default=1000, help='Edges')
    parser.add_argument('--k', type=int, default=10, help='Sources')
    args = parser.parse_args()

    if args.graph:
        graph_file = args.graph
    else:
        fd, graph_file = tempfile.mkstemp(suffix='.txt')
        os.close(fd)
        generate_graph(args.n, args.m, args.k, graph_file)

    ref = reference_solver(graph_file)

    for binary in args.binaries:
        print(f"\n>>> Testing {binary}")
        ret, out, mem, t = run_binary(binary, graph_file)
        if ret != 0:
            print(f"[✘] Runtime error (code {ret})")
            continue
        try:
            parsed = parse_output(out)
            ok = compare_results(ref, parsed)
        except Exception as e:
            print(f"[✘] Output parse error: {e}")
            ok = False
        if ok:
            print(f"[✔] Correctness passed")
        else:
            print(f"[✘] Wrong answer")
        print(f"Time: {t:.3f}s, Max RSS: {mem/1024/1024:.1f} MB")

if __name__ == "__main__":
    main()
