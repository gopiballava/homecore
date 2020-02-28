
from recordclass import recordclass

Node = recordclass('Node', 'value next previous')


class doubleLink(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, value):
        """
        Creates a new node and inserts it at the head of our
        double linked list.
        Returns the node object that is at the new head.
        """
        if self.tail is None and self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            new_head = Node(value, self.head, None)
            self.head.previous = new_head
            self.head = new_head
        return self.head

    def moveToHead(self, node):
        """
        Move a pre-existing node to the head of the list,
        making it the most recently used element.
        """
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
        """
        Return the value stored in the tail node of the list,
        which is the least recently accessed value.
        Returns None if the list is empty.
        """
        if self.tail is None:
            return None
        retv = self.tail.value
        if self.tail == self.head:
            # Only one node left, return it, list will now be empty:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.previous
        return retv


class lruCache(object):
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.data = {}
        self.dll = doubleLink()

    def writeItem(self, k, v):
        if k in self.data:
            # Key is present, just update value and LRU order
            self.data[k][1] = v
            self.dll.moveToHead(self.data[k][0])
        else:
            # New key!
            node = self.dll.insertAtHead(k)
            self.data[k] = [node, v]
            if len(self.data) > self.max_size:
                oldest_key = self.dll.popFromTail()
                del self.data[oldest_key]

    def readItem(self, k):
        (node, v) = self.data[k]
        self.dll.moveToHead(node)
        return v
