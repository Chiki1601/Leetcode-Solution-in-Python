class Solution(object):
    def checkPowersOfThree(self, n):
        while n > 0: 
            if n % 3 == 2: 
                return False
            n = n // 3
        return (True if n == 0 else False)
        """
        :type n: int
        :rtype: bool
        """
        
