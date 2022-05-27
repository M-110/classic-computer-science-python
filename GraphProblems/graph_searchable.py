from typing import Union, List, Tuple, Set
from graph import Graph, V
from SearchProblems.data_structures import Stack, Queue, PriorityQueue
from SearchProblems.maze import Node

Path = List[str]


class SearchableGraph(Graph):
    def search(self, collection_type: Union[Stack, Queue], start: V, end: V) -> Path or None:
        frontier = collection_type()
        n: Node[V] = Node(start, None)
        frontier.push(n)
        explored: Set[V] = {start}

        while not frontier.empty:
            current_node: Node[V] = frontier.pop()
            current_state: V = current_node.state

            if end ==  current_state:
                return current_node
            # print('for child in: ', current_vertex)
            for child in self.neighbors_for_vertex(current_state):
                if child in explored:
                    continue
                explored.add(child)

                frontier.push(Node(child, current_node))

    def dfs(self, start: V, end: V) -> Path or None:
        return self.search(Stack, start, end)

    def bfs(self, start: V, end: V):
        return self.search(Queue, start, end)

    def retrace_node_path(self, node: Node[V]) -> List[V]:
        """Trace the node's parents and returns  list of all nodes it took
        to reach its current state.
        """
        path = [node.state]
        while node.parent is not None:
            node = node.parent
            path.append(node.state)
        path.reverse()
        return path


if __name__ == "__main__":
    city_graph = SearchableGraph(["Seattle", "San Francisco", "Los Angeles",
                                  "Riverside", "Phoenix", "Chicago", "Boston",
                                  "New York", "Atlanta", "Miami", "Dallas",
                                  "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    result = city_graph.bfs('Boston', 'Phoenix')
    path = city_graph.retrace_node_path(result)
    print(path)
