class Solution(object):
    def removeZeros(self, n):
        s = ""
        while n > 0:
            rem = n % 10
            if rem != 0:
                s = s + str(rem)
            n //= 10
        s = s[::-1]
        return int(s)
