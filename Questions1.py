__author__ = 'rohanmathure'
import unittest
import math

# Given a sorted array find the number of occurrence for number given

def numOfOccurences(numArray, element):
    count = int()
    i = 0
    mid = int()
    j = len(numArray)
    while i<=j >0 :
        mid = j/2
        if numArray[mid] == element:
            #Now search in both directions  for the number of occurences
            count = getAllOccurences(numArray,element,mid)
            break
        else:
            if i==j:
                break
            elif numArray[mid] > element:
                # search left
                j = mid
            else:
                # search right
                i = math.ceil((i+j)/2)
    return count


def getAllOccurences(numArray, element, position):
    count = int()
    count = count +1 #since already found
    i = position -1
    while i> 0:
        if numArray[i]==element:
            count=count+1
            i=i-1
        else:
            break
    i = position+1
    while i<len(numArray):
        if numArray[i]==element:
            count=count+1
            i=i+1
        else:
            break
    return count

class TestNumberOfOccurences(unittest.TestCase):

  def test_basic(self):
      self.assertEqual(numOfOccurences([1,2,3,4,5,5,5,5,6,7,8],5),4)
      self.assertEqual(numOfOccurences([1,2,3,3,3,4,5],3),3)

  def test_blank(self):
      self.assertEqual(numOfOccurences([],5),0)

  def test_none(self):
      self.assertEqual(numOfOccurences([1,2,3,4,4,5],6),0)
      self.assertEqual(numOfOccurences([1,3,5,7,9],6),0)


if __name__ == '__main__':
    unittest.main()