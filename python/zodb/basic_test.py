from functools import total_ordering

import sys
import ZODB
import ZODB.FileStorage
import persistent
from persistent.list import PersistentList
from persistent.mapping import PersistentMapping
import transaction
from BTrees.OOBTree import TreeSet, BTree


# @total_ordering
class Node(persistent.Persistent):
    from_edges_allowed = set()
    to_edges_allowed = set()

    def __init__(self, title):
        self.title = title
        self.from_edges = PersistentMapping()
        self.to_edges = PersistentMapping()
        if issubclass(self.__class__, ConnectableNode):
            self.from_edges_allowed = set(self.from_edges_allowed)
            self.from_edges_allowed.add('IsPartOfHouse')
        

#     def add_from(self, edge):
#         self.from_edges.add(edge)
#     def __cmp__(self, other):
#         print("CALLED")
#         return cmp(self.title, other.title)
#     def __hash__(self):
#         return self.title
#     def __lt__(self, other):
#         return self.__hash__() < other.__hash__()


class LogicalHouse(Node):
    from_edges_allowed = set()
    to_edges_allowed = set(('IsPartOfHouse', ))

    def create_connected_node(self, node_type: str, node_name: str):
        new_node = globals()[node_type](node_name)
        IsPartOfHouse(new_node, self)
        return new_node
    
    def get_connected_nodes(self):
        return [edge.from_node for edge in self.to_edges['IsPartOfHouse']]

class ConnectableNode(Node):
    from_edges_allowed = set(('IsPartOfHouse',))
    to_edges_allowed = set()
        

class ESPNode(ConnectableNode):
    def get_connected_sensors(self):
        pass


class GPIOConnector(ConnectableNode):
    from_edges_allowed = set(('IsPartOfHouse', 'IsPluggedInToConnector'))
    to_edges_allowed = set(('IsPluggedInToConnector',))

class PhysicalSensor(ConnectableNode):
    pass

class WaterFloatSensor(PhysicalSensor):
    from_edges_allowed = set(('IsPartOfHouse', 'IsPluggedInToConnector'))
    to_edges_allowed = set()


def add_object_to_mapping(obj, mapping, class_names):
    for class_name in class_names:
        if issubclass(obj.__class__, globals()[class_name]):
            if class_name in mapping:
                object_list = mapping[class_name]
            else:
                object_list = PersistentList()
                mapping[class_name] = object_list
            object_list.append(obj)
            return
    raise RuntimeError('Not allowed to add {} to {}'.format(obj, class_names))

            
# @total_ordering
class Edge(persistent.Persistent):
    def __init__(self, from_node, to_node):
        print("Adding edge", from_node, to_node)
        self.from_node = from_node
        self.to_node = to_node
#         print("f,t", from_node, from_node.from_edges, self)
#         print(self.from_node.from_edges)
        add_object_to_mapping(self, self.from_node.from_edges, self.from_node.from_edges_allowed)
        add_object_to_mapping(self, self.to_node.to_edges, self.to_node.to_edges_allowed)
#         self.from_node.from_edges.append(self)
#         self.to_node.to_edges.append(self)
    
    def __cmp__(self, other):
        print("EDGE")
        return cmp(self._get_cmp_string(), other._get_cmp_string())
    def __hash__(self):
        return "{}=>{}".format(self.from_node.title, self.to_node.title)
    def __lt__(self, other):
        return self.__hash__() < other.__hash__()
    def desc(self):
        print("I'm an EDGE")


class IsPartOfHouse(Edge):
    pass

class HasAttachedConnector(Edge):
    pass

class IsPluggedInToConnector(Edge):
    pass



def make_storage():
    storage = ZODB.FileStorage.FileStorage('mydata.fs')
#     storage = None
    db = ZODB.DB(storage)
    connection = db.open()
    return connection


def test_rw():
    db = ZODB.DB(None)
    connection = db.open()
    cli_write(connection=connection)
    cli_read(connection=connection)


def cli_write(connection=None):
    if connection is None:
        connection = make_storage()
    root = connection.root
    root.house = LogicalHouse('beechview_house')
    beechview = root.house

    esp = root.house.create_connected_node('ESPNode', "esp8266")
    water_sensor = beechview.create_connected_node('WaterFloatSensor', 'water_sensor')
    water_gpio = beechview.create_connected_node('GPIOConnector', 'water_gpio')
    e = IsPluggedInToConnector(water_sensor, water_gpio)
#     HasAttachedConnector(esp, water_gpio)
    for node in beechview.get_connected_nodes():
        print(node)
        print('  to:   {}'.format(node.to_edges))
        print('  from: {}'.format(node.from_edges))
    print(esp.from_edges)
    print("Is sub", issubclass( beechview.__class__, globals()['Node']))
    print("Is sub", issubclass(LogicalHouse, globals()['Node']))
    print("Is sub", issubclass(Node, globals()['Node']))
#     root.nodes['wtf'] = e
#     esp.from_edges.append(water_sensor)
    transaction.commit()

def test_write_old():
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


def cli_read(connection=None):
    if connection is None:
        connection = make_storage()
    root = connection.root
    beechview = root.house
    for node in beechview.get_connected_nodes():
        print(node)
        print('  to: SOMEONE is VERB {} to ME '.format(node.to_edges))
        print('  from; This/I am : {}'.format(node.from_edges))
    return
    print(root.nodes['first_esp'])
    for edge in root.nodes['first_esp'].from_edges:
        print("  Edge: {} to {}".format(edge, edge.to_node))
#     print(dir(connection))
#     print(connection.book)

def test_read_old():
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
        cli_write()
    elif sys.argv[1] == 'r':
        cli_read()
    else:
        print("Usage: {} w | r".format(sys.argv[0]))
        print("w writes data to the store on disk, r reads it.")
