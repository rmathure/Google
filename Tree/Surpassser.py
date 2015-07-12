__author__ = 'rohanmathure'


import unittest
from NodeParent import Node
from Tree import Tree

class Surpasser:
    def __init__(self):
        self.__tree__ = None
        self.__numArray__ = list()
        self.__maxSurpasser__ = 0

    def setTree(self,tree):
        self.__tree__ = tree

    def setArray(self,numArray):
        self.__numArray__ = numArray

    def createNode(self,value):
        node = Node()
        node.setValue(value)
        return node

    def addNode(self,node,startNode):

        if node.getValue() <= startNode.getValue():
            if startNode.getLeft() == None:
                startNode.setLeft(node)
            else:
                self.addNode(node,startNode.getLeft())
        else:
            if startNode.getRight() == None:
                startNode.setRight(node)
            else:
                self.addNode(node,startNode.getRight())

    def buildTree(self):
        for i in self.__numArray__:
            if self.__tree__ == None:
                self.__tree__=Tree()
                self.__tree__.setRoot(self.createNode(i))
            else:
                startNode=self.__tree__.getRoot()
                node=self.createNode(i)
                self.addNode(node,startNode)

    def findMaxSurpasser(self,startNode):
        if startNode == None:
            return
        else:
            rightNode=startNode.getRight()
            maxNum=self.findTreeElementNum(rightNode)
            if maxNum>self.__maxSurpasser__:
                self.__maxSurpasser__=maxNum
            self.findMaxSurpasser(startNode.getLeft())


    def findTreeElementNum(self,node):
        if node == None:
            return 0
        else:
            return 1+ self.findTreeElementNum(node.getLeft())+self.findTreeElementNum(node.getRight())











class TestSurpasser(unittest.TestCase):
    def setUp(self):
        self.treeArray=Surpasser()
        self.treeArray.setArray([9,7,7,5,5,2,7,0,8,1])
        self.treeArray.buildTree()

    def TestFindTreeElement(self):
        self.assertEqual(self.treeArray.findTreeElementNum(self.treeArray.__tree__.getRoot()),10)

    def TestFindMaxSurpasser(self):
        self.treeArray.findMaxSurpasser(self.treeArray.__tree__.getRoot())
        self.assertEqual(self.treeArray.__maxSurpasser__,2)