from .path import Path


class Node(object):
    name: str = None
    outgoing_paths: 'list of Paths' = []

    def __init__(self, node_name: str, outgoing_paths: 'list of Paths'):
        self.name = node_name
        self.outgoing_paths = outgoing_paths

    def add_outgoing_path(self, path: Path):
        self.outgoing_paths.append(path)

    def remove_incoming_path(self, path: Path):
        if any(path == p for p in self.outgoing_paths):
            self.outgoing_paths.remove(path)
        else:
            print('Path not found in path list')
