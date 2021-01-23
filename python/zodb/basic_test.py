from functools import total_ordering

import sys
import ZODB
import ZODB.FileStorage
import persistent
import persistent.list
import transaction
from BTrees.OOBTree import TreeSet, BTree

# @total_ordering
class Node(persistent.Persistent):

    def __init__(self, title):
        self.title = title
        self.from_edges = TreeSet()
#         self.from_edges = persistent.list.PersistentList()
        self.to_edges = persistent.list.PersistentList()

    def add_from(self, edge):
        self.from_edges.add(edge)
#     def __cmp__(self, other):
#         print("CALLED")
#         return cmp(self.title, other.title)
#     def __hash__(self):
#         return self.title
#     def __lt__(self, other):
#         return self.__hash__() < other.__hash__()

class ESPNode(Node):
    def get_connected_sensors(self):
        pass

# @total_ordering
class Edge(persistent.Persistent):
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        print("f,t", from_node, from_node.from_edges, self)
        self.from_node.from_edges.add(self)
        print(self.from_node.from_edges)
        self.to_node.to_edges.append(self)
    
    def __cmp__(self, other):
        print("EDGE")
        return cmp(self._get_cmp_string(), other._get_cmp_string())
    def __hash__(self):
        return "{}=>{}".format(self.from_node.title, self.to_node.title)
    def __lt__(self, other):
        return self.__hash__() < other.__hash__()
    def desc(self):
        print("I'm an EDGE")

#   def connect_nodes(self, from, to):

def make_storage():
    storage = ZODB.FileStorage.FileStorage('/tmp/mydata.fs')
#     storage = None
    db = ZODB.DB(storage)
    connection = db.open()
    return connection

def test_write():
    connection = make_storage()
    root = connection.root
    root.nodes = BTree()

    esp = ESPNode("esp8266")
    root.nodes['first_esp'] = esp
    water_sensor = Node("water_sensor")
    root.nodes['water'] = water_sensor
    e = Edge(esp, water_sensor)
    print(esp.from_edges)
#     root.nodes['wtf'] = e
#     esp.from_edges.append(water_sensor)
    transaction.commit()

def test_read():
    connection = make_storage()
    root = connection.root
    print(root.nodes['first_esp'])
    for edge in root.nodes['first_esp'].from_edges:
        print("  Edge: {} to {}".format(edge, edge.to_node))
#     print(dir(connection))
#     print(connection.book)

class Account(persistent.Persistent):

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount


if __name__ == '__main__':
    if sys.argv[1] == 'w':
        test_write()
    elif sys.argv[1] == 'r':
        test_read()
    else:
        print("Usage: {} w | r".format(sys.argv[0]))
        print("w writes data to the store on disk, r reads it.")
