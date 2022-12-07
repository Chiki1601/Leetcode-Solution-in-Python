class Solution:
    def numberOfCuts(self, n):
        if n == 1: return 0
        return n if n % 2 else n // 2
