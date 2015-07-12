__author__ = 'rohanmathure'

from Tree import Tree
from Node import Node
import unittest

class BFS:
    def __init__(self):
        self.__currentLevel= list()
        self.__nextLevel = list()
        self.__maxLevel = int()
        self.__findNodeValue = int()
        self.__tree = Tree()
        self.__visitedNodes=dict()

    def setMaxLevel(self,value):
        self.__maxLevel = value

    def setFindNodeValue(self,value):
        self.__findNodeValue = value

    def getFindNodeValue(self):
        return self.__findNodeValue

    def getMaxLevel(self):
        return self.__maxLevel

    def setTree(self,tree):
        self.__tree=tree

    def searchTree(self):
        level=0
        found=False
        if self.__tree is None:
            return -1
        self.__currentLevel.append(self.__tree.getRoot())
        while level <= self.getMaxLevel():
            for node in self.__currentLevel:
                if self.__visitedNodes.get(node.getValue(),-1) != -1:
                    continue        #we do not need to process this node since we have already encountered it.
                    # as it is BFS the previous encounter is definitely going to have a lower cost
                if node.getValue()==self.__findNodeValue:
                    found=True
                    break
                else:
                    self.__nextLevel.extend(node.getChildren())
                    self.__visitedNodes[node.getValue()]=level
            if found:
                break
            level= level+1
            self.__currentLevel = list()
            self.__currentLevel.extend(self.__nextLevel)
            self.__nextLevel = list()
        if found:
            return level
        else:
            return -1


class TestBFS(unittest.TestCase):
    def setUp(self):
        self.bfs=BFS()
        tree=Tree()
        node1=Node()
        node1.setValue(1)
        node2=Node()
        node2.setValue(2)
        node3=Node()
        node3.setValue(3)
        node4=Node()
        node4.setValue(4)
        node5=Node()
        node5.setValue(5)
        node1.addChild(node2)
        node1.addChild(node3)
        node2.addChild(node4)
        node3.addChild(node5)
        node4.addChild(node2)
        tree.setRoot(node1)
        self.bfs.setTree(tree)

    def testBaseCase(self):
        self.bfs.setFindNodeValue(3)
        self.bfs.setMaxLevel(5)
        self.assertEqual(self.bfs.searchTree(), 1)

    def testNotFound(self):
        self.bfs.setFindNodeValue(8)
        self.assertEqual(self.bfs.searchTree(), -1)

    def testShortestPath(self):
        self.bfs.setFindNodeValue(2)
        self.bfs.setMaxLevel(1)
        self.assertEqual(self.bfs.searchTree(), 1)

    def testRoot(self):
        self.bfs.setFindNodeValue(1)
        self.assertEqual(self.bfs.searchTree(), 0)

    def testLevel(self):
        self.bfs.setFindNodeValue(5)
        self.bfs.setMaxLevel(1)
        self.assertEqual(self.bfs.searchTree(), -1)

    def testLevelFound(self):
        self.bfs.setFindNodeValue(5)
        self.bfs.setMaxLevel(5)
        self.assertEqual(self.bfs.searchTree(), 2)