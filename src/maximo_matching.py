from .path import Path
from .node import Node
from .group import Group
from .grafo_bipartito import GrafoBipartito
import math


class MaximoMatching(object):
    grafo_bipartito: GrafoBipartito = None
    grafo_residual: GrafoBipartito = None
    recorridos: list = []

    def __init__(self, grafo_bipartito: GrafoBipartito):
        self.grafo_bipartito = grafo_bipartito
        self.grafo_residual = grafo_bipartito

    def encontrar_maximo_matching(self, grafo_bipartito: GrafoBipartito):
        for node in grafo_bipartito.group_origin.get_nodes():

    def unir_origen_con_destino(self):
        return True

    def maximo_flujo(self, ):
        while self.depth_first():
            self.buscar_trayectoria_posible()
            self.actualizar_grafo_residual()

    def buscar_trayectoria_posible(self):
        while self.depth_first():
            return True

    def actualizar_grafo_residual(self):
        return True

    def depth_first(self):
        available_path: bool = False
        path_array: 'list of Paths' = self.grafo_residual.source.outgoing_paths
        for outgoing_path in path_array:
            if outgoing_path.weight < outgoing_path.capacity:
                available_path = True
        return available_path


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
