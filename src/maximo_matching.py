from path import Path
from node import Node
from group import Group
from grafo_bipartito import GrafoBipartito
import math


class MaximoMatching(object):
    grafo_bipartito: GrafoBipartito = None
    grafo_residual: GrafoBipartito = None
    recorridos: list = []

    def __init__(self, grafo_bipartito: GrafoBipartito):
        self.grafo_bipartito = grafo_bipartito
        self.grafo_residual = grafo_bipartito

    def maximo_flujo(self):
        path = []
        count: int = 0
        path = self.buscar_trayectoria_posible()
        if len(path) > 0:
            self.actualizar_grafo_residual(path)
            self.maximo_flujo()
        else:
            for outgoing_path in self.grafo_residual.source.outgoing_paths:
                if outgoing_path.weight == 1:
                    count = count + 1
        if count > 0:
            print(count)

    def buscar_trayectoria_posible(self):
        available_path: list = []
        path_array: 'list of Paths' = self.grafo_residual.source.outgoing_paths
        for outgoing_path in path_array:
            if outgoing_path.weight < outgoing_path.capacity:
                self.depth_first_search(self.grafo_residual.group_origin.find_node_by_name(outgoing_path.name),
                                        available_path)
                if len(available_path) > 0:
                    available_path.insert(0, self.grafo_residual.group_origin.find_node_by_name(outgoing_path.name))
                    self.recorridos.append(available_path)
                    for recorrido in self.recorridos:
                        print("[", end="")
                        for nodo in recorrido:
                            print(nodo.name, end=",")
                        print("]", end=";")
                    print("")
                    break
        return available_path


    def actualizar_grafo_residual(self, nodes: 'list of Nodes'):
        self.grafo_residual.update_path(nodes, 1)


    def depth_first_search(self, start: Node, walkthrough: list):
        if start.name != 'T':
            for neighbor in start.outgoing_paths:
                if neighbor.weight < neighbor.capacity:
                    walkthrough.append(self.grafo_bipartito.find_node_by_name(neighbor.name))
                    self.depth_first_search(self.grafo_bipartito.find_node_by_name(neighbor.name), walkthrough)
                    break
                else:
                    walkthrough.clear()
                    self.depth_first_search(self.grafo_bipartito.find_node_by_name(neighbor.name), walkthrough)
        else:
            return walkthrough


group_a = Group('A', [
    Node('A1', [Path('B1', 0, math.inf), Path('B2', 0, math.inf)]),
    Node('A2', [Path('B2', 0, math.inf), Path('B3', 0, math.inf)]),
    Node('A3', [Path('B3', 0, math.inf), Path('B4', 0, math.inf)]),
    Node('A4', [Path('B4', 0, math.inf)])

])
group_b = Group('B', [
    Node('B1', [Path('T', 0, 1)]),
    Node('B2', [Path('T', 0, 1)]),
    Node('B3', [Path('T', 0, 1)]),
    Node('B4', [Path('T', 0, 1)]),
])
source = Node('S', [])
for node in group_a.get_nodes():
    source.add_outgoing_path(Path(node.name, 0, 1))
terminal = Node('T', [])
gb = GrafoBipartito(source, group_a, group_b, terminal)

MaximoMatching = MaximoMatching(gb)
MaximoMatching.maximo_flujo()
