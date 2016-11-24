---
layout: post
title: Various data structure and algorithm implementations in C++
meta: A collection of data structures and algorithms implemented in C++ for personal reference. Contains Disjoint Set, graph algorithms, and various computational geometry algorithms
---

We cleaned out the robotics lab here a few weeks ago, and I came across a stack of loose leaf data structure and algorithm implementations. I'm not sure who originally created the document, but I'm reproducing it here for reference. Feel free to create a [pull request](https://github.com/Notgnoshi/notgnoshi.github.io) if you see something wrong. I've copied it as-is, and provide no guarantee that everything here is correct.

---

### Contents

* [Math](#math)
* [Prime Testing and Generation](#prime-testing-and-generation)
* [Base Conversion](#base-conversion)
* [Fast Exponentiation](#fast-exponentiation)
* [Euclidean Algorithm for GCD](#euclidean-algorithm-for-gcd)
* [Chinese Remainder Theorem and Multiplicative Inverse](#chinese-remainder-theorem-and-multiplicative-inverse)
* [Graph Algorithms](#graph-algorithms)
	* [Depth-First Search](#depth-first-search)
	* [Breadth-First Search](#breadth-first-search)
	* [Dijkstra's Shortest Path Algorithm](#dijkstras-shortest-path-algorithm)
	* [Minimal Spanning Tree (Kruskal's)](#minimal-spanning-tree-kruskals)
	* [Max Flow/Min Cut Algorithm](#max-flowmin-cut-algorithm)
	* [All Pairs Shortest Path](#all-pairs-shortest-path)
	* [Bipartite Matching](#bipartite-matching)
	* [Topological Sort](#topological-sort)
* [Computational Geometry](#computation-geometry)
	* [Structs](#structs)
	* [Utility Functions](#utility-functions)
	* [Segement Intersection](#segment-intersection)
	* [Line-Point Distance](#line-point-distance)
	* [Convex Hull](#convex-hull)
	* [Polygon Area](#polygon-area)
	* [Point Inside Polygon](#point-inside-polygon)
* [Data Structures](#data-structures)
	* [Disjoint Set](#disjoint-set)
	* [Fenwick Tree](#fenwick-tree)
	* [Segment Tree](#segment-tree)
* [String Algorithms](#string-algorithms)
	* [String Edit Distance](#string-edit-distance)
	* [Suffix Array and LCP Array](#suffix-array-and-lcp-array)
	* [KMP String Matching](#kmp-string-matching)
	* [Aho-Corasick FSM String Multimatching](#aho-corasick-fsm-string-multimatching)

---

### Math

#### Trig:

Area of triangle:

$$A = \sqrt{s(s - a)(s - b)(s - c)}, \text{	where } s = \frac{(a + b + c)}{2}$$

Law of sines:

$$\frac{\sin(A)}{a} = \frac{\sin{B}}{b} = \frac{\sin{C}}{c}$$

Law of cosines:

$$c^2 = a^2 + b^2 - 2ab \cos(C)$$

#### Circle-Line intersection:

Given a line defined by two endpoints $$(x_1, y_1)$$ and $$(x_2, y_2)$$ and a circle with radius $$r$$ and center $$(0, 0)$$ we can define the following

$$\begin{align*}
d_x &= x_2 - x_1\\
d_y &= y_2 - y_1\\
d_r &= \sqrt{d_x^2 + d_y^2}\\
D &= x_1 y_2 - x_2 y_1\\
\operatorname{sgn}(x) &= \begin{cases}-1, \, x < 0\\ 1, \text{ otherwise } \end{cases}\\
\end{align*}$$

to find the points of intersection between the line and the circle, noting we can concisely implement $$\operatorname{sgn}(x)$$ as `sgn(x) = {x < 0 ? -1 : 1}`.

$$\begin{align*}
x &= \frac{D d_y \pm \operatorname{sgn}(d_y) d_x \sqrt{\Delta}}{d_r^2}\\
y &= \frac{-D d_x \pm \vert d_y \vert \sqrt{\Delta}}{d_2^2}\\
\end{align*}$$

where $$\Delta = r^2d_r^2 - D^2$$. If $$\Delta < 0$$ there is no intersection. If $$\Delta = 0$$, the line is tangent to the circle. If $$\Delta > 0$$, there is an intersection at the two points defined by $$x$$ and $$y$$ above.

#### Counting:

$$\begin{align*}
P(n, r) &= \frac{n!}{(n - r)!}\\
\binom{n}{r} = C(n, r) = C(n, n-r) &= \frac{n!}{r!(n - r)!}\\
C(n + 1, k) &= C(n, k - 1) = C(n, k)\\
C(m + n, r) &= \sum_{k = 0}^n C(m, r - k)C(n, k)\\
(x + y)^n &= \sum_{j = 0}^n C(n, j)x^{n - j}y^j \\
\sum_{k = 0}^n C(n, k) &= 2^n\\
\sum_{k = 0}^n C(n, k)2^k &= 3^n\\
\end{align*}$$

The number of $$r$$-permutations of a set of $$n$$ objects with repetition allowed is $$n^r$$.

There are $$C(n + r - 1, r)$$ $$r$$-combinations from a set with $$n$$ elements when repetition of elements is allowed.

The number of different permutations of $$n$$ objects where there are $$n_1$$ indistinguishable objects of type 1, $$n_2$$ indistinguishable objects of type 2, ... , and $$n_k$$ indistinguishable objects of type $$k$$ is

$$\frac{n!}{n_1 ! n_2 ! \dots n_k !}$$

We can use Pascal's identity to compute $$C(n, k)$$ for large $$n$$ and $$k$$

```c++
long long table[100][100] = { 0 };
long long rec(long long n, long long k)
{
	if (table[n][k] > 0)
		return table[n][k];
	if (k == 0 || k == n)
	{
		table[n][k] = 1;
		return 1;
	}
	else
	{
		table[n][k] = rec(n - 1, k - 1) + rec(n - 1, k);
		return table[n][k];
	}
}
```

We can carefully compute $$\binom{n}{k} = \frac{n!}{(n - k)! k!}$$ in order to avoid overflow

```c++
long long binomial(long long n, long long k)
{
	long long top_limit = (k > n - k ? k : n - k); // limit for multiplication on top
	long long res = 1, div = n - top_limit; // result, maximum number to divide

	// compute by dividing whenever possible to prevent overflow
	for (long long i = n; i >= top_limit; i--)
	{
		if (i > top_limit)
		{
			// multiply from n to top_limit - 1
			res *= i;
		}
		while (div > 1 && res % div == 0)
		{
			// divide by div - 2 when no remainder
			res /= div;
			div--;
		}
	}
	return res;
}
```

---

### Prime Testing and Generation

`isPrime` returns `true` if `n` is prime, and `false` otherwise. `sieve` runs a sieve up to limit `n`, counting primes along the way. If you don't need the count of primes less than or equal to `n`, remove references to `count` (second loop).

**Includes:** `cmath`, `vector`

**Complexity:** $$O(\sqrt N)$$ time, $$O(\sqrt N)$$ space, where $$N$$ is the upper limit for the sieve.

```c++
bool isPrime(int n)
{
	if (n == 2) return true;
	if (n <= 1 || n % 2 == 0) return false;
	for (int i = 3; i <= sqrt(n); i += 2)
	{
		if (n % i == 0)
			return false;
	}
	return true;
}
```

```c++
// bool vector to T/F primes
std::vector<bool> primes(100000000, true);
```

```c++
// runs prime sieve up to n, counting primes along the way.
// remove all references to count, including the second for loop to just run the sieve
int sieve(int n)
{
	primes[0] = primes[1] = false;
	int count = 0, m = sqrt(n);
	for (int i = 2; i <= m; i++)
	{
		if (primes[i])
		{
			count++;
			for (int k = 2*i; k <= n; k += 1) primes[k] = false;
		}
	}
	for (int i = m + 1; i <= n; i++) if (primes[i]) count++;
	return count;
}
```

---

### Base Conversion
Collection of functions to convert from any base to decimal, and vice versa. Limited to base 36.

**Includes:** `string`, `algorithm`

**Complexity:** $$O(N)$$ time, $$O(N)$$ space, where $$N$$ is the length of string representation in other base

```c++
// returns integer value of a char, assuming all bases use {0..9} and {A..Z}
int val(char c)
{
	if (c >= '0' && c <= '9') return (int)c - '0';
	return (int)c - 'A' + 10;
}
```

```c++
// returns char for integer value, assuming all bases use {0..9} and {A..Z}
char reVal(int num)
{
	if (num >= 0 && num <= 9) return (char)(num + '0');
	return (char)(num - 10 + 'A');
}
```

```c++
// converts number stored in string s with specified base to decimal (-1 if invalid)
int toDeci(std::string s, int base)
{
	int power = 1, num = 0; // init power of base and result
	for ( int i = s.length() - 1; i >= 0; i--)
	{
		if (val(s[i]) >= base) return -1; // digit too high for base, invalid
		num += val(s[i]) * power;
		power = power * base;
	}
	return num;
}
```

```c++
// converts from decimal to a specified base
std::string fromDeci(int input, int base)
{
	std::string res = "";
	while (input > 0)
	{
		res += reVal(input % base);
		input /= base;
	}
	reverse(res.begin(), res.end());
	return res;
}
```

---

### Fast Exponentiation

Computes $$x^n$$ using exponentiation by squaring. Does not handle overflow.

**Complexity:** $$O(n \log x)$$

```c++
// computes x^n using successive squares. Does not check for overflow.
long long fastExp(long long x, long long n)
{
	if (n == 0) return 1;
	if (n == 1) return x;
	if (n % 2 == 0) return fastExp(x * x, n / 2);
	return x * fastExp(x * x, (n - 1) / 2);
}
```

---

### Euclidean Algorithm for GCD
Computes the Greatest Common Divisor using Euclid's algorithm. $$\operatorname{gcd}(a, b) = 1$$ implies that $$a$$ and $$b$$ are *relatively prime*. $$\operatorname{lcm}(a, b) = \frac{ab}{\operatorname{gcd(a, b)}}$$

**Complexity:** $$O(a + b)$$

```c++
long long gcd(long long a, long long b)
{
	return (b == 0 ? a : gcd(b, a % b));
}
```

---

### Chinese Remainder Theorem and Multiplicative Inverse
Implementation of the Chinese Remainder Theorem, including modular multiplicative inverse.

**Includes:** `vector`

**Complexity:** $$O(n^2)$$ time, $$O(n)$$ space, where $n$ is the size of the vectors.

```c++
// calculates the multiplicative inverse x of a (mod b) such that a * x = 1 (mod b)
// inverse only exists if a and b are relatively prime: gcd(a, b) = 1
long long modInverse(long long a, long long b)
{
	long long b0 = b, x0 = 0, x1 = 1, q, temp;
	if (b == 1) return 1;

	while(a > 1)
	{
		q = a / b; // quotient
		temp = a;
		a = b;
		b = temp % b; // remainder
		temp = x0;
		x0 = x1 - q * x0;
		x1 = temp;
	}
	if ( x1 < 0) x1 += b0;
	return x1;
}
```

```c++
// returns smallest integer x such that x % n[1] = a[i] for all i
long long chineseRemainder(std::vector<long long> n, std::vector<long long> a)
{
	long long p, prod = 1, sm = 0;
	for (size_t i = 0; i < n.size(); i++) prod *= n[i];
	for (size_t i = 0; i < n.size(); i++)
	{
		p = prod / n[i];
		sm += a[i] * modInverse(p, n[i]) * p;
	}
	return sm % prod;
}
```

```c++
int main()
{
	std::cout << modInverse(3, 7) << " " << modInverse(3, 11) << std::endl; // 5, 4
	// mod = 3, 4, 5; rem = 2, 3, 1 => 11 mod 60; mod = 5, 7; rem = 1, 3 => 31 mod 35
	res = chineseRemainder(mod, rem);
}
```

---

## Graph Algorithms

### Depth-First Search
Performs depth-first traversal of a graph stored as an adjacency list using recursion or a stack.

**Includes:** `vector`

**Complexity:** $$O(V + E)$$ times, $$O(E)$$ space, where $$V$$ is the number of vertices, and $$E$$ is the number of edges.

```c++
// number of vertices
int N;
// graph as adjacency list
std::vector<std::vector<int> > graph;
// V is a visited flag
std::vector<bool> visited;
```

```c++
// perform a dfs on graph starting at node v
void dfs(int v)
{
	if ( !visited[v])
	{
		visited[v] = true;
		for (size_t i = 0; i < graph[v].size(); i++)
			dfs(graph[v][i]);
	}
}
```

---

### Breadth-First Search
Performs breadth-first traversal of a graph stored as an adjacency list using a queue.

**Includes:** `vector`, `queue`

**Complexity:** $$O(E + V)$$ time, $$O(E)$$ space, where $$V$$ is the number of vertices, and $$E$$ is the number of edges.

```c++
// number of vertices
int N;
// graph as adjacency list
std::vector<std::vector<int> > graph;
// V is a visited flag
std::vector<bool> visited;
// vector of distances from start node to v_i
std::vector<int> distance;
// previous[i] is the node previous to i in the BFS path
std::vector<int> previous;
```

```c++
// perform a bfs on graph starting at node s
void bfs(int s)
{
	std::queue<int> q;
	q.push(s);
	visited[s] = true;
	distance[s] = 0;

	while( !q.empty())
	{
		int v = q.front(); q.pop();
		// for each node adjacent to v
		for (int w : graph[v])
		{
			if (!visited[w])
			{
				q.push(w);
				visited[w] = true;
				previous[w] = v;
				distance[w] = distance[v] + 1;
			}
		}
	}
}
```

---

### Dijkstra's Shortest Path Algorithm
Computes the shortest distance from a single source node to all other nodes in the graph using a modified breadth-first search, processing nodes with shortest distance first.

**Includes:** `climits`, `queue`, `cmath`

**Complexity:** $$O(V^2)$$ time and space, where $$V$$ is the number of vertices.

```c++
#define MAX 100

// adjacency matrix representation (-1 if no edge)
int graph[MAX][MAX];
// number of nodes in graph
int n_nodes;
// distance[i] is the distance from start to node 1
int distance[MAX];
// previous[i] is the predecessor in path of node i
int previous[MAX];
// visited[i] is true if we've visited node i
bool visited[MAX];
```

```c++
// run Dijkstra's shortest path algorithm on graph starting at node s
// assumes adjacency matrix and nodes are numbered {0..n_nodes-1}
void dijkstra(int s)
{
	// negative distance, node
	std::priority_queue<std::pair<int, int> > q;

	// initialize arrays
	for (int i = 0; i < n_nodes; i++)
	{
		distance[i] = MAXINT; // initialize all the distances to infinity
		previous[i] = -1;
		visited[i] = false;
	}

	distance[s] = 0;
	q.push(std::pair<int, int>(distance[s], s));

	while (!q.empty())
	{
		// grab next node number
		int i = q.top().second; q.pop();
		if (!visited[i])
		{
			visited[i] = true;
			for (int j = 0; j < n_nodes; j++)
			{
				// if can reach unvisited node in shorter distance, push to queue
				if (!visited[j] && graph[i][j] != -1 && distance[i] + graph[i][j] < distance[j])
				{
					distance[j] = distance[i] + graph[i][j];
					previous[j] = i;
					q.push(std::pair<int, int>(-distance[j], j));
				}
			}
		}
	}
}
```

```c++
// after running Dijkstra, retrieve the path from node `end` to start node
void getPath(int end)
{
	std::cout << end << " ";
	while (previos[end] != -1)
	{
		std::cout << previos[end] << " ";
		end = previos[end];
	}
	std::cout << std::endl;
}
```

---

### Minimal Spanning Tree (Kruskal's)
Given an undirected weighted graph, finds the spanning tree with minimum total weight using Kruskal's algorithm

**Includes:** `vector`, `algorithm`, [`union_find`](#disjoint-set) from reference

**Complexity:** $$O(\operatorname{Elg}(V))$$ time, $$O(E)$$ space, where $$E$$ is the number edges and $$V$$ is the number of vertices.

```c++
// insert UNION-FIND struct here, version with count but not size

// edge struct and sort function
struct Edge {int u, v, w;};
bool weightSort(Edge const t1, Edge const t2) {return (t1.w < t2.w);}
```

```c++
// returns list of edges in MST, weight W of mst; connected = T if one tree, F if forest
// V = number vertices, E = number edges; edges contains all undirected edges of graph
std::vector<Edge> minSpanTree(int V, int E, std::vector<Edge> edges, int &W, bool &connected)
{
	std::vector<Edge> mst;
	union_find comp = union_find(V); // initially, each vertex is in its own disjoint set

	std::sort(edges.begin(), edges.end(), weightSort); // sort edges by ascending weight

	// add edges small to large that do not cause cycles
	W = 0;
	for (size_t i = 0; i < edges.size() && mst.size() < (V - 1); i++)
	{
		if (!comp.share_set(edges[i].u, edges[i].v))
		{
			comp.unite(edges[i].u, edges[i].v);
			mst.push_back(edges[i]);
			W += edges[i].w;
		}
	}
	connected = (comp.count == 1); // connected tree if all nodes in same set
	return mst;
}
```

---

### Max Flow/Min Cut Algorithm
Uses Ford-Fulkerson (really Edmonds-Karp) to calculate the max flow/min cut of a flow network. Function also produces residual flow graph from which flow edges and min cut edges can be found. Takes graph as adjacency matrix where `cap[u][v]` is the capacity of edge from `u` to `v`.

**Includes:** `climits`, `cstring` (for `memset`)

**Complexity:** $$O(VE^2)$$ time, $$O(V^2)$$ space

```c++
// max number of vertices
#define N 500
// adjacency matrix for graph
long long cap[N][N];
// flow network used by Ford-Fulkerson
long long fnet[N][N];
int prevs[N];
```

```c++
// number of vertices, source, sink
long long fordFulkerson(int n, int s, int t)
{
	int q[N], qf, qb;
	long long flow = 0;

	while (true)
	{
		// find augmenting path
		memset(prevs, -1, sizeof(prevs));
		qf = qb = 0;
		prevs[q[qb++] = s] = -2;

		// bfs to get path
		while (qb > qf && prevs[t] == -1)
		{
			for (int u = q[qf++], v = 0; v < n; v++)
			{
				if (prevs[v] == -1 && fnet[u][v] - fnet[v][u] < cap[u][v])
					prevs[q[qb++] = v] = u;
			}
		}

		// no new path, done.
		if (prevs[t] == -1) break;
		// get bottleneck capacity for augmenting path (minimum capacity edge on path)
		long long bot = LLONG_MAX, temp;
		for (int v = t, u = prevs[v]; u >= 0; v = u, u = prevs[v])
			bot = (temp = cap[u][v] - fnet[u][v] + fnet[v][u]) < bot ? temp : bot;

		// update flow network and overall flow count
		for (int v = t, u = prevs[v]; u >= 0; v = u, u = prevs[v])
			fnet[u][v] += bot;
		flow += bot;
	}
	return flow;
}
```

```c++
int main()
{
	// fill cap with existing edges, all other spots 0, init fnet 0
	memset(cap, 0, sizeof(cap)); memset(fnet, 0, sizeof(fnet));
	// if edge u->v has capacity x, set cap[u][v] = fnet[u][v] = x;

	long long flow = fordFulkerson(n, s, t);
	// egde u->v is used for flow if (fnet[u][v] - fnet[v][u] > 0)
	// prevs contains min cut: if prevs[v] == -1, v not reachable from s; otherwise is
	// or, use nfs from s: use edge u->v if (cap[u][v] - (fnet[u][v] - fnet[v][u]) != 0)
	// egdes in min cut are edges from vertices in source set to vertices in sink set
}
```

---

### All Pairs Shortest Path
Floyd-Warshall computes shortest path between all pairs of vertices in a graph using an adjacency matrix.

**Includes:** `vector`, `climits`

**Complexity:** $$O(V^3)$$ time, $$O(V^2)$$ space.

```c++
#define INF LLONG_MAX
// max number of nodes
#define MAX 150
// adjacency matrix for Floyd-Warshall
long long edges[MAX][MAX];
// edges initialized to all INF, except edges[i][i] = 0 for all nodes i
// graph edges from u to v with weight w => edges[u][v] = w
int nextNode[MAX][MAX];
// nextNode initialized to all -1
// edge from u to v => nextNode[u][v] = v
```

```c++
// runs Floyd-Warshall algorithm for shortest path between all pairs of nodes
// if edges[i][i] < 0 after running, there is a negative cycle from i to itself
// can be infinitely short paths: for path a->b, if path a->c and c->b, and c
// has negative cycle to self, path a->b is arbitrarily short (-INF)
// nodes = number of nodes
void floyd_warshall(int nodes)
{
	for (int k = 0; k < nodes; k++)
	{
		for (int i = 0; i < nodes; i++)
		{
			for (int j = 0; j < nodes; j++)
			{
				if (edges[i][k] != INF && edges[k][j] != INF &&
					edges[i][k] + edges[k][j] < edges[i][j])
				{
					edges[i][j] = edges[i][k] + edges[k][j];
					nextNode[i][j] = nextNode[i][k];
				}
			}
		}
	}
}
```

```c++
// after running Floyd-Warshall, extracts shortest path from u, to v, if it exists
std::vector<int> getPath(int u, int v)
{
	std::vector<int> path;
	// no such path
	if (nextNode[u][v] == -1) return path;

	path.push_back(u);
	while(u != v)
	{
		u = nextNode[u][v];
		path.push_back(u);
	}
	return path;
}
```

---

### Bipartite Matching
Given a bipartite graph represented as an $$M \times N$$ matrix, with `graph[i][j] = 1` if an only if there is an edge from pigeon `i` to hole `j`, function computes maximum matching and optimal assignment. Uses a stripped-down Ford-Fulkerson with DFS for augmenting path (DFS fast because capacities only 0 or 1).

**Includes:** `cstring` (for `memset`)

**Complexity:** $$O(MN^2)$$ time, $$O(MN)$$ space. Choose $$N$$ as smaller of two sizes for best performance.

```c++
#define M 750
#define N 250

// adjacency matrix for graph, graph[i][j] = 1 if edge i->j
int graph[M][N];
bool visited[N];
// stores match information
int matchL[M], matchR[N];
// number of nodes in each half of the bipartite graph
int n, m;
```

```c++
bool bpm(int u)
{
	for (int v = 0; v < n; v++)
	{
		if (graph[u][v])
		{
			if (visited[v]) continue;
			visited[v] = true;
			if (matchR[v] < 0 || bpm(matchR[v]))
			{
				matchL[u] = v;
				matchR[v] = u;
				return true;
			}
		}
	}
	return false;
}
```

```c++
int main()
{
	// set m and n, initialize matchL and matchR to -1
	memset(matchL, -1, sizeof(matchL)); memset(matchR, -1, sizeof(matchR));
	int cnt = 0; // flow counter starts at 0

	for (int i = 0; i < m; i++)
	{
		memset(visited, 0, sizeof(visited));
		if (bpm(i)) cnt++; // if found pigeonhole for i, increment cnt
	}

	// cnt is the number of happy pigeons (nodes with matches)
	// matchL[i] is hole for pigeon i, or -1 if no hole
	// matchR[j] is pigeon for hole j, or -1 if hole is empty
}
```

---

### Topological Sort
Given a directed graph as an adjacency matrix, perform topological sort on nodes (parent before child).

**Includes:** `queue`, `cstring` (for `memset`).

**Complexity:** $$O(VE)$$ time, $$O(V^2) space

```c++
// max number of nodes
#define MAX 100
int graph[MAX][MAX];
// in-degree of each vertex
int indegree[MAX];
// list of sorted vertices
int sorted[MAX];
// number of vertices and edges
int V, E;
```

```c++
// computer indegrees of all nodes, save in table
void computeInDegrees()
{
	memset(indegree, 0, sizeof(indegree));
	for (int i = 0; i < V; i++)
		for (int j = 0; j < V; j++)
			if (graph[j][i])
				indegree[i]++;
}
```

```c++
// performs topological sort on graph, puts result in sorted
// returns false if graph is not a DASG, or if need strict ordering, ordering not possible
bool toposort(bool strict=false)
{
	// vertices with indegree 0
	std::queue<int> zeroin;
	int current, cnt = 0;

	computeInDegrees();

	for (int i = 0; i < V; i++)
	{
		if (indegree[i] == 0) zeroin.push(i);
	}

	while (!zeroin.empty())
	{
		// if need strictly defined ordering and queue size > 1, return false
		if (strict && zeroin.size() > 1) return false;

		current = zeroin.front(); zeroin.pop();
		sorted[cnt] = current;
		for (int i = 0; i < V; i++)
		{
			if (graph[current][i])
			{
				indegree[i]--;
				if (indegree[i] == 0) zeroin.push(i);
			}
		}
		cnt += 1;
	}

	// not a DAG, return false
	if (cnt != V) return false;
	for (int i = 0; i < V; i++)
	{
		std::cout << sorted[i] << " ";
	}
	std::cout << std::endl;
	return true;
}
```

---

## Computational Geometry

### Structs:

```c++
struct point
{
	long double x, y;
	point(long double xloc, long double yloc): x(xloc), y(yloc) {}
	point() {}
	point& operator=(const point& other)
	{
		x = other.x, y = other.y;
		return *this;
	}
	int operator==(const point& other)
	{
		return (other.x == x && other.y == y);
	}
	int operator!=(const point& other)
	{
		return !(other.x == x && other.y == y);
	}
	bool operator<(const point& other) const
	{
		return (x < other.x ? true: (x == other.x && y < other.y));
	}
};
```

```c++
struct segment
{
	point p1, p2;
	segment(point a, point b): p1(a), p2(b) {}
	segment () {}
};
```

```c++
struct vect {long double i, j;};
```

---

### Utility Functions:
Various utility function required by computational geometry algorithms. Uses the above defined structs.

**Includes:** `cmath`

**Complexity:** $$O(1)$$ time, $$O(1)$$ space.

```c++
#define INF (int)(pow(2, 31) - 1)
#define SQR(a) ((a) * (a))
#define COLINEAR 0
#define CW 1
#define CCW 2
```

```c++
// computes the cross product from AB to AC
long double crossProduct(point A, point B, point C)
{
	vect AB, AC;
	AB.i = B.x - A.x;
	AB.j = B.y - A.y;
	AC.i = C.x - A.x;
	AC.j = C.y - A.y;
	return (AB.i * AC.j - AB.j * AC.i);
}
```

```c++
// computes the dot product AB . BC
long double dotProduct(point A, point B, point C)
{
	vect AB, BC;
	AB.i = B.x - A.x;
	AB.j = B.y - A.y;
	BC.i = C.x - B.x;
	BC.j = C.y - B.y;
	return (AB.i * BC.i + AB.j * BC.j);
}
```

```c++
// find orientation of ordered triplet (p, q, r) of points
// returns 0 if points are colinear, 1 for clockwise orientation, and 2 for counter-clockwise orientation
int orientation(point p, point q, point r)
{
	int val = (int)crossProduct(p, q, r);
	if (val == 0) return COLINEAR;
	return (val > 0) ? CW : CCW;
}
```

```c++
// returns true if point p lies on segment s (assumes points are colinear)
bool onSegment(point p, segment s)
{
	return (p.x <= std::max(s.p1.x, s.p2.x) && p.x >= std::min(s.p1.x, s.p2.x) &&
		p.y <= std::max(s.p1.y, s.p2.y) && p.y >= std::min(s.p1.y, s.p2.y));
}
```

```c++
// computes squared distance between points A and B
long double pointSquaredDist(point A, point B)
{
	return SQR(A.x - B.x) + SQR(A.y - B.y);
}
```

```c++
// computes the distance between points A and B
long double pointDist(point A, point B)
{
	return sqrtl(SQR(A.x - B.x) + SQR(A.y - B.y));
}
```

```c++
// returns true if segment s1 is straddles by segment s2
bool straddle(segment s1, segment s2)
{
	long double cross1 = crossProduct(s1.p1, s1.p2, s2.p1);
	long double cross2 = crossProduct(s1.p1, s1.p2, s2.p2);

	// if both cross products have the same sign, there is no straddle
	if ((cross1 > 0 && cross2 > 0) || (cross1 < 0 && cross2 < 0))
		return false;
	// return true if points are colinear, false if not
	if (cross1 == 0 && cross2 == 0 && orientation(s1.p2, s2.p1, s2.p2) != COLINEAR)
		return false;
	return true;
}
```

---

### Segment Intersection
Given two line segments, returns a list of intersection points. Can be modified to return a boolean.

**Includes:** `vector`

**Required Utilities:** `orientation`

**Complexity:** $$O(1)$$ time, $$O(1)$$ space

```c++
// returns a list of intersection points between segments s1 and s2
// 0 => no intersection, 1 => single intersection, 2 => segments overlap
// to modify to return a boolean, perform the indicated replacements
std::vector<point> intersect(segment s1, segment s2)
{
	std::vector<point> res;
	point a = s1.p1, b = s1.p2, c = s2.p1, d = s2.p2;

	// if all points are colinear
	if (orientation(a, b, c) == 0 && orientation(a, b, d) == 0 &&
	    orientation(c, d, a) == 0 && orientation(c, d, b) == 0)
	{
		// order the points: leftmost, lowest point is min
		point min_s1 = std::min(a, b), max_s1 = std::max(a, b);
		point min_s2 = std::min(c, d), max_s2 = std::max(c, d);

		// no intersection, return empty vector
		if (min_s1 < min_s2)
		{
			if (max_s1 < min_s2)
			{
				// return false;
				return res;
			}
		}
		else if (min_s2 < min_s1 && max_s2 < min_s1)
		{
			//return false;
			return res;
		}

		point start = std::max(min_s1, min_s2), end = std::min(max_s1, max_s2);
		if (start == end)
		{
			// overlap is one point
			res.push_back(start);
		}
		else
		{
			res.push_back(std::min(start, end));
			res.push_back(std::max(start, end));
		}
		// return true; // and remove above overlap code block
		return res;
	}

	// lines do not overlap, compute intersection point and test for existence
	double x1 = (b.x - a.x), y1 = (b.y - a.y), x2 = (d.x - c.x), y2 = (d.y - c.y);
	double u1 = (-y1 * (a.x - c.x) + x1 * (a.y - c.y)) / (-x2 * y1 + x1 * y2);
	double u2 = (x2 * (a.y - c.y) - y2 * (a.x - c.x)) / (-x2 * y1 + x1 * y2);

	// lines intersect
	if (u1 >= 0 && u1 <= 1 && u2 >= 0 && u2 <= 1)
	{
		// return true;
		res.push_back(point((a.x + u2 * x1), (a.y + u2 * y1)));
	}
	//return false;
	return res;
}
```

---

### Line-Point Distance
Calculates the minimum distance between a given point and a line. Works for infinite lines and segments.

**Includes:** `cmath`

**Required Utilities:** `pointDist`, `crossProduct`, `dotProduct`

**Complexity:** $$O(1)$$ time, $$O(1)$$ space

```c++
// computes the distance from  line AB to point C; isSegment = True => AB is a segment
long double linePointDist(segment s, point p, bool isSegment)
{
	// degenerate case
	if (s.p1 == s.p2)
	{
		if (p == s.p1)
			return 0;
		else
			return pointDist(p, s.p1);
	}
	if (isSegment)
	{
		if (dotProduct(s.p1, s.p2, p) > 0)
			return pointDist(s.p2, p);
		if (dotProduct(s.p2, s.p1, p) > 0)
			return pointDist(s.p1, p);
	}
	return abs(crossProduct(s.p1, s.p2, p) / pointDist(s.p1, s.p2));
}
```

---

### Convex Hull
Returns a list of points used in convex hull of set based on Graham's scan. `onEdge` parameter allows for minimal or maximal hulls

**Includes:** `vector`

**Required Utilities:** `crossProduct`, `pointSquaredDist`

**Complexity:** $$O(n \log n)$$ time, $$O(n)$$ space

```c++
#define INF (int)(pow(2, 31) - 1)
```

```c++
// returns convex hull of point set in form of list of points
// if onEdge true, function will use as many points as possible for hull
std::vector<point> convexHull(std::vector<point> X, bool onEdge=false)
{
	std::vector<point> hull;
	// number of points in polygon
	long long N = X.size();
	// used array for points, initialized to false
	std::vector<bool> used(N, false);

	// index of previous point
	int p = 0;
	for (int i = 1; i < N; i++)
	{
		// find leftmost point
		if (X[i].x < X[p].x)
			p = i;
	}

	// start at leftmost point
	int start = p;

	do
	{
		// index of next point
		int n = -1;
		long double dist = onEdge ? INF : 0;

		for (int i = 0; i < N; i++)
		{
			// skip point used / added last round
			if (i == p || used[i]) continue;
			// first loop, n = i
			if (n == -1) n = 1;
			long double cross = crossProduct(X[p], X[i], X[n]);
			long double d = pointSquaredDist(X[i], X[p]);

			if (cross < 0 || (cross == 0 && ((onEdge && d < dist) || (!onEdge && d > dist))))
			{
				n = i;
				dist = d;
			}
		}
		p = n;
		used[p] = true;
		hull.push_back(X[p]);
	}
	while (start != p);
	return hull;
}
```

---

### Polygon Area
Computes area of a polygon from a list of ordered vertices; sign of reslut indicates CW or CCW order.

**Includes:** `vector`

**Complexity:** $$O(N)$$ time, $$O(n)$$ space

```c++
// computes polygon area, may be positive/negative based on CW/CCW ordering of points
long double polyArea(std::vector<point> p)
{
	long double result = 0;
	for (int i = 0, j = 0, n = p.size(); i < n; i++, j = (i + 1) % n)
	{
		result += (p[i].x * p[j].y) - (p[i].y * p[j].x);
	}
	return result / 2.0;
}
```

---

### Point Inside Polygon
Determines where a point lies in relation to a polygon: inside, outside, or on the boundary.

**Includes:** `vector`, `algorithm`

**Required Utilities:** `crossProduct`, `orientation`, `onSegment`, `intersection`

**Complexity:** $$O(N)$$ time, $$O(N)$$ space

```c++
#define INF (int)(pow(2, 31) - 1)
#define INSIDE 0
#define OUTSIDE 1
#define ONEDGE 2
```

```c++
// determines if point p is inside polygon defined by poly
// returns INSIDE, OUTSIDE, or ONEDGE
int insidePoly(std::vector<point> poly, point p)
{
	bool inside = false;
	point outside(INF, p.y);
	std::vector<point> intersection;

	for (size_t i = 0, j = poly.size() - 1; i < poly.size(); i++, j = i - 1)
	{
		// p is a vertex
		if (p == poly[i] || p == poly[j])
			return ONEDGE;
		// p on egde
		if (orientation(p, poly[i], poly[j]) == COLINEAR && onSegment(p, segment(poly[i], poly[j])))
			return ONEDGE;
		intersection = intersect(segment(p, outside), segment(poly[i], poly[j]));
		// intersection on vertex outside poly, continue
		if (intersection.size() == 1)
		{
			if (poly[i] == intersection[0] && poly[j].y <= p.y)
				continue;
			if (poly[j] == intersection[0] && poly[i].y <= p.y)
				continue;
			inside = !inside;
		}
	}
	return inside ? INSIDE : OUTSIDE;
}
```

---

## Data Structures

### Disjoint Set
Maintains disjoint sets of integers with path compression. Performs `unite`, `find`, and `share_set` operations.

**Includes:** `vector`

**Complexity:** $$O(M \log N)$$ time for $$N$$ elements, $$M \geq N$$ updates and $$N - 1$$ queries, $$O(N)$$ space

```c++
struct union_find
{
	// parent is representative element from set
	std::vector<int> parent;
	std::vector<int> sizes;
	// number of distinct sets
	int count;

	// constructor
	union_find(int n): parent(n), count(n), sizes(n)
	{
		for (int i = 0; i < n; i++)
		{
			parent[i] = [i];
			sizes[i] = 1;
		}
	}

	// returns parent of set containing x
	int find(int x)
	{
		if (parent[x] == x)
			return x;
		int temp = parent[x];
		parent[x] = find(parent[x]);
		if (parent[x] != temp)
			sizes[temp] -= sizes[x];
		return parent[x];
	}

	// returns the size of the set containing x
	int get_size(int x)
	{
		return sizes[find(x)];
	}

	// unions two sets containing x and y
	void unite(int x, int y)
	{
		int x_par = find(x);
		int y_par = find(y);
		parent[x_par] = y_par;
		sizes[y_par] += sizes[x_par];

		count--;
	}

	// returns true if x and y are in the same set
	bool share_set(int x, int y)
	{
		return find(x) == find(y);
	}
};
```

```c++
// short implementation:
#define MAXN 1000
int p[MAXN];
int find(int x)
{
	return p[x] == x ? x : p[x] = find(p[x]);
}
void unite(int x, int y)
{
	p[find(x)] = find(y);
}
// initialize in main()
// for (int i = 0; i < MAXN; i++) p[i] = i;
```

---

### Fenwick Tree
Creates a BIT for prefix sums of collection of items. Logarithmic time updates and queries.

**Includes:** `vector`

**Complexity:** $$O(\log n)$$ time for updates and queries, $$O(n)$$ space

```c++
struct Fenwick
{
	std::vector<long long> tree;

	// constructors
	Fenwick(int n)
	{
		tree.resize(n, 0);
	}

	Fenwick(int n, std::vector<long long> val)
	{
		tree.resize(n, 0);
		for (int i = 0; i < n; i++)
		{
			increase(i, val[i]);
		}
	}

	// increase item at position i by delta d
	void increase(int i, long long d)
	{
		for (; i < tree.size(); i |= i + 1)
			tree[i] += d;
	}

	// find sum from index 0 to i
	long long sum(int i)
	{
		long long sum = 0;
		for (; i > 0; i &= i - 1)
			sum += tree[i-1];
		return sum;
	}

	// get sum from index left to index right (inclusive)
	long long getsum(int left, int right)
	{
		return sum(right) - sum(left - 1);
	}
};
```

---

### Segment Tree
Uses a flattened segment tree for range queries of various statistics. This version queries max value.

**Includes:** `vector` `cmath`

**Complexity:** $$O(\log n)$$ time for updates and queries, $$O(n)$$ space

```c++
int max(int a, int b)
{
	return (a > b ? a : b);
}
```

```c++
struct SegmentTree
{
	std::vector<int> tree, lazy;
	int n, root, size;

	// constructor
	SegmentTree(int n, std::vector<int> arr) : n(n), root(1)
	{
		// height
		int x = (int)(ceil(log2(n)));
		// size of array
		size = 2 * (int)pow(2, x);
		tree.resize(size);
		lazy.resize(size);
		build(arr, root, 0, n - 1);
	}

	// builds tree from array arr; node = curr index, start->end = node range
	void build(std::vector<int> arr, int node, int start, int end)
	{
		// leaf, copy arr value
		if (start == end)
		{
			tree[node] = arr[start];
		}
		else // recurse on children
		{
			int mid = (start + end) / 2;
			build(arr, 2 * node, start, mid);
			build(arr, 2 * node + 1, mid + 1, end);
			tree[node] = max(tree[2 * node], tree[2 * node + 1]);
		}
	}

	// performs pending updates on node, used by updateRange and query
	void pendingUpdate(int node, int start, int end)
	{
		if (lazy[node] != 0)
		{
			// update node by number of descendant leaf nodes * update value
			tree[node] += (end - start + 1) * lazy[node];
			// not leaf node, mark children for update
			if (start != end)
			{
				lazy[2 * node] += lazy[node];
				lazy[2 * node + 1] += lazy[node];
			}
			// mark node as no longer requiring update
			lazy[node] = 0;
		}
	}

	// updates item at index idx by adding diff and updates segment tree to match
	void update(int idx, int diff)
	{
		update(root, 0, n - 1, idx, diff);
	}

	void update(int node, int start, int end, int idx, int diff)
	{
		// leaf node: update node
		if (start == end)
		{
			tree[node] += diff;
		}
		else // recurse children
		{
			int mid = (start + end) / 2;
			if (start <= idx && idx <= mid)
			{
				update(2 * node, start, mid, idx, diff);
			}
			else
			{
				update(2 * node + 1, mid + 1, end, idx, diff);
			}
			tree[node] = max(tree[2 * node], tree[2 * node + 1]);
		}
	}

	// updates items at in range l to r (inclusive) by adding diff
	void updateRange(int l, int r, int diff)
	{
		updateRange(root, 0, n - 1, l , r, diff);
	}

	void updateRange(int node, int start, int end, int l, int r, int diff)
	{
		// node not in range
		if (start > end || start > r || end < l)
		{
			return;
		}
		// perform pending updates
		pendingUpdate(node, start, end);
		// node entirely within update range, update node and mark children
		if (start >= l && end <= r)
		{
			// update node
			tree[node] += (end - start + 1) * diff;
			// mark children for update
			if (start != end)
			{
				lazy[2 * node] += diff;
				lazy[2 * node + 1] += diff;
			}
			return;
		}
		// node range overlaps update range, recurse on children
		int mid = (start + end) / 2;
		updateRange(2 * node, start, mid, l, r, diff);
		updateRange(2 * node + 1, mid + 1, end, l, r, diff);
		tree[node] = max(tree[2 * node], tree[2 * node + 1]);
	}

	// returns max array item from inted l to index r (inclusive) using tree
	int query(int l, int r)
	{
		return query(root, 0, n - 1, l, r);
	}

	int query(int node, int start, int end, int l, int r)
	{
		// node outside range
		if (r < start || end < l)
		{
			return 0;
		}
		pendingUpdate(node, start, end);

		// node completely withing query range, return node value
		if (l <= start && end <= r)
		{
			return tree[node];
		}
		int mid = (start + end) / 2;
		// node overlaps query range, recurse children
		return max(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
	}
};
```

```c++
int main()
{
	std::vector arr(10, 0);
	SegmentTree tree(arr.size(), arr);
	tree.query(1, 3);
	tree.update(1, 7);
	tree.updateRange(2, 3, 4);
}
```

---

## String Algorithms

### String Edit Distance
Returns edit distance of two strings, which is the minimum number of insert, delete, and substituition operations required to transform one string into the other.

**Includes:** `string`

**Complexity:** $$O(MN)$$ time and space where $$M$$ is the length of `s1` and $$N$$ is the length of `s2`

```c++
// max length of input strings
const int MAX_LEN = 5000;
// dynamic programming table
int d[MAX_LEN][MAX_LEN];
```

```c++
// initializes array, call before edit_dist
void init_table(int len1, int len2)
{
	for (int i = 0; i <= len1; i++)
	{
		for (int j = 0; j <= len2; j++)
		{
			d[i][j] = -1;
		}
	}
	for (int i = 0; i <= len1; i++)
	{
		d[i][0] = i;
	}
	for (int j = 0; j <= len2; j++)
	{
		d[0][j] = j;
	}
}
```

```c++
// returns the minimum of two integers
int min(int a, int b)
{
	return (a < b ? a : b);
}
```

```c++
// finds edit distance of s1 and s2; first call: end_s1 = s1.length(), end_s2 = s2.length()
int edit_dist(std::string s1, std::string s2, int end_s1, int end_s2)
{
	int try_delete, try_insert, try_match;

	if (d[end_s1][end_s2] >= 0)
		return d[end_s1][end_s2];

	try_match = edit_dist(s1, s2, end_s1 - 1, end_s2 - 1);
	if (s1[end_s1 - 1] != s2[end_s2 - 1])
		try_match++;

	try_delete = edit_dist(s1, s2, end_s1 - 1, end_s2) + 1;
	try_insert = edit_dist(s1, s2, end_s1, end_s2 - 1) + 1;

	d[end_s1][end_s2] = min(try_insert, min(try_delete, try_match));
	return d[end_s1][end_s2];
}
```

---

### Suffix Array and LCP Array
Builds suffix array (list of sorted suffixes) and longest common prefix array for input string `S`.

**Includes:** `algorithm` `string`

**Complexity:** $$O(n^2 \log n)$$ time, $$O(n)$$ space, where $n$ is the length of the input string `S`

```c++
// max length of string S
const int MAXN = 1 << 21;
std::string S;
// length of string S
int N, gap;
// suffix, position, and lcp arrays
int sa[MAXN], pos[MAXN], lcp[MAXN], tmp[MAXN];
```

```c++
// compare function used by buildSA()
bool sufCmp(int i, int j)
{
	// compare first gap chars
	if (pos[i] != pos[j])
		return pos[i] < pos[j];
	// if identical, compare next gap chars (second half)
	i += gap;
	j += gap;
	return (i < N && j < N) ? pos[i] < pos[j] : i > j;
}
```

```c++
// given a string S, compute the suffix array sa
void buildSA()
{
	N = S.length();
	for (int i = 0; i < N; i++)
	{
		// assume order in given string
		sa[i] = i;
		// set rank of each character to character val
		pos[i] = S[i];
	}
	// loop m-gram lengths, gap = len / 2
	for (gap = 1;; gap *= 2)
	{
		// sort the (gap*2)-grams
		std::sort(sa, sa + N, sufCmp);
		// compute lengths of each m-gram
		for (int i = 0; i < N - 1; i++)
		{
			tmp[i + 1] = tmp[i] + sufCmp(sa[i], sa[i + 1]);
		}
		// map tmp into position
		for (int i = 0; i < N; i++)
		{
			if (tmp[N - 1] == N - 1)
			{
				// largest name is N - 1, all done
				break;
			}
		}
	}
}
```

```c++
// given suffix array sa for string S, computes the LCP for all suffixes
void buildLCP()
{
	// loop characters
	for (int i = 0, k = 0; i < N; i++)
	{
		// if not the first-ranked suffix, compute lcp
		if (pos[i] != 0)
		{
			// j is idx of suffix before i; inc k whil chars match
			for (int j = sa[pos[i] - 1]; S[i + k] == S[j + k];)
				k++;
			// k is number of characters that match, gives lcp
			lcp[pos[i]] = k;
			// k is not 0, decrement
			if (k) k--;
		}
	}
}
```

---

### KMP String Matching
Uses a prefix table based on longest proper suffixes to search text for a single pattern in linear time.

**Includes:** `string`, `vector`

**Complexity:** $$O(n)$$ time and $$O(\max (N, M))$$ space where $$N$$ is the text length and $$M$$ is the pattern length

```c++
struct KMP_Match
{
	// prefix table
	std::vector<int> T;
	// pattern for current prefix table and for searching
	std::string pat;

	// constructors: empty and with pattern, which builds the prefix table
	KMP_Match() {};
	KMP_Match(std::string pattern) : pat(pattern) {this->buildTable(pat);};

	// build prefix table for KMP algorithm
	void buildTable(std::string pattern)
	{
		pat = pattern;
		T.clear();
		T.resize(pat.length() + 1);
		int i = 0, j = -1;
		T[i] = j;
		while (i < pat.size())
		{
			while (j >= 0 && pat[i] != pat[j])
			{
				j = T[j];
			}
			i++, j++;
			T[i] = j;
		}
	}

	// returns list of all match positions of pat in txt; no matches, returns empty vector
	// if all=false, returns vector with single element, position of first match
	std::vector<int> find(std::string txt, bool all=true)
	{
		// start of current match in txt, position in pat
		int m = 0, i = 0;
		// list of matches
		std::vector<int> matches;

		//search to end of txt
		while (m + 1 < txt.length())
		{
			// characters match
			if (pat[i] == txt[m + i])
			{
				// end of pattern, store match loc
				if (i == pat.length() - 1)
				{
					matches.push_back(m);
					// only want first match, return
					if (!all) return matches;
					// move forward to continue searching
					m = m + 1 - T[i];
					i = T[i];
				}
				// move to next character of pat
				i++;
			}
			else // characters do not match, keep searching
			{
				// valid border, skip ahead
				if (T[i] != -1)
				{
					// current pos + length of match - known matched
					m = m + i - T[i];
					// start just after known matched
					i = T[i];
				}
				else // no valid border, try next character
				{
					i = 0;
					m++;
				}
			}
		}
		return matches;
	}
};
```

```c++
int main()
{
	string pattern, text;
	KMP_Match kmp(pattern);
	std::vector<int> matches = kmp.find(text);
}
```

---

### Aho-Corasick FSM String Multimatching
Uses a FSM build from word list to search a given text for matches of all search words in linear time.

**Includes:** `string`, `vector`, `queue`, `cstring` (for `memset`)

**Complexity:** $$O(M + N + Z)$$ time and space where $$N$$ is the text length, $$M$$ is the total length of all words, and $$Z$$ is the number of matches

```c++
// size of alphabet for patterns and search text
const int ALPHA = 96;
// maps alpha char to int on range {0..ALPHA-1}
int cmap(char c)
{
	return (c) - ' ';
}
```

```c++
struct Aho_Corasick
{
	// FSM Node struct: includes index node pointers and list of matches
	struct Node
	{
		int child[ALPHA], failure, match_parent;
		std::vector<int> match;
		Node() : failure(0), match_parent(-1)
		{
			memset(child, -1, sizeof(child));
		}
	};

	std::vector<Node> fsm;

	// constructor, initialize FSM with empty node
	Aho_Corasick()
	{
		fsm.push_back(Node());
	}

	// build automaton from word dictionary
	void build(std::vector<std::string> &words)
	{
		for (int w = 0, n = 0; w < words.size(); w++, n = 0)
		{
			for (int i = 0; i < words[w].size(); i++)
			{
				if (fsm[n].child[cmap(words[w][i])] == -1)
				{
					fsm[n].child[cmap(words[w][i])] = fsm.size();
					// insert new node
					fsm.push_back(Node());
				}
				// move to next node
				n = fsm[n].child[cmap(words[w][i])];
			}
			// end of word, save index as match
			fsm[n].match.push_back(w);
		}
		// complete goto function for root, queue up nodes reached by root
		std::queue<int> q;
		for (int k = 0; k < ALPHA; k++)
		{
			// point to root
			if (fsm[0].child[k] == -1)
			{
				fsm[0].child[k] = 0;
			}
			// if edge k from root
			else if (fsm[0].child[k] > 0)
			{
				// set failure to root
				fsm[fsm[0].child[k]].failure = 0;
				// push node to queue
				q.push(fsm[0].child[k]);
			}
		}
		while (!q.empty())
		{
			// get node id from queue
			int curr = q.front(); q.pop();
			for (int k = 0; k < ALPHA; k++)
			{
				// dest of edge k from curr
				int dest = fsm[curr].child[k];
				// valid edge for curr and k, push dest
				if (dest != -1)
				{
					q.push(dest);
					// node id for traversal
					int v = fsm[curr].failure;
					while (fsm[v].child[k] == -1)
					{
						v = fsm[v].failure;
					}
					fsm[dest].failure = fsm[v].child[k];
					// save all matches for retrieval during search
					fsm[dest].match_parent = fsm[v].child[k];
					while (fsm[dest].match_parent != -1 && fsm[fsm[dest].match_parent].match.empty())
					{
						fsm[dest].match_parent = fsm[fsm[dest].match_parent].match_parent;
					}
				}
			}
		}
	}

	// runs search for words in sentence, returns locations of all matches
	// matches[i] contains indexes of start of matches of words[i] in text (not sorted)
	std::vector<std::vector<int> > search(std::string &sentence, std::vector<std::string> &words)
	{
		std::vector<std::vector<int> > matches(words.size());
		// overall current and temp node index
		int state = 0, ss = 0;

		for (int i = 0, ss = state; i < sentence.length(); i++, ss = state)
		{
			// while no matching, follow fail edges
			while (fsm[ss].child[cmap(sentence[i])] == -1)
			{
				ss = fsm[ss].failure;
			}
			// follow valid edge, update current state
			state = fsm[state].child[cmap(sentence[i])] = fsm[ss].child[cmap(sentence[i])];
			for (ss = state; ss != -1; ss = fsm[ss].match_parent)
			{
				for (int j = 0; j < fsm[ss].match.size(); j++)
				{
					// word match at curr node
					int w = fsm[ss].match[j];
					matches[w].push_back(i + 1 - words[w].length());
				}
			}
		}
		return matches;
	}
};
```

```c++
int main()
{
	// list of strings to match
	std::vector<string> words;
	string text;
	// finite state machine for searching
	Aho_Corasick fsm;
	// build fsm for dictionary of patterns
	fsm.build(words);
	// run search
	std::vector<std::vector<int> > matches = fsm.search(text, words);
}
```

---
