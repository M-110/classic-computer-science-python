from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')  # Vertex type


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = None):
        if vertices is None:
            vertices = []
        self._vertices = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        """Get number of vertices."""
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        """Get number of edges."""
        return sum(len(edge) for edge in self._edges)

    def add_vertex(self, vertex: V) -> int:
        """Add the vertex to the graph and returns its
        index as int."""
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge):
        """Add an edge to the graph corresponding with
        both directions."""
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int):
        """Add edge between vertex u and vertex v."""
        self.add_edge(Edge(u, v))

    def add_edge_by_vertices(self, first: V, second: V):
        """Lookup the indices of the first and second variable
        and then add an edge between those indices."""
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int) -> V:
        """Get the vertex at the given index."""
        return self._vertices[index]

    def index_of(self, vertex: V) -> int:
        """Get the index of the given vertex."""
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int) -> List[V]:
        """Get a list of vertices connected to the vertex at
        the given index by an edge."""
        return [self.vertex_at(edge.v) for edge in self._edges[index]]

    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        """Get a list of vertices connected to the given vertex."""
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int) -> List[Edge]:
        """Get a list of edges for the vertex at the given index."""
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        """Get a list of edges for the given vertex."""
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self):
        """Return a string that shows each vertex and the neighbors 
        it shares an edge with."""
        return '\n'.join([f'{self.vertex_at(i)} -> {self.neighbors_for_index(i)}'
                          for i in range(self.vertex_count)])


if __name__ == "__main__":
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles",
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
    print(city_graph)
