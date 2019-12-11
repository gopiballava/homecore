from .lru import doubleLink


def test_double_link():
    dl = doubleLink()
    for i in range(10):
        dl.insertAtHead(i)
    for i in range(10):
        assert dl.popFromTail() == i
