from collections import defaultdict

class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight) -> None:
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    @staticmethod
    def dijsktra(graph, initial, end) -> list:
        shortest_paths = {initial: (None, 0)}
        current_node = initial

        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
                next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                raise ValueError("Path not possible")

            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node

        path = path[::-1]
        return path

    @staticmethod
    def print_result(start: str, end: str, data: list):
        print(f"jalur terpendek dari {start} ke {end} adalah:", end=" ")
        for index, node in enumerate(data):
            if index == len(data) - 1:
                print(node)
            else:
                print(node, end=" -> ")

if __name__ == '__main__':
    graph = Graph()

    edges = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('B', 'D', 2.5),
        ('C', 'F', 2.7),
        ('C', 'G', 3.1),
        ('D', 'E', 1.5),
        ('E', 'H', 10),
        ('F', 'G', 1),
        ('F', 'H', 4.5),
        ('G', 'H', 4.2),
        ('H', 'E', 10),
    ]

    for edge in edges:
        graph.add_edge(*edge)

    graph.print_result('A', 'H', graph.dijsktra(graph, 'A', 'H'))
    graph.print_result('C', 'H', graph.dijsktra(graph, 'C', 'H'))
