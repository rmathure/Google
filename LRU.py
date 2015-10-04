__author__ = 'rohanmathure'

import unittest
from collections import OrderedDict
import calendar
import time


class Page:

    def __init__(self, pageNumber, data):
        self.pageNumber = pageNumber
        self.data = data


class LRU:

    def __init__(self, size):
        self.maxSize = size
        self.timestampPage = OrderedDict()
        self.pageTimeStamp = dict()

    def request(self, pageNumber):
        if pageNumber in self.pageTimeStamp.keys():
            time = self.pageTimeStamp[pageNumber]
            del self.timestampPage[time]
            self.addPage(pageNumber)
        else:
            if len(self.pageTimeStamp.keys()) < self.maxSize:
                self.addPage(pageNumber)
            else:
                key,value = self.timestampPage.items()[0]
                del self.pageTimeStamp[value]
                del self.timestampPage[key]
                self.addPage(pageNumber)

    def addPage(self, pageNumber):
            timeNow = calendar.timegm(time.gmtime())
            self.timestampPage[timeNow] = pageNumber
            self.pageTimeStamp[pageNumber] = timeNow


class TestLRU(unittest.TestCase):
    def setUp(self):
        self.LRU = LRU(3)

    def test_request_under_limit(self):
        self.LRU.request(3)
        self.assertTrue(3 in self.LRU.pageTimeStamp.keys())
        self.assertTrue(3 in self.LRU.timestampPage.values())
        self.LRU.request(4)
        self.assertTrue(4 in self.LRU.pageTimeStamp.keys())
        self.assertTrue(4 in self.LRU.timestampPage.values())
        self.assertEqual(len(self.LRU.pageTimeStamp.keys()), 2)
        self.LRU.request(5)
        self.assertTrue(5 in self.LRU.pageTimeStamp.keys())
        self.assertTrue(5 in self.LRU.timestampPage.values())
        self.assertEqual(len(self.LRU.pageTimeStamp.keys()), 3)

    def test_request_limit_repeat(self):
        self.LRU.request(3)
        self.LRU.request(4)
        self.LRU.request(5)
        self.LRU.request(4)
        self.assertTrue(4 in self.LRU.pageTimeStamp.keys())
        self.assertTrue(4 in self.LRU.timestampPage.values())
        self.assertEqual(len(self.LRU.pageTimeStamp.keys()), 3)

    def test_request_limit_no_repeat(self):
        self.LRU.request(3)
        self.LRU.request(4)
        self.LRU.request(5)
        self.LRU.request(4)
        self.LRU.request(6)
        self.assertTrue(6 in self.LRU.pageTimeStamp.keys())
        self.assertTrue(6 in self.LRU.timestampPage.values())
        self.assertEqual(len(self.LRU.pageTimeStamp.keys()), 3)

