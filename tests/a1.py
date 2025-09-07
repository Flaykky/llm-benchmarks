#!/usr/bin/env python3
import argparse
import os
import subprocess
import tempfile
import time
import psutil
import hashlib

# --- Graph generation (simple placeholder) ---
def generate_graphs():
    graphs = []
    # tiny test
    g1 = "10 9\n" + "\n".join(f"{i} {i+1} 1" for i in range(1, 10)) + "\n1\n1\n"
    graphs.append(("linear_10.txt", g1))
    # random test (placeholder, replace with real generator)
    import random
    n = 100
    m = 300
    edges = "\n".join(
        f"{random.randint(1,n)} {random.randint(1,n)} {random.randint(1,100)}"
        for _ in range(m)
    )
    g2 = f"{n} {m}\n{edges}\n1\n1\n"
    graphs.append(("random_100.txt", g2))
    return graphs

# --- run program, measure time and memory ---
def run_program(executable, input_data):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_in:
        tmp_in.write(input_data.encode())
        tmp_in.flush()
        tmp_in_name = tmp_in.name

    start_time = time.perf_counter()
    proc = psutil.Popen([executable],
                        stdin=open(tmp_in_name, "rb"),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    peak_memory = 0
    try:
        while proc.is_running():
            try:
                mem = proc.memory_info().rss
                peak_memory = max(peak_memory, mem)
            except psutil.NoSuchProcess:
                break
            time.sleep(0.01)
    finally:
        stdout, stderr = proc.communicate()
    elapsed = time.perf_counter() - start_time
    os.unlink(tmp_in_name)
    return stdout.decode(errors="ignore"), stderr.decode(errors="ignore"), elapsed, peak_memory

# --- compare outputs (normalize whitespaces) ---
def normalize_output(out):
    return "\n".join(" ".join(line.split()) for line in out.strip().splitlines())

def hash_output(out):
    return hashlib.sha256(normalize_output(out).encode()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("executables", nargs="+", help="Paths to compiled binaries")
    parser.add_argument("--generate", action="store_true", help="Generate graphs instead of using .txt files")
    parser.add_argument("--graphs", nargs="*", help="Paths to .txt graphs")
    parser.add_argument("--max-mem", type=int, default=150*1024*1024, help="Max allowed RAM (bytes)")
    args = parser.parse_args()

    if args.generate:
        graphs = generate_graphs()
    else:
        graphs = []
        for gpath in args.graphs:
            with open(gpath, "r") as f:
                graphs.append((os.path.basename(gpath), f.read()))

    for gname, gdata in graphs:
        print(f"\n=== Testing graph: {gname} (size: {len(gdata.splitlines())} lines) ===")
        reference_hash = None
        for exe in args.executables:
            print(f"\n-> Testing {exe}:")
            out, err, elapsed, peak_mem = run_program(exe, gdata)
            h = hash_output(out)
            if reference_hash is None:
                reference_hash = h
                truth_ok = True
            else:
                truth_ok = (h == reference_hash)
            print(f"   [ {'✔' if truth_ok else '✖'} ] correctness check")
            print(f"   [ {'✔' if peak_mem <= args.max_mem else '✖'} ] RAM usage: {peak_mem/1024/1024:.1f} MB (limit {args.max_mem/1024/1024:.1f} MB)")
            print(f"   Time: {elapsed:.3f} s")
            if err.strip():
                print(f"   stderr: {err.strip()}")

if __name__ == "__main__":
    main()
