# Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

edges, queries = [], []
graph = {}

for _ in range(m):
    edges.append(input().split())

#Adds edges to adjacent list structure
for edge in edges:
    if not (edge[0] in graph):
        graph[edge[0]] = []
    if not (edge[1] in graph):
        graph[edge[1]] = []
    #add each vertex to other's adjacents
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0]) 

q = int(input())

for _ in range(q):
    queries.append(input().split())
	
# Print a `1` to stdout for each query. This section should be altered to instead print a `1` where the
# query indicates a connection and `0` else.

def dfs_visit(node, end, visited):
    visited[node] = True
    for v in graph.get(node, []):
        if v == end:
            return True
        if not visited[v]:
            if dfs_visit(v, end, visited):
                return True
    return False

def dfs(start, end):
    visited = {}
    for u in graph:
        visited[u] = False
    if dfs_visit(start, end, visited):
        print(1)
    else:
        print(0)


for i in queries:
    dfs(i[0], i[1])

