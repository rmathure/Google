__author__ = 'rohanmathure'

class Node:
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
