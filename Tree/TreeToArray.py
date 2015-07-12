__author__ = 'rohanmathure'


import unittest

from Tree import Tree
from NodeParent import Node

class TreeToArray:
    def __init__(self):
        self.__tree__ = None
        self.__array__= list()

    def setTree(self,tree):
        self.__tree__= tree

    def convertTreeToArray(self):
        self.__array__ = self.serialize(self.__tree__.getRoot())
        return self.__array__

    def serialize(self,node):
        leftArray= list()
        rightArray = list()

        if not node.getLeft() == None:
            leftArray=self.serialize(node.getLeft())
        else:
            leftArray=[]

        if not node.getRight() == None:
            rightArray=self.serialize(node.getRight())
        else:
            rightArray =[]

        leftArray.append(node.getValue())
        leftArray.extend(rightArray)
        return leftArray

class TestTreeToArray(unittest.TestCase):
    def setUp(self):
        self.treeToArray = TreeToArray()
        tree = Tree()
        node1=Node()
        node1.setValue(1)
        node2=Node()
        node2.setValue(2)
        node3=Node()
        node3.setValue(3)
        node4=Node()
        node4.setValue(4)
        tree.setRoot(node1)
        node1.setLeft(node2)
        node1.setRight(node3)
        node3.setRight(node4)
        self.treeToArray.setTree(tree)

    def testSerialize(self):
        self.assertEqual(self.treeToArray.convertTreeToArray(),[2,1,3,4])


