class Path(object):
    name: str = None
    weight: int = None
    capacity: int = None

    def __init__(self, name: str, weight: int, capacity: int):
        self.name = name
        self.weight = weight
        self.capacity = capacity

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_weight(self):
        return self.weight

    def set_weight(self, weight: int):
        self.weight = weight

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity: int):
        self.capacity = capacity
