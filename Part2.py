   # Read in the number of vertices (n) and edges (m)
n = int(input())
m = int(input())

# Read the edges from stdin.
edges = []
graph = {}


for _ in range(m):
    edges.append(input().split())

for edge in edges:
    if not (edge[0] in graph):
        graph[edge[0]] = []
    if not (edge[1] in graph):
        graph[edge[1]] = []
    #add each vertex to other's adjacents
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))    

# Read the A edges. You may want to use a different data-structure.
n_A, A = int(input()), []

for _ in range(n_A):
	A.append(input().split())

parent = {}
rank = {}
mst_weight = 0

def find(to_find):
    if parent[to_find] != to_find:
        parent[to_find] = find(parent[to_find])
    return parent[to_find]

def union(u, v):
    id_u = find(u)
    id_v = find(v)

    #when they are joint
    if id_u == id_v:
        return
    
    #when they are disjoint
    if rank[id_u] < rank[id_v]:
        parent[id_u] = id_v
    elif rank[id_u] > rank[id_v]:
        parent[id_v] = id_u
    else:
        #when same rank, make u less a higher rank
        parent[id_v] = id_u
        rank[id_u] += 1


def sort_helper(array):
    return array[2]

edges = sorted(edges, key=sort_helper)

for a in A:
    a_vertex = graph.get(a[0])
    for j in a_vertex:
        if a[1] == j[0]:
            mst_weight += float(j[1])

for edge in edges:
    parent[edge[0]] = edge[0]
    parent[edge[1]] = edge[1]
    rank[edge[0]] = 0
    rank[edge[1]] = 0

for a in A:
    union(a[0], a[1])

for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        mst_weight += float(edge[2])





# Print the weight of the mst to two decimal-places. 
print('{:.2f}'.format(mst_weight))
