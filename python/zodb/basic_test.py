
import ZODB, ZODB.FileStorage
import persistent
from BTrees.OOBTree import TreeSet

class Book(persistent.Persistent):

   def __init__(self, title):
       self.title = title
       self.authors = TreeSet()

   def add_author(self, author):
       self.authors.add(author)


def test_storage():
    #storage = ZODB.FileStorage.FileStorage('mydata.fs')
    storage = None
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    book = Book("ZODB")
    connection.add(book)
    