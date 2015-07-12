__author__ = 'rohanmathure'


class Node:
    def __init__(self):
        self.__value = int()
        self.__left__ = None
        self.__right__= None
        self.__parent__ = None


    def setValue(self,value):
        self.__value = value

    def getValue(self):
        return self.__value

    def setLeft(self,node):
        self.__left__=node

    def getLeft(self):
        return self.__left__

    def setRight(self,node):
        self.__right__=node

    def getRight(self):
        return self.__right__

    def setParent(self,node):
        self.__parent__=node

    def getParent(self):
        return self.__parent__
