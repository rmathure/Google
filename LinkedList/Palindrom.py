__author__ = 'rohanmathure'

import unittest
from Node import Node


class PalindromCheck:
    def __init__(self):
        self.__value__ = Node()

    def getValue(self):
        return self.__value__

    def setValue(self, value):
        self.__value__ = value

    def isPalindrome(self):
        firstPointer = None
        lastPointer = None
        stack = list()
        if self.__value__ is None:
            return False
        lastPointer = self.__value__
        while True:
            stack.append(lastPointer)
            if lastPointer.getNext() is None:
                break
            else:
                lastPointer = lastPointer.getNext()
        lastPointer = len(stack) - 1
        for i in range(len(stack)):
            if i > lastPointer:
                break
            if stack[i].getValue() == stack[lastPointer].getValue():
                lastPointer -= 1
            else:
                return False
        return True


class TestPalindromeFalse(unittest.TestCase):
    def setUp(self):
        self.palindrome = PalindromCheck()
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node5 = Node()
        node6 = Node()
        node1.setValue(1)
        node1.setNext(node2)
        node2.setValue(2)
        node2.setNext(node3)
        node3.setValue(3)
        node3.setNext(node4)
        node4.setValue(4)
        node4.setNext(node5)
        node5.setValue(5)
        node5.setNext(node6)
        node6.setValue(6)
        self.palindrome.setValue(node1)

    def TestPalindromeFalse(self):
        self.assertFalse(self.palindrome.isPalindrome())


class TestPalindromeTrue(unittest.TestCase):
    def setUp(self):
        self.palindrome = PalindromCheck()
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node5 = Node()
        node6 = Node()
        node1.setValue(1)
        node1.setNext(node2)
        node2.setValue(2)
        node2.setNext(node3)
        node3.setValue(3)
        node3.setNext(node4)
        node4.setValue(3)
        node4.setNext(node5)
        node5.setValue(2)
        node5.setNext(node6)
        node6.setValue(1)
        self.palindrome.setValue(node1)

    def TestPalindromeTrue(self):
        self.assertTrue(self.palindrome.isPalindrome())
