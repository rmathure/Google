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