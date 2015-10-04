__author__ = 'rohanmathure'

import unittest


class Page(object):
    def __init__(self, page_number, data):
        self.pageNumber = page_number
        self.data = data
        self.prevPage = None
        self.nextPage = None


class LRUCache(object):
    def __init__(self, maxsize):
        self.head = None
        self.maxsize = maxsize
        self.end = None
        self.pageMap = dict()

    def __set_head__(self, page):
        page.nextPage = self.head
        if self.head is not None:
            self.head.prevPage = page
        self.head = page
        page.prevPage = None

    def __remove_page__(self, page):
        if page == self.end and page == self.head:
            self.end = None
            self.head = None
            page.nextPage = None
            page.prevPage = None
        elif page == self.end:
            self.__set_end__(page.prevPage)
        elif page == self.head:
            self.__set_head__(page.nextPage)
        else:
            page.prevPage.nextPage = page.nextPage
            page.nextPage.prevPage = page.prevPage

    def __set_end__(self, page):
        page.nextPage = None
        self.end = page

    def get_page(self, page_number):
        if page_number in self.pageMap:
            page = self.pageMap[page_number]
            if not page == self.head:
                self.__remove_page__(page)
                self.__set_head__(page)
            return page
        return None

    def set_page(self, page):
        if len(self.pageMap.keys()) >= self.maxsize:
            del self.pageMap[self.end.pageNumber]
            self.__remove_page__(self.end)
        self.__set_head__(page)
        if self.end is None:
            self.__set_end__(page)
        self.pageMap[page.pageNumber] = page


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.LRU = LRUCache(3)

    def test_under_max_size(self):
        self.assertIsNone(self.LRU.get_page(1))
        page = Page(1,[])
        self.LRU.set_page(page)
        self.assertEqual(self.LRU.get_page(1), page)
        page = Page(2,[])
        self.LRU.set_page(page)
        self.assertEqual(self.LRU.get_page(2), page)
        page = Page(3,[])
        self.LRU.set_page(page)
        self.assertEqual(self.LRU.get_page(3), page)

    def test_page_request_from_cache(self):
        page = Page(1, [])
        self.LRU.set_page(page)
        page = Page(2, [])
        self.LRU.set_page(page)
        page = Page(3, [])
        self.LRU.set_page(page)
        self.LRU.get_page(2)
        self.assertEqual(self.LRU.head.pageNumber, 2)
        self.assertEqual(self.LRU.end.pageNumber, 1)

    def test_page_replace(self):
        page = Page(1, [])
        self.LRU.set_page(page)
        page = Page(2, [])
        self.LRU.set_page(page)
        page = Page(3, [])
        self.LRU.set_page(page)
        page = Page(4, [])
        self.LRU.set_page(page)
        self.assertEqual(self.LRU.head.pageNumber, 4)
        self.assertEqual(self.LRU.end.pageNumber, 2)
        self.assertEqual(len(self.LRU.pageMap), 3)
        self.assertFalse(1 in self.LRU.pageMap)
        self.assertEqual(self.LRU.get_page(2).pageNumber, 2)


class TestPageHeadAndEnd(unittest.TestCase):
    def setUp(self):
        self.LRU = LRUCache(1)

    def test_head_and_end_retrieve(self):
        self.LRU.set_page(Page(1,[]))
        self.assertEqual(self.LRU.get_page(1).pageNumber, 1)

    def test_head_and_end_replace(self):
        self.LRU.set_page(Page(1, []))
        self.LRU.set_page(Page(2, []))
        self.assertEqual(self.LRU.get_page(2).pageNumber, 2)
        self.assertEqual(self.LRU.head.pageNumber, 2)
        self.assertEqual(self.LRU.end.pageNumber, 2)
        self.assertIsNone(self.LRU.get_page(1))
