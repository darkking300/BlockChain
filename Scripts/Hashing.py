import hashlib as hasher
import datetime


class Data():
    def __init__(self, index, data, date):
        self.index = index
        self.data = data
        self.date = datetime.datetime.now()
        self.hex = self.hashing()

    def hashing(self):
        """This is the method which performs the hashing operation"""
        sha = hasher.sha256()
        strings = str(self.index) + str(self.data) + str(self.date)
        sha.update(strings.encode('utf-8'))
        return sha.hexdigest()

    def turncoats(self):
        """Never got around to use this as data is not private in class,
        and can be accessed publicly."""
        return self.hex


def genesisBlock():
    """Actually the first block created is never used in this program
    except for that its presence ensure smooth operation on database."""
    firstBlock = Data(0,"This is first block",None)
    return firstBlock

listBlock = []


def nextBlocks(previous_block,data):
    """Creates a new block for the blockchain"""
    index = int(previous_block.index) + 1
    timeStamp = None
    new_block = Data(index, data, timeStamp)
    return new_block





