__author__ = 'rohanmathure'


from Tree import Tree
from NodeParent import Node

import unittest

class TreeIterator:
    def __init__(self):
        self.__tree__ = Tree()
        self.__currentNode__ = Node()
        self.__isFirst = True

    def setTree(self,tree):
        self.__tree__=tree

    def next(self):
        tempNode=Node()
        if self.__tree__ == None:
            return False
        if self.__tree__.getRoot() == None:
            return False
        if self.__isFirst:
            self.__isFirst = False
            if not self.__tree__.getRoot().getLeft() == None:
                self.__currentNode__ = self.getLeftMostChild(self.__tree__.getRoot().getLeft())
            else:
                self.__currentNode__ = self.__tree__.getRoot()
        else:
            if not self.__currentNode__.getRight() == None:
                self.__currentNode__=self.getLeftMostChild(self.__currentNode__.getRight())
            elif self.__currentNode__.getParent() == None:
                return False
            elif self.__currentNode__ == self.__currentNode__.getParent().getLeft():
                self.__currentNode__ = self.__currentNode__.getParent()
            elif self.__currentNode__ == self.__currentNode__.getParent().getRight():
                tempNode=self.__currentNode__
                while not tempNode == None:
                    if tempNode == tempNode.getParent().getLeft():
                        self.__currentNode__ = tempNode.getParent()
                        return self.__currentNode__
                    else:
                        tempNode = tempNode.getParent()
                else:
                    return False
        return self.__currentNode__

    def getLeftMostChild(self,node):
        if not node.getLeft() == None:
            return self.getLeftMostChild(node.getLeft())
        else:
            return node


class TestTreeIterator(unittest.TestCase):
    def setUp(self):
        self.treeIterator=TreeIterator()
        tree=Tree()
        node1=Node()
        node2=Node()
        node3=Node()
        node4=Node()
        node5=Node()
        node6=Node()
        node7=Node()
        node8=Node()
        node9=Node()
        node12=Node()
        node2.setValue(2)
        node3.setValue(3)
        node1.setValue(1)
        node4.setValue(4)
        node5.setValue(5)
        node6.setValue(6)
        node7.setValue(7)
        node8.setValue(8)
        node9.setValue(9)
        node12.setValue(12)
        tree.setRoot(node12)
        node12.setLeft(node1)
        node12.setRight(node9)
        node9.setLeft(node2)
        node9.setRight(node4)
        node2.setRight(node8)
        node8.setLeft(node5)
        node8.setRight(node6)
        node4.setLeft(node3)
        node4.setRight(node7)
        node3.setParent(node4)
        node7.setParent(node4)
        node4.setParent(node9)
        node9.setParent(node12)
        node1.setParent(node12)
        node2.setParent(node9)
        node8.setParent(node2)
        node5.setParent(node8)
        node6.setParent(node8)
        self.treeIterator.setTree(tree)

    def testIteration(self):

        self.assertEqual(self.treeIterator.next().getValue(), 1)
        self.assertEqual(self.treeIterator.next().getValue(), 12)
        self.assertEqual(self.treeIterator.next().getValue(), 2)
        self.assertEqual(self.treeIterator.next().getValue(), 5)
        self.assertEqual(self.treeIterator.next().getValue(), 8)
        self.assertEqual(self.treeIterator.next().getValue(), 6)
        self.assertEqual(self.treeIterator.next().getValue(), 9)
        self.assertEqual(self.treeIterator.next().getValue(), 3)
        self.assertEqual(self.treeIterator.next().getValue(), 4)
        self.assertEqual(self.treeIterator.next().getValue(), 7)




