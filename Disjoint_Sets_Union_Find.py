"""Data Structures for Disjoint Sets, Reference - CLRS Page 565"""

# ------------------------- Visual Representation for Linked List implementation on Page 565 CLRS --------------------------

set_dict = {}               # Make it global to make the program simpler. Disjoint sets are stored here with key = representative of a set(i.e first element of linked list)
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
    
    def Make_Set(self,item,setname):            # Creates a new linked list, whose only object is 'item'
        setObject = self.SetObject(setname)
        newNode= self.Node(item)
        newNode.BACKWARD_LINK = setObject
        setObject.head = newNode
        setObject.tail = newNode
        set_dict[item] = setObject 
        return setObject
    
    def Find_Set(self,item):
        if set_dict.get(item) is not None:
            return set_dict[item].head
        else:
            for value in set_dict.values():
                node = value.head
                while node is not None:
                    if node.info == item:
                        return node.BACKWARD_LINK
                    node = node.FORWARD_LINK
                   
                raise ValueError('Cannot find this item in any Disjoint Set') 
                 # Representative of Set

    def Union(self,x,y):                # Implementation as per page 565 CLRS    
        x.tail.FORWARD_LINK = y.head
        x.tail = y.tail
        node = y.head
        while node is not None:
            node.BACKWARD_LINK = x
            node = node.FORWARD_LINK
        value = x.head.info
        set_dict[value] = x             # Create new disjoint set in set_dict
        del set_dict[y.head.info]       # Remove old set 'y' as y has been merged with 'x' now
        y.head = None                   # head and tail of 'y' are now None
        y.tail = None
        return x                        # Return new Disjoint set x


d = DisjointSet()
s1 = d.Make_Set(25,'S1')
s2 = d.Make_Set(8,'S2')
s3 = d.Make_Set(225,'S3')
s4 = d.Make_Set(78,'S4')

x = d.Union(s1,s2)
y = d.Union(s3,s4)
d.Union(x,y)
a = d.Find_Set(8)
b = d.Find_Set(78)
print(a is b)
