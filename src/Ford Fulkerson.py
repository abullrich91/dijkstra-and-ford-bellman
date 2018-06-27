import math

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])
    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


# Create a graph given in the above diagram

bpGraph = [[0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 1]]

practGraph = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, math.inf, math.inf, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, math.inf, math.inf, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, math.inf, math.inf, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
testGraph = [[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],#0,source
             [0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, math.inf, 0, 0, 0],#1,p
             [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0, 0, 0, math.inf, 0],#2,p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, math.inf, 0, 0, 0, 0],#3,p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0],#4p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, math.inf, 0],#5p
             [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0, 0, 0, math.inf, 0],#6p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0, math.inf, 0, 0],#7p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#8q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#9q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#10q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#11q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#12q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#13q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #14 terminal
g = Graph(practGraph)

source = 0
sink = 9


print("maximo flujo %d" %g.FordFulkerson(source, sink))

