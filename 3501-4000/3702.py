from itertools import combinations
import functools
import operator

class Solution(object):
    def longestSubsequence(self, nums):
        length = len(nums)
        if nums.count(0) == length:
            return 0
        checkxor  = functools.reduce(operator.xor, nums)

        if checkxor != 0:
            return length
        else:
            return length - 1
