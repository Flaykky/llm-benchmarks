# llm-benchmarks
largest llm coding benchmark

## llm modeles 

1. OpenAI:

- GPT5 
- GPT5 + think deeper
- GPT5 + web search
- GPT-oss-20B
- GPT-oss-120B

2. Deepseek:

- Deepseek 
- Deepseek with thinking
- Deepseek with web search
- Deepseek with thinking + web search

3. Qwen:

- Qwen3-Coder
- Qwen3-Coder with web search
- Qwen3-Coder-Flash
- Qwen3-Coder-Flash with web search
- Qwen3-30B-A3B-2507
- Qwen3-30B-A3B-2507 with web search
- Qwen3-30B-A3B-2507 with thinking [81,920 tokens]
- Qwen3-30B-A3B-2507 with thinking + web search
- Qwen3-235B-A22B-2507 
- Qwen3-235B-A22B-2507 with internet search
- Qwen3-235B-A22B-2507 with thinking [81,920 tokens]
- Qwen3-235B-A22B-2507 with thinking + web search
- Qwen2.5-Max 
- Qwen2.5-Max with web search
- Qwen2.5-Max with thinking 
- Qwen2.5-Max with thinking + internet search

4. Grok:

- Grok3
- Grok3 + deepsearch

- Grok4
- Grok4 + deepsearch

- Grok4 heavy
- Grok4 heavy + deepsearch

5. Claude:

- Claude Sonnet 4.1 
- Claude Sonnet 4.1 with web search 
- Claude Sonnet 4.1 with web search + extended thinking
- Claude Sonnet 4.1 with extended thinking

- Claude Sonnet 4
- Claude Sonnet 4 with web search 
- Claude Sonnet 4 with web search + extended thinking
- Claude Sonnet 4 with extended thinking

- Claude Sonnet 3.7
- Claude Sonnet 3.7 with web search 
- Claude Sonnet 3.7 with web search + extended thinking
- Claude Sonnet 3.7 with extended thinking

- Claude Opus 4.1 
- Claude Opus 4.1 with web search 
- Claude Opus 4.1 with web search + extended thinking
- Claude Opus 4.1 with extended thinking

- Claude Opus 3
- Claude Opus 3 with web search 
- Claude Opus 3 with web search + extended thinking
- Claude Opus 3 with extended thinking

- Claude Haiku 3.5
- Claude Haiku 3.5 with extended thinking

6. Gemini:

- Gemini 2.5 Flash
- Gemini 2.5 Pro

7. Microsoft copilot:

- Copilot fast answer 
- Copilot Think Deeper
- Copilot smart (gpt-5)

8. Kimi:

- Kimi k2 
- Kimi k2 with web search
- Kimi k1.5 
- Kimi k1.5 with websearch
- Kimi k1.5 with thinking
- Kimi k1.5 with web search + thinking

## tasks for llm

1) Algorithms — extreme optimization
A1. “Minimal Memory All-Pairs Shortest Paths”

Prompt:
You are given a weighted directed graph with up to N = 20,000 vertices and M up to 200,000 edges. Implement an algorithm that computes all-pairs shortest paths only for K specified source vertices (K ≤ 1000) and returns distances to all vertices for those K sources. Memory is extremely limited: your program must not allocate more than 150 MB of heap memory. Time limit: target O(K * (M log N / 4)) — show optimizations that reduce constant factors. Provide both code and a short explanation of optimizations used.

Languages: C, C++, Rust, Go
Difficulty: Very hard
Constraints (mandatory):

No external libraries except standard library.

Memory usage ≤ 150 MB measured by peak resident memory.

Use memory pools / custom allocators where helpful.

Solutions must fit within ~300 lines (or document split modules if needed).
Acceptance:

Correctness on random graphs (will be tested).

Peak memory under 150MB on large synthetic graph.

Runtime within 2× of optimal Dijkstra per source on sparse graphs.
Approx lines: 150–300

A2. “Cache-friendly kd-tree for nearest neighbor”

Prompt:
Implement a static kd-tree for 3D points (N up to 10M) optimized for minimal cache misses and compact memory layout. Provide construction and k-NN query (k ≤ 16) APIs. Emphasize contiguous storage, iterative algorithms (no recursion allowed), and branch-minimizing traversal. Explain memory layout choices.

