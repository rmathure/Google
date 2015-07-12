__author__ = 'rohanmathure'

from Node import Node

class LinkedList:
    def __init__(self):
        self.__head__=Node()

    def getHead(self):
        return self.__head__

    def setHead(self,node):
        self.__head__=node