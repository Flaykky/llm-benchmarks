use std::io::{self, BufRead};
use std::collections::BinaryHeap;
use std::cmp::Ordering;

// A state for the priority queue: (cost, position).
// We implement Ord manually to make BinaryHeap a min-heap.
#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    cost: u32,
    position: usize,
}

// The priority queue needs Ord. We want to pop the state with the *smallest* cost.
impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
            .then_with(|| self.position.cmp(&other.position))
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// A compact graph representation using a Compressed Sparse Row (CSR) format.
// This reduces memory overhead compared to `Vec<Vec<(usize, u32)>>`.
struct Graph {
    // `offsets[i]`..`offsets[i+1]` stores the range of edges for node `i`.
    offsets: Vec<usize>,
    // All edges are stored contiguously.
    edges: Vec<(usize, u32)>, // (destination_node, weight)
}

impl Graph {
    fn new(n: usize, edges_with_sources: &[(usize, usize, u32)]) -> Self {
        let mut adj = vec![Vec::new(); n];
        for &(u, v, w) in edges_with_sources {
            adj[u].push((v, w));
        }

        let mut offsets = vec![0; n + 1];
        let mut flat_edges = Vec::with_capacity(edges_with_sources.len());

        for i in 0..n {
            offsets[i + 1] = offsets[i] + adj[i].len();
            for &edge in &adj[i] {
                flat_edges.push(edge);
            }
        }

        Graph {
            offsets,
            edges: flat_edges,
        }
    }
    
    // Get an iterator over neighbors of a given node.
    fn neighbors(&self, u: usize) -> impl Iterator<Item = &(usize, u32)> {
        self.edges[self.offsets[u]..self.offsets[u+1]].iter()
    }
}

/// Runs Dijkstra's algorithm from a single source.
/// Reuses `dist` and `heap` allocations to avoid repeated memory churn.
fn dijkstra(
    graph: &Graph,
    source: usize,
    dist: &mut Vec<u32>,
    heap: &mut BinaryHeap<State>,
) {
    // 1. Reset reusable data structures
    dist.fill(u32::MAX);
    heap.clear();

    // 2. Initialize source
    dist[source] = 0;
    heap.push(State { cost: 0, position: source });

    // 3. Main Dijkstra loop
    while let Some(State { cost, position }) = heap.pop() {
        // Skip if we've found a better path already
        if cost > dist[position] {
            continue;
        }

        // Explore neighbors
        for &(neighbor, weight) in graph.neighbors(position) {
            let next_cost = cost.saturating_add(weight);
            if next_cost < dist[neighbor] {
                dist[neighbor] = next_cost;
                heap.push(State { cost: next_cost, position: neighbor });
            }
        }
    }
}

/// Solves the multi-source shortest path problem.
fn solve(
    n: usize,
    edges: &[(usize, usize, u32)],
    sources: &[usize],
) -> Vec<Vec<u32>> {
    let graph = Graph::new(n, edges);
    let k = sources.len();
    
    // The final result matrix, this will be our largest allocation.
    let mut all_distances = Vec::with_capacity(k);

    // --- Memory Pool Optimization ---
    // Allocate memory for Dijkstra's data structures *once* and reuse them.
    // This avoids `k` allocations and deallocations for the dist vector and heap.
    let mut reusable_dist = vec![u32::MAX; n];
    let mut reusable_heap = BinaryHeap::with_capacity(n);
    // --- End Optimization ---

    for &source in sources {
        dijkstra(
            &graph,
            source,
            &mut reusable_dist,
            &mut reusable_heap,
        );
        // Clone the result for this source into our final output matrix.
        all_distances.push(reusable_dist.clone());
    }

    all_distances
}

fn main() {
    // A mock to simulate reading input without complex parsing logic.
    // In a real scenario, this would parse from stdin.
    let n = 20_000;
    let m = 200_000;
    let k = 1_000;

    // Generate some mock data for demonstration.
    let mut edges = Vec::with_capacity(m);
    for i in 0..m {
        let u = i % n;
        let v = (i * 3 + 7) % n;
        let w = (i % 100 + 1) as u32;
        edges.push((u, v, w));
    }

    let sources: Vec<usize> = (0..k).map(|i| i * 19 % n).collect();

    // --- Core Logic ---
    let results = solve(n, &edges, &sources);
    // --- End Core Logic ---
    
    // Example output: print distance from first source to first 10 nodes.
    println!("Distances from source {}:", sources[0]);
    for i in 0..10 {
        let d = results[0][i];
        if d == u32::MAX {
            println!("  Node {}: unreachable", i);
        } else {
            println!("  Node {}: {}", i, d);
        }
    }

    // Example output: print distance from second source to first 10 nodes.
    println!("\nDistances from source {}:", sources[1]);
    for i in 0..10 {
        let d = results[1][i];
        if d == u32::MAX {
            println!("  Node {}: unreachable", i);
        } else {
            println!("  Node {}: {}", i, d);
        }
    }
}


// --- Input parsing functions (if needed for a contest environment) ---
// The following is an example of how you might parse input from stdin.
// This part is commented out to keep the focus on the algorithm.
/*
fn main_with_stdin() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let line1 = lines.next().unwrap().unwrap();
    let mut parts = line1.split_whitespace();
    let n: usize = parts.next().unwrap().parse().unwrap();
    let m: usize = parts.next().unwrap().parse().unwrap();
    let k: usize = parts.next().unwrap().parse().unwrap();
    
    let sources_line = lines.next().unwrap().unwrap();
    let sources: Vec<usize> = sources_line.split_whitespace()
        .map(|s| s.parse::<usize>().unwrap() - 1) // Assuming 1-indexed input
        .collect();

    let mut edges = Vec::with_capacity(m);
    for _ in 0..m {
        let line = lines.next().unwrap().unwrap();
        let mut parts = line.split_whitespace();
        let u: usize = parts.next().unwrap().parse().unwrap() - 1; // 1-indexed
        let v: usize = parts.next().unwrap().parse().unwrap() - 1; // 1-indexed
        let w: u32 = parts.next().unwrap().parse().unwrap();
        edges.push((u, v, w));
    }

    let results = solve(n, &edges, &sources);

    // Print all results as required.
    for i in 0..k {
        for j in 0..n {
            let dist = results[i][j];
            if dist == u32::MAX {
                print!("-1 ");
            } else {
                print!("{} ", dist);
            }
        }
        println!();
    }
}
*/