Languages: C, C++, Rust
Difficulty: Very hard
Constraints:

No recursion.

Data stored in a single contiguous memory block.

Provide performance microbenchmarks on synthetic data (time per query).
Acceptance:

Correct nearest neighbors on tests.

Demonstrable improvement of cache misses (explain using theory / counters if available).
Approx lines: 200

2) Computer Science theory / miscellanea
B1. “Constraint solver — SAT solver core optimization”

Prompt:
Implement the core of a DPLL-style SAT solver with unit propagation, watched literals, non-chronological backtracking (learning a single clause per conflict). The solver must solve crafted SAT instances up to 10^6 variables clauses efficiently. Provide APIs: add_clause, solve. Explain heuristics used.

Languages: C, Rust, C++
Difficulty: Very hard
Constraints:

Must implement watched literals.

Use iterative approach; recursion allowed but depth must be bounded.
Acceptance: Solve CNF benchmarks (small) and demonstrate conflict-driven learning correctness.
Approx lines: 200–300

B2. “Type inference for a small functional language”

Prompt:
Write a Hindley–Milner style type inference engine (including let-polymorphism and simple algebraic data types) for an ML-like language. Return principal type or error. Provide tests.

Languages: OCaml, Haskell, Rust, Python
Difficulty: Hard
Constraints:

Prefer immutable data structures; show algorithm W.

Limit recursion depth for type substitution to avoid blowups.
Acceptance: Correct principal types for provided expressions and ADTs.
Approx lines: 150

3) Frontend (Next/React/Vanilla JS)
C1. “Highly-performant virtualized spreadsheet”

Prompt:
Implement a web component (React/Vanilla JS) that renders a spreadsheet grid of size 1,000,000 × 1000 using virtualization. Support cell editing, copy/paste, and formula evaluation for basic arithmetic and references (e.g., =A1+B2). Must be responsive and memory-efficient.

Languages: React (Next.js), TypeScript, Vanilla JS
Difficulty: Very hard
Constraints:

No external virtualization libraries; implement your own windowing.

Keep DOM nodes ≤ 200 at any time.

Provide tests and performance measurements (render time, memory).
Acceptance: Correct scroll behavior, formula correctness, low DOM node count.
Approx lines (component + helpers): 200

C2. “Accessible, secure chat widget”

Prompt:
Create a small secure chat widget in React that sanitizes user input, defends against XSS, supports end-to-end message encryption (client-side) using Web Crypto API, and shows secure UI. Provide a server protocol mock (no server implementation required) and explain threat model.

Languages: React + TypeScript, Vanilla JS
Difficulty: Hard
Constraints:

No dangerouslySetInnerHTML; sanitize all rendered content.

Use Web Crypto API for encryption (show code for key generation & message encryption).
Acceptance: Clean UI, documented crypto usage, sanitized rendering.
Approx lines: 150

4) Secure coding / safety-critical
D1. “Prototype secure messenger backend”

Prompt:
Design and implement a prototype of a messaging backend focusing on security. Requirements: authenticated user registration (password hashing with Argon2), end-to-end message delivery simulation (store only ciphertext on server), message deletion (forward secrecy simulated via key rotation), replay protection, and defense against common attacks (SQL injection, timing attacks). Provide a minimal client to demonstrate E2E encryption. Include threat model and code comments explaining safety-critical choices.

Languages: Rust (recommended), Go, Java
Difficulty: Very hard (security-focused)
Constraints:

Use libs only for crypto primitives (Argon2, X25519, XSalsa20/ChaCha20-Poly1305). No high-level messenger frameworks.

Server stores only ciphertext and minimal metadata.

Demonstrate key rotation and deletion semantics.
Acceptance: Security checklist satisfied, correctness of crypto flows, tests simulating attack vectors.
Approx lines: 250

D2. “Memory-safe C module for parsing untrusted data”

Prompt:
Write a C library function that parses a custom binary message format (fields with length prefixes) and returns allocated structures. It must be hardened against buffer overflows, integer overflows, and resource-exhaustion DoS. Provide fuzz-testing harness and explain mitigation techniques.

Languages: C (must show defensive coding), Rust (for comparison)
Difficulty: Hard
Constraints:

No strcpy/sprintf etc. Use bounds-checked parsing.

