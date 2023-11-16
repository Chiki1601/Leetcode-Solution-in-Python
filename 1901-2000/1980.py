class Solution(object):
    def findDifferentBinaryString(self, nums):
        result = ""

        for i in range(len(nums)):
            result += '1' if nums[i][i] == '0' else '0'

        return result
        
