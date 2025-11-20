#include <stdio.h> // - fun fact: gemini 2.5 pro instead of ".h" writed ".hh" 
#include <stdlib.h>
#include <limits.h>

#define D_ARY 4 // Using a 4-ary heap for optimization

// --- Graph Data Structures ---
// Compact representation for an edge
typedef struct {
    int to;
    int weight;
} Edge;

// Graph represented by a compact adjacency list
typedef struct {
    int num_vertices;
    int num_edges;
    Edge* edges; // Contiguous array of all edges
    int* adj;    // Index pointers into the edges array
} Graph;

// --- Priority Queue (4-ary Heap) Data Structures ---
// Node for the priority queue
typedef struct {
    int vertex;
    int dist;
} PQNode;

// Priority Queue implementation
typedef struct {
    PQNode* nodes;
    int capacity;
    int size;
} PriorityQueue;

// --- Function Prototypes ---
Graph* create_graph(int n, int m);
void add_edge(Graph* g, int from, int to, int weight, int* edge_counts);
void dijkstra(Graph* g, int start_node, long long* distances);

// Priority Queue helpers
PriorityQueue* pq_create(int capacity);
void pq_push(PriorityQueue* pq, int vertex, int dist);
PQNode pq_pop(PriorityQueue* pq);
void pq_free(PriorityQueue* pq);

// --- Main Program ---
int main() {
    // Fast I/O
    // setvbuf(stdout, NULL, _IOFBF, 1<<20);

    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);

    int* sources = (int*)malloc(k * sizeof(int));
    for (int i = 0; i < k; ++i) {
        scanf("%d", &sources[i]);
    }

    Graph* g = create_graph(n, m);
    
    // To build the compact adjacency list, we first count outgoing degrees
    int* out_degree = (int*)calloc(n, sizeof(int));
    Edge* temp_edges = (Edge*)malloc(m * sizeof(Edge));
    int* from_v = (int*)malloc(m * sizeof(int));

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        from_v[i] = u;
        temp_edges[i] = (Edge){v, w};
        out_degree[u]++;
    }

    // Set up the adjacency index array
    g->adj[0] = 0;
    for (int i = 0; i < n; ++i) {
        g->adj[i + 1] = g->adj[i] + out_degree[i];
    }

    // Populate the final edges array in sorted order of 'from' vertex
    int* current_edge_counts = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < m; ++i) {
        int from_node = from_v[i];
        int index = g->adj[from_node] + current_edge_counts[from_node];
        g->edges[index] = temp_edges[i];
        current_edge_counts[from_node]++;
    }
    
    free(out_degree);
    free(temp_edges);
    free(from_v);
    free(current_edge_counts);

    // Allocate memory for all results
    // Use long long for distances to prevent overflow on large path sums
    long long* all_distances = (long long*)malloc((long long)k * n * sizeof(long long));
    if (!all_distances) {
        perror("Failed to allocate result matrix");
        return 1;
    }

    // Run Dijkstra for each source
    for (int i = 0; i < k; ++i) {
        long long* current_distances = all_distances + (long long)i * n;
        dijkstra(g, sources[i], current_distances);
    }

    // Print results (optional, for verification)
    /*
    for (int i = 0; i < k; ++i) {
        printf("Distances from source %d:\n", sources[i]);
        for (int j = 0; j < n; ++j) {
            long long dist = all_distances[(long long)i * n + j];
            if (dist == LLONG_MAX) {
                printf("  %d: INF\n", j);
            } else {
                printf("  %d: %lld\n", j, dist);
            }
        }
    }
    */
    
    // Cleanup
    free(sources);
    free(g->edges);
    free(g->adj);
    free(g);
    free(all_distances);

    return 0;
}

// --- Graph Functions ---
Graph* create_graph(int n, int m) {
    Graph* g = (Graph*)malloc(sizeof(Graph));
    g->num_vertices = n;
    g->num_edges = m;
    g->edges = (Edge*)malloc(m * sizeof(Edge));
    g->adj = (int*)malloc((n + 1) * sizeof(int));
    return g;
}

// --- Dijkstra's Algorithm ---
void dijkstra(Graph* g, int start_node, long long* distances) {
    for (int i = 0; i < g->num_vertices; ++i) {
        distances[i] = LLONG_MAX;
    }
    distances[start_node] = 0;

    PriorityQueue* pq = pq_create(g->num_edges);
    pq_push(pq, start_node, 0);

    while (pq->size > 0) {
        PQNode top = pq_pop(pq);
        int u = top.vertex;
        int d = top.dist;

        // Lazy deletion: if we found a better path already, skip
        if (d > distances[u]) {
            continue;
        }

        // Relax edges
        for (int i = g->adj[u]; i < g->adj[u + 1]; ++i) {
            Edge* edge = &g->edges[i];
            int v = edge->to;
            int weight = edge->weight;

            if (distances[u] != LLONG_MAX && (long long)distances[u] + weight < distances[v]) {
                distances[v] = (long long)distances[u] + weight;
                // Note: We use an int for the PQ distance to save memory,
                // assuming intermediate paths fit. Final distances are long long.
                pq_push(pq, v, distances[v]);
            }
        }
    }

    pq_free(pq);
}

// --- Priority Queue (4-ary Heap) Functions ---
PriorityQueue* pq_create(int capacity) {
    PriorityQueue* pq = (PriorityQueue*)malloc(sizeof(PriorityQueue));
    pq->nodes = (PQNode*)malloc(capacity * sizeof(PQNode));
    pq->capacity = capacity;
    pq->size = 0;
    return pq;
}

void pq_free(PriorityQueue* pq) {
    free(pq->nodes);
    free(pq);
}

void sift_up(PQNode* nodes, int i) {
    while (i > 0) {
        int parent = (i - 1) / D_ARY;
        if (nodes[i].dist < nodes[parent].dist) {
            PQNode temp = nodes[i];
            nodes[i] = nodes[parent];
            nodes[parent] = temp;
            i = parent;
        } else {
            break;
        }
    }
}

void sift_down(PQNode* nodes, int size, int i) {
    while (1) {
        int min_child_idx = -1;
        int min_child_dist = INT_MAX;

        // Find the minimum among the D_ARY children
        for (int j = 1; j <= D_ARY; ++j) {
            int child_idx = D_ARY * i + j;
            if (child_idx >= size) break;
            if (nodes[child_idx].dist < min_child_dist) {
                min_child_dist = nodes[child_idx].dist;
                min_child_idx = child_idx;
            }
        }

        if (min_child_idx != -1 && nodes[min_child_idx].dist < nodes[i].dist) {
            PQNode temp = nodes[i];
            nodes[i] = nodes[min_child_idx];
            nodes[min_child_idx] = temp;
            i = min_child_idx;
        } else {
            break;
        }
    }
}

void pq_push(PriorityQueue* pq, int vertex, int dist) {
    // Simple push without decrease-key logic
    if (pq->size == pq->capacity) {
        // In a real contest, handle reallocation or ensure capacity is sufficient
        // For this problem, M is a safe capacity.
        return;
    }
    pq->nodes[pq->size] = (PQNode){vertex, dist};
    sift_up(pq->nodes, pq->size);
    pq->size++;
}

PQNode pq_pop(PriorityQueue* pq) {
    PQNode top = pq->nodes[0];
    pq->size--;
    if (pq->size > 0) {
        pq->nodes[0] = pq->nodes[pq->size];
        sift_down(pq->nodes, pq->size, 0);
    }
    return top;
}