Always validate length fields before allocations.
Acceptance: Passes fuzz-harness (no crashes for many iterations), no undefined behavior on ASAN.
Approx lines: 150

5) Mobile (Android / iOS)
E1. “Offline-first syncing with CRDTs (mobile)”

Prompt:
Implement a minimal CRDT-based note syncing system for mobile: local data store, CRDT merge logic, and conflict-free merge protocol. Provide a simple Android (Kotlin) client that can simulate offline edits and then merge. Focus on correctness over UI.

Languages: Kotlin (Android), Swift (iOS), Rust (shared core)
Difficulty: Hard
Constraints:

Use a compact CRDT (e.g., RGA or JSON-CRDT).

Provide deterministic merge tests and serialization format.
Acceptance: Convergent state after merges; deterministic conflict resolution.
Approx lines: 200

E2. “Android secure biometric-protected vault”

Prompt:
Create an Android Kotlin module that provides secure storage of small secrets protected by biometric authentication. Use Android Keystore correctly, avoid storing secrets in files or SharedPreferences. Provide sample usage and threat analysis.

Languages: Kotlin
Difficulty: Medium
Constraints:

Use Android Keystore with user-auth-required key.

Show correct fallback behavior if biometrics unavailable.
Acceptance: Demonstrable key creation & encryption/decryption flows.
Approx lines: 120

6) Backend
F1. “High-throughput RPC server”

Prompt:
Implement a high-throughput RPC server that supports streaming requests (multiplexed), backpressure, and graceful shutdown. Provide client and benchmark harness to demonstrate throughput on many concurrent clients (1000+). Show CPU/memory limits and how server enforces them.

Languages: Go, Rust, Java
Difficulty: Very hard
Constraints:

Use only stdlibs; implement protocol over TCP.

Include connection pooling & worker model.
Acceptance: Correctness, benchmarks showing linear scalability up to given cores.
Approx lines: 250

F2. “Type-safe GraphQL-like query executor”

Prompt:
Implement a minimal, type-safe GraphQL executor for a statically-typed language (Rust/Go/Java). Support query parsing, selection sets, and resolvers with batching. Prevent query injection and depth-exploit (limit depth & complexity).

Languages: Rust, Go, Java
Difficulty: Hard
Constraints:

Must implement cost analysis for queries.

No dynamic eval or unsafe parsing patterns.
Acceptance: Correct results and robust defense against overly-expensive queries.
Approx lines: 180

7) Desktop (Windows/Mac/Linux)
G1. “Cross-platform sandboxed plugin host”

Prompt:
Design and implement a desktop application host (e.g., for audio plugins) that runs third-party plugins in isolated OS processes with a strict IPC protocol. Must prevent plugin from reading host files/keys. Provide a plugin API and a sandboxed plugin example.

Languages: C/C++, Rust (host + plugin), or C# (Windows)
Difficulty: Very hard
Constraints:

Use OS-level sandboxing (seccomp on Linux, App Sandbox on macOS, job objects/ACLs on Windows).

Implement heartbeat & kill on misbehavior.
Acceptance: Plugin cannot list host files in tests; host continues stable after plugin crash.
Approx lines: 250

G2. “Efficient cross-platform file watcher”

Prompt:
Implement a cross-platform file watching service with a unified API that uses inotify on Linux, FSEvents on macOS, and ReadDirectoryChangesW on Windows. Provide robust handling of spurious events and rename/move semantics.

Languages: Rust, Go, C#
Difficulty: Medium–Hard
Constraints:

Must handle large directories (100k files) with low CPU.
Acceptance: Accurate events under test scenarios.
Approx lines: 150

8) Pentest / hardening
H1. “Hardened web app — threat exercises”

Prompt:
Given a small Express/Flask web app skeleton, implement hardened versions of endpoints to resist CSRF, XSS, SQLi, RCE via file upload, auth bypass, and session fixation. Deliver both secure code and a short list of attack payloads attempted (and how they are mitigated).

Languages: Node.js (JS/TS), Python (Flask)
Difficulty: Hard
Constraints:

Demonstrate input validation, CSP, secure cookies, parameterized queries, file upload sandboxing.
Acceptance: All provided attack payloads fail; app still functional.
Approx lines: 120–180

H2. “Simulated exploit & patch cycle”

