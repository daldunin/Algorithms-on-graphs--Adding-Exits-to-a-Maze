#Uses python3

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
