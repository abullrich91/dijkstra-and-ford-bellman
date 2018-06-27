from collections import defaultdict
import math

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
    def minCut(self, source, sink):
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
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] > 0 and self.org_graph[i][j] == 0:
                    if i < sink and j > source :
                      print (str(j) + " - " + str(i))



#grafos
practGraph = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0], #0, source
              [0, 0, 0, 0, 0, math.inf, math.inf, 0, 0, 0],#1,A1
              [0, 0, 0, 0, 0, 0, math.inf, math.inf, 0, 0],#2 A2
              [0, 0, 0, 0, 0, 0, 0, math.inf, math.inf, 0],#3 A3
              [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0],#4 A4
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#5 B1
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#6 B2
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#7 B3
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#8 B4
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]#9 sink/terminal

testGraph = [[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],#0,source
             [0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, math.inf, 0, 0, 0],#1,p
             [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0, 0, 0, math.inf, 0],#2,p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, math.inf, 0, 0, 0, 0],#3,p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0],#4 p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, math.inf, 0],#5 p
             [0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0, 0, 0, math.inf, 0],#6 p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, math.inf, 0, 0, math.inf, 0, 0],#7 p
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#8 q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#9 q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#10 q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#11 q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#12 q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],#13 q
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #14 terminal


g = Graph(practGraph)

source = 0
sink = 9
g.minCut(source, sink)


