
import ZODB, ZODB.FileStorage

def test_storage():
    #storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(None)
    connection = db.open()
    root = connection.root

import persistent

class Account(persistent.Persistent):

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def cash(self, amount):
        assert amount < self.balance
        self.balance -= amount
