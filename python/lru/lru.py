
from recordclass import recordclass

Node = recordclass('Node', 'value next previous')


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
        return self.head

    def moveToHead(self, node):
        # We'll do nothing if it's already head:
        if self.head is not node:
            if node.previous is not None:
                node.previous.next = node.next
            if node.next is not None:
                node.next.previous = node.previous
            node.previous = None
            node.next = self.head
            self.head.previous = node
            self.head = node
        
    def popFromTail(self):
        if self.tail is None:
            return None
        retv = self.tail.value
        if self.tail == self.head:
            # Only one node left, return it, list will be empty:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.previous
        return retv
        

class lruCache(object):
    def __init__(self, max_size=10):
        self.max_size = max_size
        # We store [node, value]
        self.data = {}
        # Double linked list of keys we might want to delete if we need more cache space
        self.dll = doubleLink()

    def writeItem(self, k, v):
        if k in self.data:
            # Already present, update value and LRU order
            self.data[k][1] = v
            self.dll.moveToHead(self.data[k][0])
        else:
            # New key!
            node = self.dll.insertAtHead(k)
            self.data[k] = [node, v]
    
    def readItem(self, k):
        (node, v) = self.data[k]
        self.dll.moveToHead(node)
        return v
            