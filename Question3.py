__author__ = 'rohanmathure'


import unittest
import math


def pow(x,n):
    ans = float()
    if n==0:
        ans= 1
    elif n<0:
        ans = 1.0/ pow(x, abs(n))
    elif n >0:
        if isinstance(n,int):
            ans = powerPositive(x,n)
        else:
            #fraction
             ans= math.exp(n*math.log(x))
    return ans

def powerPositive(x,n):
    ans = float()
    ans = 1
    while n >=1:
        ans = ans * x
        n = n-1
    return ans

class TestPower(unittest.TestCase):
    def testBaseCase(self):
        self.assertEqual(pow(3,3),27)
        self.assertEqual(pow(3,0),1)

    def testNegative(self):
        self.assertEqual(pow(2,-2),0.25)
        self.assertEqual(pow(-2,-2),0.25)
        self.assertEqual(pow(-2,-1),-0.5)

    def testFraction(self):
        self.assertEqual(pow(4,0.5),2)
        self.assertEqual(pow(16,0.25),2)