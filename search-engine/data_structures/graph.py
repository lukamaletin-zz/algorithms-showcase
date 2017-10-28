# Author: Luka Maletin


class GraphError(Exception):
    pass


class Graph(object):
    class Vertex(object):
        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

    class Edge(object):
        def __init__(self, u, v):
            self._source = u
            self._destination = v

        def source(self):
            return self._source

        def destination(self):
            return self._destination

        def __hash__(self):
            return hash((self._source, self._destination))

    def __init__(self):
        # (K, V) = (Vertex, destinations (dictionary)):
        self._outgoing = {}  # top-level dictionary

        # (K, V) = (Vertex, sources (dictionary)):
        self._incoming = {}  # top-level dictionary

        # (K, V) = (link, Vertex)
        self._vertices = {}

    def insert_vertex(self, x=None):
        if x not in self._vertices:
            v = self.Vertex(x)
            # (K, V) = (Vertex, Edge):
            self._outgoing[v] = {}

            # (K, V) = (Vertex, Edge):
            self._incoming[v] = {}

            self._vertices[x] = v
            return v
        else:
            return self._vertices[x]

    def insert_edge(self, u, v):
        if self.get_edge(u, v) is not None:
            raise GraphError('Vertices are already connected.')
        e = self.Edge(u, v)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def get_vertex(self, x):
        return self._vertices[x]

    def incoming_degree(self, v):
        return len(self._incoming[v])

    def incoming_edges(self, v):
        result = []
        for edge in self._incoming[v].values():
            result.append(edge)
        return result
