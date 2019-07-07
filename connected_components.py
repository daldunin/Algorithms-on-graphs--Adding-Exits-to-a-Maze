#Uses python3

# Problem: Adding Exits to a Maze
# Problem Introduction
# Now you decide to make sure that there are no dead zones in a maze, that is, that at least one exit is
# reachable from each cell. For this, you find connected components of the corresponding undirected graph
# and ensure that each component contains an exit cell.
# Problem Description
# Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components
# in it.
# Input Format. A graph is given in the standard format.
# Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑚 ≤ 103.
# Output Format. Output the number of connected components.

import sys
import numpy


def number_of_components(adj):
    result = 0
    #write your code here
    cc = 1
    for v in range(0, len(adj)):
        if not visited[v]:
            explore(v, cc)
            cc += 1
    result = int(max(CCnum))
    return result


def explore(v, cc):
    visited[v] = 1
    CCnum[v] = cc
    for w in adj[v]:
        if not visited[w]:
            explore(w, cc)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = numpy.zeros((n, 1))
    CCnum = numpy.zeros((n, 1))  # number of connected component that vertex belongs to
    print(number_of_components(adj))
