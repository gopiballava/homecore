
from recordclass import recordclass

Node = recordclass('Node', 'value next previous')


class NoNodesLeftException(Exception):
    pass


class doubleLink(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtHead(self, value):
        new_head = Node(value, self.head, None)
        if self.head is not None:
            self.head.previous = new_head
        self.head = new_head
        if self.tail is None:
            self.tail = self.head
    
    def moveToHead(self, node):
        pass
    
    def popFromTail(self):
        if self.tail is None:
            raise NoNodesLeftException
        retv = self.tail.value
        if self.tail == self.head:
            # Only one node.
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.previous
        return retv
        