Prompt:
Provide a minimal native service with a deliberate vulnerability (e.g., use-after-free or SQLi). Then write an exploit (proof-of-concept) and a secure patch. Document timeline and mitigations.

Languages: C/C++ for service; Python/C for exploit
Difficulty: Hard (ethical)
Constraints:

Exploit is only for demonstration; include clear safety explanation and responsible disclosure steps.
Acceptance: Exploit works in local lab; patched version not vulnerable.
Approx lines: 200

9) Systems programming
I1. “User-space filesystem (FUSE) optimized”

Prompt:
Implement a user-space filesystem via FUSE that provides a compressed, deduplicated backing store. Focus on performance: low CPU overhead, good caching strategy, and crash consistency.

Languages: C, Rust, Go (with FUSE bindings)
Difficulty: Very hard
Constraints:

Crash-consistent metadata updates (journaling).

Demonstrate read/write throughput benchmarks.
Acceptance: Functional filesystem; recoverable after simulated crash; good throughput.
Approx lines: 250

I2. “Lock-free multi-producer/multi-consumer queue”

Prompt:
Implement a wait-free or lock-free MPMC queue for variable-sized entries in shared memory. Document memory ordering, ABA mitigation, and provide microbenchmarks.

Languages: C, C++, Rust
Difficulty: Very hard
Constraints:

No global locks; use atomic primitives only.

Correct under heavy contention.
Acceptance: Correctness + benchmarks.
Approx lines: 200

10) Shell scripts
J1. “Robust deployment script”

Prompt:
Write a POSIX-compliant shell script for zero-downtime deployment of a web service using symlink swapping and health checks. Should be idempotent, handle partial failures, and roll back.

Languages: Bash / POSIX sh
Difficulty: Medium
Constraints:

No GNU-only features — must be POSIX-compatible.

Provide logging and retry logic.
Acceptance: Simulated deployment tests succeed and rollback works.
Approx lines: 150

J2. “Safe system scanner & remediation script”

Prompt:
Create a shell script that scans a Linux system for dangerous misconfigurations (world-writable /tmp, weak SSH config, old packages) and optionally applies safe remediation with confirmations. Emphasize caution and idempotence.

Languages: Bash
Difficulty: Medium
Constraints:

Must not delete files without explicit confirmation.
Acceptance: Produces reports and remediates when confirmed.
Approx lines: 120

11) GameDev (Unreal, Unity, Godot)
K1. “Deterministic lockstep multiplayer core”

Prompt:
Implement a deterministic lockstep simulation engine for real-time multiplayer (simple RTS) with rollback and state checkpointing. Demonstrate desync detection and correction.

Languages: C# (Unity), C++ (Unreal), GDScript (Godot)
Difficulty: Very hard
Constraints:

Deterministic simulation: avoid floating point non-determinism (use fixed-point).

Provide network replay and desync test harness.
Acceptance: No desyncs in provided test scenarios.
Approx lines: 250

K2. “High-performance particle system”

Prompt:
Implement a CPU-GPU particle system with GPU instancing and a minimal shader for particle physics. Show batching, culling, and LOD to handle millions of particles.

Languages: C++/HLSL (Unreal), C#/ShaderLab (Unity), GDScript + GLES shader (Godot)
Difficulty: Hard
Constraints:

Efficient upload strategy (SSBO/instance buffer).
Acceptance: High particle counts with acceptable frame time.
Approx lines: 180

12) Misc / other picks
L1. “Assembly micro-kernel routine”

Prompt:
Write a hand-optimized x86_64 assembly routine that performs high-throughput memory copy with vectorization and non-temporal stores for large buffers. Provide C wrapper and benchmarks.

Languages: x86_64 assembly + C
Difficulty: Hard
Constraints:

Use SIMD (AVX2/AVX512 where available) and non-temporal stores.
Acceptance: Throughput beats memcpy baseline on large buffers (document environment).
Approx lines: 120

L2. “Functional-programming challenge — lambda calculus interpreter”

Prompt:
Implement a small lambda-calculus interpreter in Haskell or Lisp that supports α-conversion, β-reduction, and normal-order evaluation. Also add a type checker for simple types.

Languages: Haskell, Lisp (Scheme)
Difficulty: Medium–Hard
Constraints:

Must be purely functional; avoid mutable state.
Acceptance: Correct reductions and type check on tests.
Approx lines: 160
