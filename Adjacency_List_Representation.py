"""Author - Anantvir Singh, concept reference:= Data Structures and Algorithms by Michael T. Goodrich et al"""

"""----------------------------Adjacency List Representation---------------------------------"""

class DoublyLinkedList:
    class Node:
        def __init__(self,info,backward_link = None,forward_link = None):
            self.FORWARD_LINK = forward_link
            self.BACKWARD_LINK = backward_link
            self.info = info
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_ptr = None
        self.size = 0
    
    def insert_item_at_head(self,item):
        if self.head is None:
            newNode = self.Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode = self.Node(item)
            newNode.FORWARD_LINK = self.head
            self.head.BACKWARD_LINK = newNode
            self.head = newNode
            self.size += 1
        return newNode
    
    def insert_item_at_tail(self,item):
        if self.tail is None:
            newNode = self.Node(item)
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            newNode = self.Node(item)
            self.tail.FORWARD_LINK = newNode
            newNode.BACKWARD_LINK = self.tail
            self.tail = newNode
            self.size += 1
        return newNode
    
    def insert_item_between_nodes(self,item,LOCA,LOCB):
        newNode = self.Node(item)
        newNode.FORWARD_LINK = LOCB
        newNode.BACKWARD_LINK = LOCA
        LOCA.FORWARD_LINK = newNode
        LOCB.BACKWARD_LINK = newNode
        self.size += 1
        return newNode
    
    def traverse_list(self):
        if self.head == None:
            raise KeyError('Cant traverse. List is Empty !')
        self.current_ptr = self.head
        while(self.current_ptr is not None):
            print(self.current_ptr.info)
            self.current_ptr = self.current_ptr.FORWARD_LINK
        self.current_ptr = self.head

# ---------------------------------------------Vertex------------------------------------------------------
class Vertex:
    def __init__(self,value):
        self.value = value
        self.incidence_list = []
    
    def element(self):
        return self.value
    
    def __hash__(self):
        return hash(id(self))

# ---------------------------------------------Edge------------------------------------------------------

class Edge:
    def __init__(self,u,v,value):
        self.origin = u
        self.destination = v
        self.value = value
    
    def endpoints(self):
        return (self.origin,self.destination)

    def opposite(self,v):
        return self.origin if v is self.destination else self.origin
    
    def element(self):
        return self.value
    
    def __hash__(self):
        return hash((self.origin,self.destination))     # Always make vertex and edges hashable

class Graph:
    def __init__(self,directed = False):
        self.outgoing = []                              # can be list or doubly linked list
        self.incoming = [] if directed == True else self.outgoing
    
    def is_Directed(self):
        return self.outgoing is not self.incoming
    
    def vertex_count(self):
        return len(self.outgoing)
    
    def vertices(self):
        for vertex in self.outgoing:
            print(vertex)
    
    def edge_count(self):
        edges = set()
        for vertex in self.outgoing:
            edges.add(vertex.incidence_list)
        return len(edges)
    
    def get_Edge(self,u,v):
        for edge in u.incidence_list:
            if edge in v.incidence_list:
                return edge
    
    def degree(self,v):
        return len(v.incidence_list)
    
    def incident_edges(self,v,outgoing = True):
        for edge in v.incidence_list:
            yield edge
    
    def insert_Vertex(self,x):
        v = Vertex(x)
        self.outgoing.append(v)
        if self.is_Directed():
            self.incoming.append(v)
        return v
    
    def insert_edge(self,u,v,x):
        e = Edge(u,v,x)
        u.incidence_list.append(e)
        v.incidence_list.append(e)
        return e

g = Graph()
u= g.insert_Vertex('u')
v = g.insert_Vertex('v')
g.insert_edge(u,v,'e')
w = g.insert_Vertex('w')
g.insert_edge(u,w,'g')
g.insert_edge(v,w,'f')
z = g.insert_Vertex('z')
g.insert_edge(w,z,'h')

    



