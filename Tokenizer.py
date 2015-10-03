__author__ = 'rohanmathure'



def tokenizer(inputStr):
    curentmode = 0
    retArray= list()
    stringTemp = str()
    oppDict={1:')',2:'}',3:']'}
    mode ={'(':1,'{':2,'[':3}
    tokenList = list()


def tokenizer(stringInput):
    curentmode = 0
    retArray= list()
    stringTemp = str()
    oppDict={1:')',2:'}',3:']'}
    mode ={'(':1,'{':2,'[':3}
    for i in range(len(stringInput)):
        if curentmode == 0:
            if stringInput[i] in mode.keys():
                if not stringInput[i+1]==stringInput[i]:
                    retArray.append(stringTemp)
                    stringTemp = ""
                    curentmode = mode[stringInput[i]]
                else:
                    stringTemp += stringInput[i]
                    i += 1
            else:
                stringTemp += stringInput[i]
        else:
            if stringInput[i] == oppDict[curentmode]:
                if (not i == len(stringInput) and i+1 < len(stringInput)) and not stringInput[i+1]==stringInput[i]:
                    retArray.append(stringTemp)
                    stringTemp = ""
                    curentmode = 0
                else:
                    stringTemp += stringInput[i]
            else:
                stringTemp += stringInput[i]
    if len(stringTemp) > 0:
        retArray.append(stringTemp)
    return retArray

import unittest


class TestTokenizer(unittest.TestCase):
    def test_basic_token(self):
        self.assertEqual(tokenizer("abc(cde)efg[ght]hdh{hdjd}"), ['abc', 'cde', 'efg', 'ght', 'hdh', 'hdjd'])

    def test_escape_token(self):
        self.assertEqual(tokenizer("abc((efg(cde)abc"), ['abcefg', 'cde', 'abc'])

    def test_token_inside_token(self):
        self.assertEqual(tokenizer("abc(abc(abc(bcd)nsnj)"), ['abc', 'abcabcbcd', 'nsnj'])
        self.assertEqual(tokenizer("abc(bgh{[gh)bcd"), ['abc', 'bghgh', 'bcd'])
        self.assertEqual(tokenizer("abc{bgh}}ghj}kl"),['abc', 'bghghj', 'kl'])