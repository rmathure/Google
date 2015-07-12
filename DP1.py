__author__ = 'rohanmathure'
import unittest

def getZigZag(numArray):
    if len(numArray) ==1 :
        return 1
    elif len(numArray)==2:
        if numArray[1]-numArray[0] != 0:
            return 2
        else:
            return 0
    else:
        if (numArray[len(numArray)-1]-numArray[len(numArray)-2]<0 and numArray[len(numArray)-2]-numArray[len(numArray)-3]>0) or (numArray[len(numArray)-1]-numArray[len(numArray)-2]>0 and numArray[len(numArray)-2]-numArray[len(numArray)-3]<0):
            return 1+ getZigZag(numArray[:-1])
        else:
            return 0+getZigZag(numArray[:-1])

def getZigZagDP(numArray):
    lengthArray=list()

    if len(numArray) >= 1 :
        lengthArray.append(numArray[0])
    if len(numArray)>=2:
        if numArray[1]-numArray[0] != 0:
            lengthArray.append(numArray[1])
    if len(numArray)<=2:
        return len(lengthArray)

    for i in range(2,len(numArray)):

        if (numArray[i]-lengthArray[-1]<0 and lengthArray[-1]-lengthArray[-2]>0) or (numArray[i]-lengthArray[-1]>0 and lengthArray[-1]-lengthArray[-2]<0):
            lengthArray.append(numArray[i])
    print lengthArray
    return len(lengthArray)


class TestZigZagDP(unittest.TestCase):
    def test1(self):
        self.assertEqual(getZigZagDP([1, 7, 4, 9, 2, 5]),6)

    def test2(self):
        self.assertEqual(getZigZagDP([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]),7)

    def test3(self):
        self.assertEqual(getZigZagDP([44]),1)

    def test4(self):
        self.assertEqual(getZigZagDP([1, 2, 3, 4, 5, 6, 7, 8, 9]),2)

    def test5(self):
        self.assertEqual(getZigZagDP([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]),8)

    def test6(self):
        self.assertEqual(getZigZagDP([374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
249, 22, 176, 279, 23, 22, 617, 462, 459, 244]),36)

    def test7(self):
        self.assertEqual(getZigZagDP([400,105,106,104,107,103,108,102,109,101,110,200,220,8,10]),13)



class TestZigZag(unittest.TestCase):
    def test1(self):
        self.assertEqual(getZigZag([1, 7, 4, 9, 2, 5]),6)

    def test2(self):
        self.assertEqual(getZigZag([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]),7)

    def test3(self):
        self.assertEqual(getZigZag([44]),1)

    def test4(self):
        self.assertEqual(getZigZag([1, 2, 3, 4, 5, 6, 7, 8, 9]),2)

    def test5(self):
        self.assertEqual(getZigZag([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]),8)

    def test6(self):
        self.assertEqual(getZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
249, 22, 176, 279, 23, 22, 617, 462, 459, 244]),36)

    def test7(self):
        self.assertEqual(getZigZag([400,105,106,104,107,103,108,102,109,101,110,200,220,8,10]),13)