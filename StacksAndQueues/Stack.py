__author__ = 'rohanmathure'

import unittest
from LinkedList.Node import Node


class LinkedList:
    def __init__(self):
        self.__head__=NodeMin()

    def getHead(self):
        return self.__head__

    def setHead(self,node):
        self.__head__=node


class NodeMin(Node):
    def __init__(self):
        super(NodeMin,self).__init__()
        self.__min__=None

    def setMin(self,value):
        self.__min__= value

    def getMin(self):
        return self.__min__



class Stack:
    def __init__(self):
        self.__linkedListList__=LinkedList()

    def push(self,node):
        headNode=self.__linkedListList__.getHead()
        #Manage minimum here
        if not headNode is None:
            if headNode.getMin() < node.getValue():
                node.setMin(headNode.getMin())
        else:
            node.setMin(node.getValue())
        self.__linkedListList__.setHead(node)
        node.setNext(headNode)

    def pop(self):
        headNode=self.__linkedListList__.getHead()
        self.__linkedListList__.setHead(headNode.getNext())
        return headNode

    def getMin(self):
        #get the current min here
        return self.__linkedListList__.getHead().getMin()

class TestStack(unittest.TestCase):
    def setUp(self):
        self.ll=LinkedList()
        node1=NodeMin()
        node1.setValue(1)
        node2=NodeMin()
        node2.setValue(2)
        node3=NodeMin()
        node3.setValue(3)
        node9=NodeMin()
        node9.setValue(9)
        node7=NodeMin()
        node7.setValue(7)
        self.stack=Stack()
        self.stack.push(node2)
        self.stack.push(node9)
        self.stack.push(node1)
        self.stack.push(node3)
        self.stack.push(node7)


    def testStack(self):
        self.assertEqual(self.stack.getMin(),1)
        self.assertEqual(self.stack.pop().getValue(),7)
        self.assertEqual(self.stack.getMin(),1)
        self.assertEqual(self.stack.pop().getValue(),3)
        self.assertEqual(self.stack.getMin(),1)
        self.assertEqual(self.stack.pop().getValue(),1)
        self.assertEqual(self.stack.getMin(),2)
        self.assertEqual(self.stack.pop().getValue(),9)
        self.assertEqual(self.stack.getMin(),2)
        self.assertEqual(self.stack.pop().getValue(),2)
