// solution.c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdint.h>

// --- Configuration and Constants ---
#define MAX_N 20000
#define MAX_M 200000
#define MAX_K 1000
#define MEMORY_POOL_SIZE (140 * 1024 * 1024) // ~140 MB for pool

// --- Data Structures ---

// Edge representation for adjacency list
typedef struct Edge {
    int to;
    int weight;
    struct Edge* next;
} Edge;

// Graph structure
Edge* adj[MAX_N];
int num_vertices, num_edges;

// Memory Pool
static char memory_pool[MEMORY_POOL_SIZE];
static size_t pool_offset = 0;

// Custom allocator
void* my_malloc(size_t size) {
    // Align to 8 bytes
    size = (size + 7) & ~7;
    if (pool_offset + size > MEMORY_POOL_SIZE) {
        fprintf(stderr, "Error: Memory pool exhausted.\n");
        exit(EXIT_FAILURE);
    }
    void* ptr = memory_pool + pool_offset;
    pool_offset += size;
    return ptr;
}

// --- Priority Queue (Min-Heap) for Dijkstra ---
#define PQ_SIZE (MAX_N + MAX_M) // Upper bound for lazy deletion

typedef struct {
    int vertex;
    long long distance;
} PQNode;

static PQNode pq[PQ_SIZE];
static int pq_size;

void pq_push(int v, long long d) {
    PQNode node = {v, d};
    pq[pq_size] = node;
    int i = pq_size++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (pq[parent].distance <= pq[i].distance) break;
        PQNode temp = pq[i]; pq[i] = pq[parent]; pq[parent] = temp;
        i = parent;
    }
}

PQNode pq_pop() {
    PQNode result = pq[0];
    pq[0] = pq[--pq_size];
    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;
        if (left < pq_size && pq[left].distance < pq[smallest].distance)
            smallest = left;
        if (right < pq_size && pq[right].distance < pq[smallest].distance)
            smallest = right;
        if (smallest == i) break;
        PQNode temp = pq[i]; pq[i] = pq[smallest]; pq[smallest] = temp;
        i = smallest;
    }
    return result;
}

int pq_empty() {
    return pq_size == 0;
}

// --- Core Algorithm ---

long long dist[MAX_N];
char visited[MAX_N];

void dijkstra(int source, long long* results) {
    for (int i = 0; i < num_vertices; i++) {
        dist[i] = LLONG_MAX;
        visited[i] = 0;
    }
    dist[source] = 0;
    pq_size = 0;
    pq_push(source, 0);

    while (!pq_empty()) {
        PQNode current = pq_pop();
        int u = current.vertex;
        long long d = current.distance;

        if (visited[u]) continue;
        visited[u] = 1;

        for (Edge* e = adj[u]; e != NULL; e = e->next) {
            int v = e->to;
            long long alt = d + e->weight;
            if (alt < dist[v]) {
                dist[v] = alt;
                pq_push(v, alt);
            }
        }
    }

    for (int i = 0; i < num_vertices; i++) {
        results[i] = dist[i];
    }
}

// --- Main Function ---
int main() {
    // --- Input Reading ---
    if (scanf("%d %d", &num_vertices, &num_edges) != 2) {
        fprintf(stderr, "Error reading N and M.\n");
        return EXIT_FAILURE;
    }

    if (num_vertices > MAX_N || num_edges > MAX_M) {
        fprintf(stderr, "Graph size exceeds limits.\n");
        return EXIT_FAILURE;
    }

    // Initialize adjacency list
    for (int i = 0; i < num_vertices; i++) {
        adj[i] = NULL;
    }

    // Read edges
    for (int i = 0; i < num_edges; i++) {
        int u, v, w;
        if (scanf("%d %d %d", &u, &v, &w) != 3) {
            fprintf(stderr, "Error reading edge %d.\n", i);
            return EXIT_FAILURE;
        }
        u--; v--; // Convert to 0-based indexing
        Edge* e = (Edge*)my_malloc(sizeof(Edge));
        e->to = v;
        e->weight = w;
        e->next = adj[u];
        adj[u] = e;
    }

    int k;
    if (scanf("%d", &k) != 1 || k > MAX_K) {
        fprintf(stderr, "Error reading K or K exceeds limit.\n");
        return EXIT_FAILURE;
    }

    int sources[MAX_K];
    for (int i = 0; i < k; i++) {
        if (scanf("%d", &sources[i]) != 1) {
            fprintf(stderr, "Error reading source %d.\n", i);
            return EXIT_FAILURE;
        }
        sources[i]--; // Convert to 0-based indexing
    }

    // --- Computation ---
    long long results_buffer[MAX_N]; // Reused for each source

    for (int i = 0; i < k; i++) {
        int src = sources[i];
        dijkstra(src, results_buffer);

        // --- Output for this source ---
        for (int j = 0; j < num_vertices; j++) {
            if (results_buffer[j] == LLONG_MAX) {
                printf("INF");
            } else {
                printf("%lld", results_buffer[j]);
            }
            if (j < num_vertices - 1) printf(" ");
        }
        printf("\n");
    }

    return 0;
}