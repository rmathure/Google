__author__ = 'rohanmathure'


import unittest


def getMinCoins(coinArray,total,minArray=dict()):
    result=-1
    if total<0:
        return -1
    if not minArray.get(total,-99)==-99:
        return minArray[total]
    for i in coinArray:
        minArray[i]=1
    for i in coinArray:
        if not result==-1:
            if total-i>0:
                result=min(getMinCoins(coinArray,total-i)+1,result,minArray)
        else:
            temp=getMinCoins(coinArray,total-i,minArray)
            if total-i>0 and not temp == -1:
                result=temp+1
    minArray[total]=result
    return result



class TestMinCoins(unittest.TestCase):
    def test1(self):
        self.assertEqual(getMinCoins([1,2,5,10],21),3)

    def test2(self):
        self.assertEqual(getMinCoins([1,2,5,10],38),6)

    def test3(self):
        self.assertEqual(getMinCoins([1,2,5,10],8),3)

    def test4(self):
        self.assertEqual(getMinCoins([2,4],7),-1)
