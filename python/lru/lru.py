
from recordclass import recordclass

Node = recordclass('Node', 'value next previous')


class NoNodesLeftException(Exception):
    pass


class doubleLink(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtHead(self, value):
        if self.tail is None and self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_head = Node(value, self.head, None)
            self.head.previous = new_head
            self.head = new_head
    
    def moveToHead(self, node):
        pass
    
    def popFromTail(self):
        if self.tail is None:
            raise NoNodesLeftException
        retv = self.tail.value
        if self.tail == self.head:
            # Only one node left, return it, list will be empty:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.previous
        return retv
        
