__author__ = 'rohanmathure'


import unittest


def maxSumSubsequence(numArray):
    maxSum=list()
    if len(numArray)>0:
        maxSum =numArray[0]
    for i in range(len(numArray)):
        maxSum=max(numArray[i])


class TestMaxSubSequence(unittest.TestCase):
    def testBase(self):
        self.assertEqual(maxSumSubsequence([3,1,-5,-6,7,1,8,0,-5,9,-2,-3,1]),20)