__author__ = 'rohanmathure'

import unittest

'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

'''

class Solution(object):
    def __init__(self):
        self.operators = set(['+','-','*'])

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operator_list = list()
        num_list = list()
        temp_str = str()
        for char in input:
            if char in self.operators:
                num_list.append(temp_str)
                temp_str = ""
                operator_list.append(char)
            else:
                temp_str += char
        if len(temp_str) > 0:
            num_list.append(temp_str)
        return self.parseInput(num_list, operator_list)

    def compute(self, a, b, op):
        if op == '+':
            return int(a)+int(b)
        elif op == '-':
            return int(a)-int(b)
        elif op == '*':
            return int(a)*int(b)

    def parseInput(self, num_list, operator_list):
        output = list()
        if len(num_list) == 0:
            return []
        elif len(num_list) == 1:
            return [int(num_list[0])]
        elif len(num_list) == 2:
            return [self.compute(num_list[0], num_list[1], operator_list[0])]
        else:
            output = map(lambda x: self.compute(num_list[0], x, operator_list[0])
                                , self.parseInput(num_list[1:], operator_list[1:]))
            output.extend(map(lambda x: self.compute(self.compute(num_list[0], num_list[1], operator_list[0]), x, operator_list[1])
                                , self.parseInput(num_list[2:], operator_list[2:])))
            return output


class TestDifferentWays(unittest.TestCase):
    def test_base(self):
        self.assertEqual(Solution().diffWaysToCompute("0"), [0])

    def test_two_num(self):
        self.assertEqual(Solution().diffWaysToCompute("1+0"), [1])

    def test_multiple(self):
        self.assertEqual(Solution().diffWaysToCompute("15-7*6+24"), [-195,-51,-3,72,240])
