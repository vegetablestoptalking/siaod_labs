class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value: str) -> None:
        self.nodes.add(value)

    def add_edge(self, from_node: str, to_node: str, cost: int) -> None:
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = cost


def find_min_road(graph) -> int:  # i'm hate yours lower-case. java, i love you :(
    pass




