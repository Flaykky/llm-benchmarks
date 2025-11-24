# prompts and llms used

## Table of Contents

- [List of LLM Models](#llm-models)
- [Languages and Task Ideas](#languages-and-tasks)
- [Task Prompts](#task-prompts)
  - [1. Algorithms – Extreme Optimization](#1-algorithms--extreme-optimization)
  - [2. Computer Science Theory / Miscellaneous](#2-computer-science-theory--miscellaneous)
  - [3. Frontend (Next/React/Vanilla JS)](#3-frontend-nextreactvanilla-js)
  - [4. Secure Coding / Safety-Critical](#4-secure-coding--safety-critical)
  - [5. Mobile Development (Android / iOS)](#5-mobile-development-android--ios)
  - [6. Backend](#6-backend)
  - [7. Desktop (Windows/Mac/Linux)](#7-desktop-windowsmaclinux)
  - [8. Pentest / Hardening](#8-pentest--hardening)
  - [9. Systems Programming](#9-systems-programming)
  - [10. Shell Scripts](#10-shell-scripts)
  - [11. Game Development (Unreal, Unity, Godot)](#11-game-development-unreal-unity-godot)
  - [12. Miscellaneous / Other Picks](#12-miscellaneous--other-picks)
- [Evaluation System (Rubric)](#evaluation-system-rubric)

---

## LLM Models

we will test many llms from 12 providers:

### 1. [OpenAI](https://chatgpt.com)
- GPT-5
- GPT-5 + Think Deeper
- GPT-5 + Web Search

- GPT 5.1

- GPT 4o
- GPT 4o-mini

- [GPT-OSS-20B](https://gpt-oss.com/)
- [GPT-OSS-120B](https://gpt-oss.com/)

### 2. [DeepSeek](https://chat.deepseek.com/)
- DeepSeek
- DeepSeek with Thinking
- DeepSeek with Web Search
- DeepSeek with Thinking + Web Search

### 3. [Qwen](https://chat.qwen.ai/)
- Qwen3-Max
- Qwen3-Max with web search
- Qwen3-Max with thinking 
- Qwen3-Max with thining+web search

- Qwen3-Coder
- Qwen3-Coder with Web Search

- Qwen3-Coder-Flash
- Qwen3-Coder-Flash with Web Search

- Qwen3-30B-A3B-2507
- Qwen3-30B-A3B-2507 with Web Search
- Qwen3-30B-A3B-2507 with Thinking [81,920 tokens]
- Qwen3-30B-A3B-2507 with Thinking + Web Search
- Qwen3-30B-A3B-2507 with Web Search

- Qwen3-235B-A22B-2507
- Qwen3-235B-A22B-2507 with Internet Search
- Qwen3-235B-A22B-2507 with Thinking [81,920 tokens]
- Qwen3-235B-A22B-2507 with Thinking + Web Search
- Qwen3-235B-A22B-2507 with Web Search

- Qwen3-Next-80B-A3B
- Qwen3-Next-80B-A3B with Thinking [81,920 tokens]
- Qwen3-Next-80B-A3B with Thinking + Web Search
- Qwen3-Next-80B-A3B with web search

- Qwen3-VL-235B-A22B
- Qwen3-VL-235B-A22B with thinking [81.920 tokens]

- Qwen3-VL-30B-A3B
- Qwen3-VL-30B-A3B with thinking [81.920 tokens]

- Qwen3-Omni-Flash
- Qwen3-Omni-Flash with thinking [81.920 tokens]

#### qwen2.5:

- Qwen2.5-Max
- Qwen2.5-Max with Web Search
- Qwen2.5-Max with Thinking
- Qwen2.5-Max with Thinking + web search

- Qwen2.5-Plus
- Qwen2.5-Plus with web search
- Qwen2.5-Plus with thinking
- Qwen2.5-Plus with thinking + web search

- Qwen2.5-Turbo 
- Qwen2.5-Turbo with web search
- Qwen2.5-Turbo with thinking
- Qwen2.5-Turbo with thinking + web search

- Qwen2.5-Omni-7B 
- Qwen2.5-Omni-7B with web search

- Qwen2.5-VL-23B-Instruct
- Qwen2.5-VL-23B-Instruct with web search
- Qwen2.5-VL-23B-Instruct with thinking
- Qwen2.5-VL-23B-Instruct with thinking + web search


- Qwen2.5-14B-Instruct-1M 
- Qwen2.5-14B-Instruct-1M with web search
- Qwen2.5-14B-Instruct-1M with thinking
- Qwen2.5-14B-Instruct-1M with thinking + web search

- Qwen2.5-Coder-32B-Instruct
- Qwen2.5-Coder-32B-Instruct with web search
- Qwen2.5-Coder-32B-Instruct with thinking
- Qwen2.5-Coder-32B-Instruct with thinking + web search

- Qwen2.5-72B-Instruct 
- Qwen2.5-72B-Instruct with web search
- Qwen2.5-72B-Instruct with thinking
- Qwen2.5-72B-Instruct with thinking + web search

#### QwQ:
- QwQ-32B
- QwQ-32B with web search
- QwQ-32B with thinking
- QwQ-32B with thinking + web search

### 4. [Grok](https://grok.com/)
- Grok3
- Grok3 + DeepSearch
- Grok4
- Grok4 + DeepSearch
- Grok4 Heavy
- Grok4 Heavy + DeepSearch
- Grok4.1 preview

### 5. [Claude](https://claude.ai/)
- Claude Sonnet 4.5
- Claude Sonnet 4.5 with Web Search
- Claude Sonnet 4.5 with Extended Thinking
- Claude Sonnet 4.5 with Web Search + Extended Thinking
- Claude Sonnet 4
- Claude Sonnet 4 with Web Search
- Claude Sonnet 4 with Extended Thinking
- Claude Sonnet 4 with Web Search + Extended Thinking
- Claude Sonnet 3.7
- Claude Sonnet 3.7 with Web Search
- Claude Sonnet 3.7 with Extended Thinking
- Claude Sonnet 3.7 with Web Search + Extended Thinking
- Claude Opus 4.1
- Claude Opus 4.1 with Web Search
- Claude Opus 4.1 with Extended Thinking
- Claude Opus 4.1 with Web Search + Extended Thinking
- Claude Opus 3
- Claude Opus 3 with Web Search
- Claude Opus 3 with Extended Thinking
- Claude Opus 3 with Web Search + Extended Thinking
- Claude Haiku 3.5
- Claude Haiku 3.5 with Extended Thinking

### 6. [Gemini](https://aistudio.google.com/)
- Gemini 2.5 Flash
- Gemini 2.5 Pro
- Gemini 3.0 preview 

### 7. [Microsoft Copilot](https://copilot.microsoft.com/)
- Copilot Fast Answer
- Copilot Think Deeper
- Copilot Smart (GPT-5)

### 8. [Kimi](https://www.kimi.com/)
- Kimi K2
- Kimi K2 with Web Search
- Kimi K1.5
- Kimi K1.5 with WebSearch
- Kimi K1.5 with Thinking
- Kimi K1.5 with Web Search + Thinking

### 9. Minimax Chat

### 10. Ollama

### 11. [Perplexity](https://www.perplexity.ai/)

### 12. [Mistral](https://mistral.ai/)
- Mistral default
- Mistral research
- Mistral thinking


---

## Languages and Tasks

### Tasks:
1. Highly optimized algorithms
2. Computer science theory
3. Frontend (Next.js / React / Vanilla JS)
4. Secure coding
5. Mobile development (Android / iOS)
6. Backend systems
7. Desktop applications (Windows, macOS, Linux)
8. Penetration testing and security hardening
9. Systems programming
10. Shell scripting
11. Game development (Unreal Engine, Unity, Godot)

### Programming Languages:
1. **Python** – widely supported by LLMs
2. **C** – requires careful memory management
3. **Rust** – modern, safe systems language
4. **C#** – used for Windows apps and Unity
5. **C++** – used for performance-critical applications
6. **Kotlin** – primary Android development
7. **Java** – versatile backend and mobile language
8. **Go** – efficient for backend and networking
9. **Lisp/Haskell** – functional programming
10. **Bash** – shell scripting
11. **Assembly** – low-level performance tuning

---

## Task Prompts

# 1. Algorithms — Extreme Optimization

### **A1. Minimal-Memory Multi-Source Shortest Paths**

```txt
You are a senior systems engineer focused on high-performance graph algorithms.
Write in **{lang}** an implementation of multi-source shortest paths for a directed weighted graph:
- N ≤ 20,000
- M ≤ 200,000
- K ≤ 1000 (sources)

Requirements:
- Use optimized Dijkstra per source.
- Limit heap usage to ≤150 MB.
- Use memory pools or custom allocators.
- Favor compact adjacency layout and reduced constant factors.
- Output distances for all K sources.

Constraints:
- No external libraries.
- Code length ≤300 lines.

Output format:
1. Code.
2. Explanation of memory optimizations (<300 words).
```

---

### **A2. Cache-Friendly KD-Tree (3D, N ≤ 10M)**

```txt
You are a performance engineer specializing in memory locality.
Write in **{lang}** a static 3D kd-tree implementation with:

Requirements:
- N up to 10 million points.
- Single contiguous memory block for nodes.
- No recursion (iterative build and search).
- k-NN queries with k ≤ 16.
- Minimize branches and cache misses.
- Include a minimal microbenchmark suite.

Constraints:
- No external libraries.
- Output code ≤200 lines (not counting benchmarks).

Output format:
1. Code.
2. Memory layout diagram (ASCII).
3. Explanation (<300 words).
```

---

### **A3. SIMD-Optimized Matrix Multiply (Blocked)**

```txt
You are an expert in low-level optimization.
Write in **{lang}** a blocked matrix multiplication implementation:

Requirements:
- Support matrices up to 8192x8192 (float32).
- Use cache-friendly tiling.
- Use intrinsics/SIMD available in the language.
- Provide fallback for systems without vectorization.

Constraints:
- No external libraries.

Output:
Code + explanation (<300 words).
```

---

# 2. Computer Science Theory

### **B1. SAT Solver Core (DPLL + Watched Literals + Learning)**

```txt
You are a compiler engineer specialized in formal logic.
Write in **{lang}** a minimal DPLL SAT solver with:

Requirements:
- Watched literals.
- Non-chronological backtracking.
- One learned clause per conflict.
- Efficient unit propagation.

Constraints:
- Handle up to 10^6 variables/clauses.
- No recursion preferred.
- No external libraries.

Output:
Code + explanation (<300 words).
```

---

### **B2. Hindley–Milner Type Inference (Algorithm W)**

```txt
You are a functional programming researcher.
Write in **{lang}** an implementation of Algorithm W for an ML-like language.

Requirements:
- Support let-polymorphism.
- Support simple algebraic data types.
- Return principal types or errors.
- Provide 5 tests.

Constraints:
- Prefer immutable structures.

Output:
Code + explanation.
```

---

# 3. Frontend (Next.js / React / Vanilla JS)

### **C1. React Virtualized Table (100k rows)**

```txt
You are a frontend performance engineer.
Write in **{lang} (JS/TS)** a React component implementing a virtualized table for 100,000 rows.

Requirements:
- Minimal re-renders.
- Uses only windowing (no external libs).
- Keyboard navigation.
- Smooth scrolling.

Output:
JS/TS code + explanation.
```

---

### **C2. Next.js SSR + Streaming API Endpoint**

```txt
You are a full-stack engineer.
Write in **{lang}** a Next.js route that streams incremental JSON chunks to the browser.

Requirements:
- No external libraries.
- Must work on the Edge runtime.
- Include client-side code to consume the stream.

Output:
Server code + client code + explanation.
```

---

# 4. Secure Coding

### **D1. Hardened Input Parser (Memory-Safe)**

```txt
You are a security engineer.
Write in **{lang}** a hardened parser for a custom binary protocol.

Requirements:
- Bounds checking for every field.
- Reject malformed data.
- Zero-copy where possible.

Output:
Code + brief threat model (<200 words).
```

---

### **D2. Sandbox Executor**

```txt
You are a systems security architect.
Write in **{lang}** a minimal sandbox for executing untrusted user code.

Requirements:
- Limit CPU time.
- Limit memory.
- No file system access.
- No external libraries.

Output:
Code + explanation of isolation model.
```

---

# 5. Mobile Development

### **E1. Android Offline-First Notes App (Kotlin)**

```txt
You are a mobile developer.
Write in Kotlin a minimal Android app:

Requirements:
- Compose UI.
- Local encrypted storage.
- Offline-first sync mock API.
- ViewModel + Repository structure.

Output:
Code + architecture summary.
```

---

### **E2. iOS SwiftUI Image Pipeline**

```txt
You are an iOS engineer.
Write in Swift a SwiftUI async image loader with:

Requirements:
- Memory cache.
- Disk cache.
- Background decoding.
- Cancellation support.

Output:
Code + explanation.
```

---

# 6. Backend Systems

### **F1. Go Microservice + Load Shedding**

```txt
You are a backend performance engineer.
Write in Go a small HTTP service with:

Requirements:
- Adaptive load shedding.
- Connection pooling.
- Graceful shutdown.
- Structured logging.

Output:
Code + explanation.
```

---

### **F2. Java High-Throughput Queue Processor**

```txt
You are a JVM performance specialist.
Write in Java a batch queue processor:

Requirements:
- Work-stealing.
- Backpressure.
- Metrics for latency and throughput.

Output:
Code + explanation.
```

---

# 7. Desktop Applications (Win/Mac/Linux)

### **G1. C# WPF Minimal Editor (Async I/O)**

```txt
You are a desktop engineer.
Write in C# a WPF text editor with:

Requirements:
- Async file loading.
- Undo/redo stack.
- Autosave.

Output:
Code + explanation.
```

---

### **G2. Cross-Platform File Watcher (Rust)**

```txt
You are a systems developer.
Write in Rust a file-watcher using platform APIs:

Requirements:
- inotify on Linux
- ReadDirectoryChangesW on Windows
- FSEvents on macOS

Output:
Rust code + explanation.
```

---

# 8. Pentest / Hardening

*(все промты сформулированы так, чтобы быть техническими и безопасными)*

### **H1. Secure TLS Configuration Auditor**

```txt
You are a security auditor.
Write in **{lang}** a TLS configuration checker:

Requirements:
- Validate cipher suites.
- Detect deprecated protocols.
- Provide secure recommendations.

Output:
Code + explanation.
```

---

### **H2. Container Isolation Analyzer**

```txt
You are a cloud security engineer.
Write in **{lang}** a tool that inspects container runtime settings:

Requirements:
- Check namespaces.
- Check capabilities.
- Check cgroup limits.
- Provide a safety score.

Output:
Code + explanation.
```

---

# 9. Systems Programming

### **I1. Custom Allocator (Arena)**

```txt
You are a low-level systems engineer.
Write in **{lang}** a high-performance arena allocator:

Requirements:
- Single contiguous region.
- Fast bump pointer.
- Reset support.
- Thread-safe variant.

Output:
Code + explanation.
```

---

### **I2. Minimal Cooperative Scheduler**

```txt
You are an OS engineer.
Write in **{lang}** a cooperative scheduler:

Requirements:
- Fibers/green threads.
- Round-robin.
- No OS threading primitives.

Output:
Code + explanation.
```

---

# 10. Shell Scripts

### **J1. Log Aggregator**

```txt
You are a DevOps engineer.
Write in Bash a log aggregator with:

Requirements:
- Parallel tailing of multiple files.
- Colored output.
- Filtering by pattern.

Output:
Code + explanation.
```

---

### **J2. Backup Verifier**

```txt
You are responsible for reliability.
Write in Bash:

Requirements:
- Verify SHA256 of backup directories.
- Incremental comparison.
- Summary report.

Output:
Code + explanation.
```

---

# 11. Game Development (Unreal/Unity/Godot)

### **K1. Unity ECS Particle System**

```txt
You are a game engine engineer.
Write in C# a Unity DOTS/ECS particle system:

Requirements:
- Burst-compiled.
- Jobs system.
- GPU-friendly layout.

Output:
Code + explanation.
```

---

### **K2. Godot 4 Navigation AI**

```txt
You are an AI gameplay developer.
Write in GDScript:

Requirements:
- Agent pathfinding.
- Dynamic obstacle updates.
- Smooth steering.

Output:
Code + explanation.
```

---

# 12. Miscellaneous

### **L1. Assembly Routine (SIMD String Compare)**

```txt
You are a low-level engineer.
Write in Assembly a SIMD-accelerated string equality check.

Requirements:
- Compare up to 4k bytes.
- Return first mismatch index or -1.

Output:
Code + explanation.
```


## Evaluation System (Rubric)

### Per-Task Scoring (100-point scale)

| Category                          | Points |
|----------------------------------|--------|
| Correctness & Functional Tests   | 40     |
| Performance & Resource Limits    | 20     |
| Security & Robustness            | 15     |
| Adherence to Constraints         | 10     |
| Code Quality, Readability        | 10     |
| Tests & Reproducibility          | 5      |

### Scoring Notes
- Partial solutions (e.g., design only) can receive up to 25 points.
- Disallowed external libraries deduct up to 10 points from "Adherence".

### Aggregation Across Tasks

Default weights for evaluation categories:

| Category               | Weight |
|-----------------------|--------|
| Algorithms            | 0.12   |
| CS Theory             | 0.10   |
| Frontend              | 0.08   |
| Secure Coding         | 0.12   |
| Mobile                | 0.08   |
| Backend               | 0.12   |
| Desktop               | 0.06   |
| Pentest/Hardening     | 0.08   |
| Systems               | 0.08   |
| Shell Scripts         | 0.03   |
| GameDev               | 0.05   |
| Misc/FP/Assembly      | 0.08   |

### Capability Levels

| Score Range | Level     | Description |
|-------------|-----------|-------------|
| 0–29        | Novice    | Basic snippets, often incorrect |
| 30–54       | Competent | Works on easy/medium tasks |
| 55–74       | Advanced  | Good performance, some edge cases missed |
| 75–89       | Expert    | High correctness, strong tests |
| 90–100      | Architect | Production-ready, well-documented |

### Practical Evaluation Checklist

1. Run unit/integration tests
2. Measure memory and runtime
3. Run fuzz tests for parsers/security tasks
4. Check constraint adherence (e.g., banned APIs)
5. Review comments and threat models
6. Evaluate modularization if task is large



