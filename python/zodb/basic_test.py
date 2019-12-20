
import ZODB, ZODB.FileStorage

def test_storage():
    #storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(None)
    connection = db.open()
    root = connection.root