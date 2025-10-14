
# LLM Benchmarks  
**The Largest Coding Benchmark for Large Language Models**

---

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
- [For Evaluators](#for-evaluators)

---

## LLM Models

we will test many llms from 11 companies:

### 1. [OpenAI](https://chatgpt.com)
- GPT-5
- GPT-5 + Think Deeper
- GPT-5 + Web Search
- GPT-OSS-20B
- GPT-OSS-120B

### 2. [DeepSeek](https://chat.deepseek.com/)
- DeepSeek
- DeepSeek with Thinking
- DeepSeek with Web Search
- DeepSeek with Thinking + Web Search

### 3. [Qwen](https://chat.qwen.ai/)
- Qwen3-Max
- Qwen3-Max with web search

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

### 4. Grok
- Grok3
- Grok3 + DeepSearch
- Grok4
- Grok4 + DeepSearch
- Grok4 Heavy
- Grok4 Heavy + DeepSearch

### 5. Claude
- Claude Sonnet 4.1
- Claude Sonnet 4.1 with Web Search
- Claude Sonnet 4.1 with Extended Thinking
- Claude Sonnet 4.1 with Web Search + Extended Thinking
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

### 6. Gemini
- Gemini 2.5 Flash
- Gemini 2.5 Pro

### 7. Microsoft Copilot
- Copilot Fast Answer
- Copilot Think Deeper
- Copilot Smart (GPT-5)

### 8. Kimi
- Kimi K2
- Kimi K2 with Web Search
- Kimi K1.5
- Kimi K1.5 with WebSearch
- Kimi K1.5 with Thinking
- Kimi K1.5 with Web Search + Thinking

### 9. Minimax Chat

### 10. Ollama

### 11. Perplexity

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

### 1. Algorithms – Extreme Optimization

#### A1. Minimal Memory All-Pairs Shortest Paths

**Prompt:**  
You are given a weighted directed graph with up to N = 20,000 vertices and M up to 200,000 edges. Implement an algorithm that computes all-pairs shortest paths **only for K specified source vertices** (K ≤ 1000) and returns distances to all vertices for those K sources. Memory is extremely limited: your program must not allocate more than 150 MB of heap memory. Time limit: target O(K * (M log N / 4)) — show optimizations that reduce constant factors. Provide both code and a short explanation of optimizations used.

**Languages:** C, C++, Rust, Go  
**Difficulty:** Very Hard  
**Constraints:**
- No external libraries except standard library
- Memory usage ≤ 150 MB
- Use memory pools / custom allocators
- Code must fit within ~300 lines

**Acceptance Criteria:**
- Correctness on random graphs
- Peak memory under 150MB
- Runtime within 2× of optimal Dijkstra per source

**Approximate Lines:** 150–300

#### A2. Cache-Friendly kd-tree for Nearest Neighbor

**Prompt:**  
Implement a static kd-tree for 3D points (N up to 10M) optimized for minimal cache misses and compact memory layout. Provide construction and k-NN query (k ≤ 16) APIs. Emphasize contiguous storage, iterative algorithms (no recursion), and branch-minimizing traversal. Explain memory layout choices.

**Languages:** C, C++, Rust  
**Difficulty:** Very Hard  
**Constraints:**
- No recursion
- Data stored in a single contiguous block
- Include microbenchmarks

**Acceptance Criteria:**
- Correct nearest neighbors on tests
- Demonstrable cache miss reduction

**Approximate Lines:** 200

---

### 2. Computer Science Theory / Miscellaneous

#### B1. Constraint Solver — SAT Solver Core Optimization

**Prompt:**  
Implement the core of a DPLL-style SAT solver with unit propagation, watched literals, non-chronological backtracking (learning a single clause per conflict). The solver must solve crafted SAT instances up to 10^6 variables/clauses efficiently. Provide APIs: `add_clause`, `solve`. Explain heuristics used.

**Languages:** C, Rust, C++  
**Difficulty:** Very Hard  
**Constraints:**
- Must implement watched literals
- Iterative approach preferred

**Acceptance Criteria:**
- Solve small CNF benchmarks
- Demonstrate conflict-driven learning

**Approximate Lines:** 200–300

#### B2. Type Inference for a Small Functional Language

**Prompt:**  
Write a Hindley–Milner style type inference engine (including let-polymorphism and simple algebraic data types) for an ML-like language. Return principal type or error. Provide tests.

**Languages:** OCaml, Haskell, Rust, Python  
**Difficulty:** Hard  
**Constraints:**
- Prefer immutable data structures
- Show Algorithm W

**Acceptance Criteria:**
- Correct principal types for provided expressions

**Approximate Lines:** 150

---

*(... continue with the rest of the tasks similarly formatted ...)*

---

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

---

## For Evaluators

### Additional Guidance

- Request brevity: Add “Solution must be ≤ 300 lines” to each prompt
- Accept pseudocode/core proofs for very long tasks
- Encourage inclusion of minimal unit tests within responses

## license 

Distributed under the MIT License. See [LICENSE](LICENSE) file for details.

