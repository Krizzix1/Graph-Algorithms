### Part 1
A solution for the problem of determining connectivity between vertex pairs in an undirected graph. Given an undirected graph G = (V, E) with n vertices and m edges, and a list of vertex pairs, the task is to decide whether there is a path between each pair of vertices.

The challenge is to design and implement an algorithm that solves this problem efficiently with a time complexity of O(q * (m + n)), where q is the number of queries.

### Part 2
This repository contains a solution for a variant of the Minimum Spanning Tree (MST) problem. The goal is to connect all vertices of an undirected graph into a single connected network while minimizing the cost of adding new edges, given a set of existing edges.

Specifically, we are given:

- An undirected graph G = (V, E) with n vertices (numbered from 0 to n-1) and m edges.
- A positive cost c_e associated with each edge in E.
- A subset of edges A ⊆ E, which represents existing direct fibre links between vertices.
- The task is to find a subset X ⊆ E \ A of edges with minimum cost such that the resulting graph (V, X ∪ A) is connected.
