__author__ = 'rohanmathure'



import fileinput

class MyHashtable:

    def __init__(self,num):
        self.entryNum = num
        self.entryList = [None] * num

    def put(self, k, v):
        found=False
        if k is None or v is None:
            return
        try:
            hashValue=hash(k) % self.entryNum
            if self.entryList[hashValue] is None:
                self.entryList[hashValue]=[[k,v]]
            else:
                for entry in self.entryList[hashValue]:
                    if entry[0]==k:
                        entry[1]=v
                        found=True
                if not found:
                    self.entryList[hashValue].append([k,v])
        except Exception:
            return

    def get(self, k):
        hashValue = hash(k)%self.entryNum
        if not self.entryList[hashValue] is None:
            for key,value in self.entryList[hashValue]:
                if k==key:
                    return value
        return None

if __name__ == "__main__":
    hashtable = MyHashtable(100)
    for line in fileinput.input():
        line = line.strip()
        k, v = line.split('=') if '=' in line else (line, None)
        if v:
            hashtable.put(k, v)
        else:
            print str(hashtable.get(k)).replace('None', 'null')




import unittest

class TestHash(unittest.TestCase):

    def setUp(self):
        self.hashTable = MyHashtable(100)

    def testHash(self):
        self.hashTable.put(2,'a')
        self.hashTable.put(2,'b')
        self.assertEqual(self.hashTable.get(2),'b')



def isPrime(n):
    if n<2:
        return False
    i =2
    while i<n:
        if n%i==0:
            return False
        else:
            i+=1
    return True

def  getNumberOfPrimes(n):
    cnt=0
    for i in range(1,n+1):
        if isPrime(n):
            cnt+=1
    return cnt

import unittest

class TestPrime(unittest.TestCase):
    def testPrime(self):
        self.assertEqual(getNumberOfPrimes(100),25)