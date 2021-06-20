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

lst = DoublyLinkedList()


