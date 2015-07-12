__author__ = 'rohanmathure'

import unittest
from LinkedListCreator import LinkedListCreator


class AddLinkedList:
    def __init__(self):
        self.__list1__=list()
        self.__list2__=list()

    def setList1(self,list1):
        self.__list1__=list1

    def setList2(self,list2):
        self.__list2__=list2

    def convertListToNumber(self,numList):
        count=0
        value=0
        while not numList is None:
            value = value+numList.getValue()*(10**count)
            count += 1
            numList=numList.getNext()
        return value

    def numToList(self,num):
        retList=[]
        currentNum=int()
        while True:
            currentNum=num%10
            num=num/10
            if currentNum==0 and num==0:
                break
            else:
                retList.append(currentNum)
        linkedList=LinkedListCreator()
        linkedList.setArray(retList)
        return linkedList.getLinkedList()

    def getSumList(self):
        num1= self.convertListToNumber(self.__list1__)
        num2=self.convertListToNumber(self.__list2__)
        return self.numToList(num1+num2)

class TestSum(unittest.TestCase):
    def Test1(self):
        linkedList=LinkedListCreator()
        linkedList.setArray([1,2,3])
        linkedList1=linkedList.getLinkedList()
        linkedList.setArray([3,4,5])
        linkedList2=linkedList.getLinkedList()
        addLinkedList=AddLinkedList()
        addLinkedList.setList1(linkedList1)
        addLinkedList.setList2(linkedList2)
        linkedList.setArray([8,6,4])
        sumList=addLinkedList.getSumList()
        self.assertEqual(sumList.getValue(),4)
        self.assertEqual(sumList.getNext().getValue(),6)
        self.assertEqual(sumList.getNext().getNext().getValue(),8)

