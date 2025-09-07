#!/usr/bin/env python3
import subprocess
import sys
import time
import os
import tempfile
import psutil
from typing import List

# --- Configurable graph generator ---
def generate_graph(n=10, m=20, k=2):
    """Returns a string with graph in input format."""
    import random
    edges = set()
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v and (u, v) not in edges:
            edges.add((u, v))
    res = [f"{n} {m}"]
    for (u, v) in edges:
        w = random.randint(1, 100)
        res.append(f"{u} {v} {w}")
    res.append(str(k))
    for _ in range(k):
        res.append(str(random.randint(1, n)))
    return "\n".join(res) + "\n"

# --- Core testing ---
def run_binary(binary: str, input_data: str):
    """Run binary with given input, capture output, measure time and memory."""
    with tempfile.NamedTemporaryFile(delete=False) as tmpin:
        tmpin.write(input_data.encode())
        tmpin.flush()
        tmpin_name = tmpin.name

    start = time.perf_counter()
    proc = subprocess.Popen([binary],
                            stdin=open(tmpin_name, 'rb'),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    pid = proc.pid
    ps_proc = psutil.Process(pid)
    peak_mem = 0
    # Poll memory while running
    while proc.poll() is None:
        try:
            mem = ps_proc.memory_info().rss
            if mem > peak_mem:
                peak_mem = mem
        except psutil.NoSuchProcess:
            break
        time.sleep(0.01)
    end = time.perf_counter()

    stdout, stderr = proc.communicate()
    os.unlink(tmpin_name)
    return {
        "exitcode": proc.returncode,
        "time_sec": end - start,
        "peak_mem_mb": peak_mem / (1024 * 1024),
        "stdout": stdout.decode(errors="replace"),
        "stderr": stderr.decode(errors="replace"),
    }

def compare_outputs(out1: str, out2: str) -> bool:
    """Compare two outputs ignoring trailing spaces/newlines."""
    norm1 = "\n".join(line.strip() for line in out1.strip().splitlines())
    norm2 = "\n".join(line.strip() for line in out2.strip().splitlines())
    return norm1 == norm2

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} binary1 [binary2 ...] graphs.txt|--generate")
        sys.exit(1)

    binaries = []
    graphs_file = None
    for arg in sys.argv[1:]:
        if os.path.isfile(arg) and os.access(arg, os.X_OK):
            binaries.append(arg)
        else:
            graphs_file = arg

    # Load or generate graphs
    graph_inputs: List[str] = []
    if graphs_file == "--generate":
        for _ in range(3):
            graph_inputs.append(generate_graph(n=50, m=200, k=3))
    else:
        with open(graphs_file) as f:
            data = f.read().strip()
        # Support multiple graphs separated by "----"
        graph_inputs = [g.strip() + "\n" for g in data.split("----")]

    # Run all binaries on all graphs
    for idx, graph_data in enumerate(graph_inputs):
        print(f"\n=== Graph #{idx+1} ===")
        reference_output = None
        for binary in binaries:
            print(f"\nRunning {binary}...")
            result = run_binary(binary, graph_data)
            print(f"Exit code: {result['exitcode']}")
            print(f"Time: {result['time_sec']:.3f} sec")
            print(f"Peak RSS: {result['peak_mem_mb']:.1f} MB")
            if result['stderr'].strip():
                print(f"Stderr:\n{result['stderr']}")
            if reference_output is None:
                reference_output = result['stdout']
                print("Output saved as reference.")
            else:
                same = compare_outputs(reference_output, result['stdout'])
                print("Output matches reference:" if same else "Output differs from reference!")
    print("\nDone.")

if __name__ == "__main__":
    main()
