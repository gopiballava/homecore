from .lru import doubleLink


def test_double_link_simple():
    dl = doubleLink()
    for i in range(10):
        dl.insertAtHead(i)
    for i in range(10):
        assert dl.popFromTail() == i
    assert dl.popFromTail() is None


def test_double_link_move():
    dl = doubleLink()
    added = []
    for i in range(5):
        added.append(dl.insertAtHead(i))
    dl.moveToHead(added[2])
    for i in (0, 1, 3, 4, 2):
        assert dl.popFromTail() == i
    assert dl.popFromTail() is None
    
    dl = doubleLink()
    added = []
    for i in range(5):
        added.append(dl.insertAtHead(i))
    dl.moveToHead(added[4])
    for i in (0, 1, 2, 3, 4):
        assert dl.popFromTail() == i
    assert dl.popFromTail() is None
    
    dl = doubleLink()
    added = []
    for i in range(5):
        added.append(dl.insertAtHead(i))
    added.reverse()
    for i in range(5):
        dl.moveToHead(added[i])
    for i in (4, 3, 2, 1, 0):
        assert dl.popFromTail() == i
    assert dl.popFromTail() is None