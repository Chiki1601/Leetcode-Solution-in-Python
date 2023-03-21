class Solution(object):
    def findSmallestInteger(self, A, k):
        count = Counter(a % k for a in A)
        stop = 0
        for i in range(k):
            if count[i] < count[stop]:
                stop = i
        return k * count[stop] + stop
