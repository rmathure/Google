__author__ = 'rohanmathure'

class Node(object):
    def __init__(self):
        self.__value__ = int()
        self.__next__ = None

    def setNext(self,node):
        self.__next__ = node

    def getNext(self):
        return self.__next__

    def getValue(self):
        return self.__value__

    def setValue(self,value):
        self.__value__ = value

    def __eq__(self, another):
        return hasattr(another, '__value__') and self.__value__ == another.__value__
    def __hash__(self):
        return hash(self.__value__)