__author__ = 'rohanmathure'

import unittest

'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.


'''
class Solution(object):
    def __init__(self):
        self.pow_dict = {100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion",
                         1000000000000: "Trillion"}
        self.num_dict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6:"Six", 7:"Seven",
                         8:"Eight", 9:"Nine", 10:"Ten",11:"Eleven", 12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",
                         16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty",
                         50:"Fifty",60:"Sixty",70:"Seventy",
                    80:"Eighteen",90:"Ninety"}


    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        q = 0
        r = 0
        output = ""
        if num in self.num_dict:
            return self.num_dict[num]

        for i in sorted(self.pow_dict.keys(), reverse=True):
            if num/i > 0:
                q = int(num/i)
                r = num%i
                break
        if q > 0:
            output = self.numberToWords(q) + " " + self.pow_dict[i] + " " + self.numberToWords(r)
        else:
            q = num/10
            r = num%10
            if q < 2:
                output = self.num_dict[q]
            else:
                output = self.num_dict[q*10] + " " + self.num_dict[r]
        return output

class TestNumberToString(unittest.TestCase):
    def test_base(self):
        self.assertEqual(Solution().numberToWords(123), "One Hundred Twenty Three")
