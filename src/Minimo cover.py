import itertools


class Vertex_Cover:

    def __init__(self, graph):
        self.graph = graph

    def validity_check(self, cover):
        is_valid = True
        for i in range(len(self.graph)):
            for j in range(i+1, len(self.graph[i])):
                if self.graph[i][j] == 1 and cover[i] != '1' and cover[j] != '1':
                    return False

        return is_valid

    def vertex_cover_naive(self):
        n = len(self.graph)
        minimum_vertex_cover = n
        a = list(itertools.product(*["01"] * n))
        for i in a:
            if Vertex_Cover.validity_check(ins, i):
                counter = 0
                for value in i:
                    if value == '1':
                        counter += 1
                minimum_vertex_cover = min(counter, minimum_vertex_cover)

        return minimum_vertex_cover

if __name__ == '__main__':
    graph =[[0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0]]
    testgraph = [[1, 1, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 1],
                 [0, 0, 0, 1]]
    practGraph = [[0, 1, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 1],
                  [0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 1, 0, 1],
                  [1, 0, 0, 0, 0, 1],
                  [0, 1, 0, 0, 1, 0]]
    bpGraph = [[0, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [1, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 1]]
    ins = Vertex_Cover(bpGraph)

    print ('the minimum vertex-cover is:', Vertex_Cover.vertex_cover_naive(ins))