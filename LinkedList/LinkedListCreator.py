__author__ = 'rohanmathure'


from Node import  Node
import unittest

class LinkedListCreator:
    def __init__(self):
        self.__array__ = list()

    def setArray(self,array):
        self.__array__=array

    def getArray(self):
        return self.__array__

    def getLinkedList(self):
        nodeArray=None
        firstNode=None
        for i in range(len(self.__array__)):
            node = Node()
            node.setValue(self.__array__[i])

            if i-1 > -1:
                nodeArray.setNext(node)
            else:
                firstNode=node
            nodeArray=node

        return firstNode

class TestLinkedListCreator(unittest.TestCase):
    def TestNormal(self):
        link=LinkedListCreator()
        link.setArray([1,2,3])
        linkList=link.getLinkedList()
        self.assertEqual(linkList.getValue(),1)
        self.assertEqual(linkList.getNext().getValue(),2)
        self.assertEqual(linkList.getNext().getNext().getValue(),3)
