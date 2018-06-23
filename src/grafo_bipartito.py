from node import Node
from group import Group
from path import Path


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

    def update_path(self, walkthrough: 'list of Nodes', new_weight: int = 1):
        i: int = 0
        for path in self.source.outgoing_paths:
            if path.name == walkthrough[0].name:
                path.weight = 1
        for node in walkthrough:
            i = 0
            path: Path = self.find_outgoing_path_from_node_list(node, walkthrough)
            if path is not None:
                path.weight = 1

    def find_outgoing_path_from_node_list(self, current_node: Node, nodes: 'list of Nodes'):
        outgoing_path: Path = None
        for path in current_node.outgoing_paths:
            if any(path.name == node.name for node in nodes):
                outgoing_path = path
                break
        return outgoing_path
