from .node import Node
from .group import Group


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
