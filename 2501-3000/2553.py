class Solution(object):
    def separateDigits(self, A):
        return [int(c) for a in A for c in str(a)]
