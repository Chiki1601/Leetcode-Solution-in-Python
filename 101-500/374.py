# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n
        while left<=right:
            mid = (left+right)/2
            gues = guess(mid)
            if gues == 0:
                return mid
            if gues == -1:
                right = mid -1
            if gues == 1:
                left = mid+1
        return -1
