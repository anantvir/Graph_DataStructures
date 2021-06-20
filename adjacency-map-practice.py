class Vertex:
    def __init__(self, data):
        self.data = data

    def get_vertex_data(self):
        return self.data
    
    def __hash__(self):
        return hash(id(self))       # Make it hashable so that a Vertex object can be a key of dict
    
class Edge:
    def __init__(self, u, v, data):
        self.origin = u
        self.destination = v
        self.data = data
    
    def endpoints(self):
        return (self.origin, self.destination)
    
    def opposite(self, u):
        return self.destination if u is self.origin else self.destination
    
    def get_edge_data(self):
        return self.data
    
    def __hash__(self):         # make hasble so that edge object can be a key in dict
        return hash((self.origin, self.destination))

class Graph:

    # Adjacency Map looks like this , u,v,w are vertices. e,f,g,h ar edges
    # {
    #     u : {
    #         v : e,
    #         w : g
    #     },
    #     v : {
    #         u : e,
    #         w : f
    #     },
    #     w : {
    #         u : g,
    #         v : f,
    #         z : h
    #     }
    # }
    def __init__(self, directed = False):
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing
    
    def isDirected(self):
        return self.outgoing is self.incoming

    def vertex_count(self):
        return len(self.outgoing)
    
    def vertices(self):
        return self.outgoing.keys() # return an iterable of vertices
    
    def edge_count(self):
        total = sum(len(self.outgoing[i]) for i in self.outgoing)
        return total if self.isDirected() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self.outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self, u, v):
        self.outgoing[u].get(v)     # use get() because it returns None if no edge is present
    
    def degree(self, v):
        return len(self.outgoing[v])
    
    def incident_edges(self, v):
        return self.outgoing[v].values()        # returns iterable list of edges
    
    def insert_vertex(self, data = None):
        v = Vertex(data)
        self.outgoing[v] = {}
        if self.isDirected():
            self.incoming = {}
        return v
    
    def insert_edge(self, u, v, data = None):
        edge = Edge(u, v, data)
        self.outgoing[u][v] = edge


        
        