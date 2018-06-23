from node import Node
from group import Group


class GrafoBipartito(object):
    source: Node = None
    group_origin: Group = None
    group_destination: Group = None
    terminal: Node = None

    def __init__(self, source: Node, group_origin: Group, group_destination: Group, terminal: Node):
        self.source = source
        self.group_origin = group_origin
        self.group_destination = group_destination
        self.terminal = terminal

    def find_node_by_name(self, name: str):
        for node in self.group_origin.nodes:
            if node.name == name:
                return node
        for node in self.group_destination.nodes:
            if node.name == name:
                return node
        if self.terminal.name == name:
            return self.terminal
        if self.source.name == name:
            return self.source
        return None
