class Solution(object):
    def findNumbers(self, nums):
        c=0
        for i in nums:
            if len(str(i))%2==0:
                c+=1
        return c
        """
        :type nums: List[int]
        :rtype: int
        """
        
