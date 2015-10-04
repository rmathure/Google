__author__ = 'rohanmathure'

# Complete the function below.

import unittest


def wordpattern(pattern, input):
    pattern_match_dict = dict()
    return wordpattern_match(pattern, input, 0, 0, pattern_match_dict)


def wordpattern_match(pattern, input, pattern_index, start_index, pattern_match_dict):
    if pattern_index == len(pattern):
        if start_index == len(input):
            return 1
        else:
            return 0

    if pattern[pattern_index] in pattern_match_dict:
        for end_index in range(start_index + 1, len(input) + 1):
            if pattern_match_dict[pattern[pattern_index]] == input[start_index:end_index]:
                if wordpattern_match(pattern, input, pattern_index + 1, end_index, pattern_match_dict):
                    return 1
    else:
        for end_index in range(start_index + 1, len(input) + 1):
            pattern_match_dict[pattern[pattern_index]] = input[start_index:end_index]
            if wordpattern_match(pattern, input, pattern_index + 1, end_index, pattern_match_dict) == 1:
                return 1
            del pattern_match_dict[pattern[pattern_index]]

    return 0


class TestPattern(unittest.TestCase):
    def testPattern(self):
        #self.assertEqual(wordpattern('abba','redredredred'), 0)
        self.assertEqual(wordpattern('abba', 'redbluebluered'), 1)


