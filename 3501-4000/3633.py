class Solution:
    def earliestFinishTime(self, a, b, c, d):
        ans = float('inf')
        # take land first

        n = len(a)
        minEnd = float('inf')
        for i in range(n):
            minEnd = min(minEnd, a[i] + b[i])
        m = len(c)

        for i in range(m):
            ans = min(ans, d[i] + max(minEnd, c[i]))

        # take water first
        minEnd = float('inf')
        for i in range(m):
            minEnd = min(minEnd, c[i] + d[i])

        for i in range(n):
            ans = min(ans, b[i] + max(minEnd, a[i]))

        return ans
