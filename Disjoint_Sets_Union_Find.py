"""Data Structures for Disjoint Sets, Reference - CLRS Page 565"""

# ------------------------- Visual Representation for Linked List implementation on Page 565 CLRS --------------------------

set_dict = {}               # Make it global to make the program simpler
class DisjointSet:
    class Node:
        def __init__(self,info,FORWARD_LINK = None, BACKWARD_LINK = None):
            self.info = info
            self.FORWARD_LINK = FORWARD_LINK
            self.BACKWARD_LINK = BACKWARD_LINK

    class SetObject:
        def __init__(self,set_object_name = None,head = None,tail = None):
            self.set_object_name = set_object_name
            self.head = None
            self.tail = None
        
        def __hash__(self):
            return hash(self.set_object_name)  
    
    def Make_Set(self,item,setname):
        setObject = self.SetObject(setname)
        newNode= self.Node(item)
        newNode.BACKWARD_LINK = setObject
        setObject.head = newNode
        setObject.tail = newNode
        set_dict[item] = setObject 
        return setObject
    
    def Find_Set(self,item):
        setObject = set_dict[item]
        return setObject.head           # Representative of Set

    def Union(self,x,y):      
        x.tail.FORWARD_LINK = y.head
        x.tail = y.tail
        node = y.head
        while node is not None:
            node.BACKWARD_LINK = x
            node = node.FORWARD_LINK
        value = x.head.info
        set_dict[value] = x
        del set_dict[y.head.info]
        y.head = None
        y.tail = None
        return x


        

d = DisjointSet()
s1 = d.Make_Set(25,'S1')
s2 = d.Make_Set(8,'S2')
s3 = d.Make_Set(225,'S3')
d.Make_Set(78,'S4')

x = d.Union(s1,s2)
d.Union(x,s3)
