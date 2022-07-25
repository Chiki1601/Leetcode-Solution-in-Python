class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        for i in range(1, N+1):
            if s[-i] == '1':
                a = int(s[-i:], 2)
                if a > k:
                    return s[:-i+1].count('0') + (i-1)
        return len(s)
