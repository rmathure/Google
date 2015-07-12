__author__ = 'rohanmathure'


class Node:
    def __init__(self):
        self.__value = int()
        self.__children= list()

    def setValue(self,value):
        self.__value = value

    def getValue(self):
        return self.__value

    def addChild(self,node):
        self.__children.append(node)

    def getChildren(self):
        return self.__children