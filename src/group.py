from .node import Node


class Group(object):
    name: str = None
    nodes: 'list of Nodes' = []

    def __init__(self, name: str, nodes: 'list of Nodes'):
        self.name = name
        self.nodes = nodes

    def add_node(self, node: Node):
        self.nodes.append(node)

    def remove_node(self, node: Node):
        if any(node == n for n in self.nodes):
            self.nodes.remove(node)
        else:
            print('Node not found in node list')

    def get_nodes(self):
        return self.nodes
