__author__ = 'rohanmathure'
import unittest
import collections

def buildItinerary(tickets):
    ticketDict=dict()
    ticketDict,source,dest = getTicketMap(tickets)
    isDone=False
    itinerary=list()
    while not isDone:
        itinerary.append(source)
        source=ticketDict.get(source,None)
        if source==dest:
            itinerary.append(source)
            isDone=True
        if source is None:
            print "Invalid itinerary"
            itinerary=None
            isDone=True
    return itinerary

def run_length_encoding(s):
  retArray=list()
  prevChar=None
  prevCount=int()
  for char in s:
      if prevChar is None:
          prevChar=char
          prevCount=1
      elif char==prevChar:
          prevCount=prevCount+1
      else:
          retArray.append([prevCount,prevChar])
          prevChar=char
          prevCount=1
  if not prevChar is None:
    retArray.append([prevCount,prevChar])
  return retArray


def group_check(s):
    openbraces=set(['[','{','('])
    closedbraces=set([']','}',')'])
    charStack=list()
    for char in s:
        if char in openbraces:
            charStack.push(char)
        elif char in closedbraces:
            if not isvalid(char,charStack.pop()):
                return False
    if len(charStack)>0:
        return False
    else:
        return True



def isvalid(char,stackChar):
    if (char==']' and stackChar=='[') or (char=='}' and stackChar=='{') or (char==')' and stackChar=='('):
        return True
    else:
        return False


def getTicketMap(tickets):
    ticketMap=dict()
    source=None
    dest =None
    sourceSet=set()
    destSet=set()

    for ticket in tickets:
        source,dest = ticket
        ticketMap[source]=dest
        sourceSet.add(source)
        destSet.add(dest)
    source = sourceSet.difference(sourceSet.intersection(destSet)).pop()
    dest = destSet.difference(sourceSet.intersection(destSet)).pop()
    return  [ticketMap,source,dest]

class TestItinerary(unittest.TestCase):
    def testBaseCase(self):
        self.assertEqual(buildItinerary([('a','b'),('b','c'),('c','d'),('d','e')]),['a','b','c','d','e'])

from random import choice
from string import ascii_uppercase

def random_string(n):
    return ''.join(choice(ascii_uppercase) for _ in xrange(n))

class TestRunLength(unittest.TestCase):
    def inverse_rle(self,arr):
        return ''.join(c*n for n, c in arr)
    def testCase(self):
        self.assertEqual(run_length_encoding(''), [])
        self.assertEqual(run_length_encoding("abc"), [[1,'a'],[1,'b'],[1,'c']])
        self.assertEqual(run_length_encoding("aab"), [[2,'a'],[1,'b']])
        self.assertEqual(run_length_encoding("hello world!"),
                           [[1,'h'],[1,'e'],[2,'l'],[1,'o'],[1,' '],[1,'w'],[1,'o'],[1,'r'],[1,'l'],[1,'d'],[1,'!']])
        self.assertEqual(run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb"),
                           [[34,'a'], [3,'b']])
        self.assertEqual(
            run_length_encoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"),
            [[12,'W'],[1,'B'],[12,'W'],[3,'B'],[24,'W'],[1,'B'],[14,'W']]
        )




        for _ in xrange(100):
            s = random_string(20)
            self.assertEqual(self.inverse_rle(run_length_encoding(s)), s)


class TestBrackets(unittest.TestCase):
    def testBrackets(self):
        self.assertEqual(group_check("()"), True)
        self.assertEqual(group_check("({"), False)