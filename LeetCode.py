__author__ = 'rohanmathure'

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''

class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        retVal = 0
        power = 1
        tempVal = 0
        while True:
            tempVal = n/pow(5, power)
            if tempVal == 0:
                break
            else:
                retVal += tempVal
                power += 1
        return retVal

'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

'''

class Solution2(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        i=0
        j=0
        k=0
        while True:
            if i >= len(s1) and j >= len(s2):
                break
            if i < len(s1) and k <len(s3) and s3[k]==s1[i]:
                i += 1
            elif j < len(s2)  and k < len(s3) and  s3[k]==s2[j]:
                j += 1
            else:
                return False
            k += 1
        if k==len(s3):
            return True
        return False

sol = Solution2()
sol.isInterleave("aa","ab","aaba")