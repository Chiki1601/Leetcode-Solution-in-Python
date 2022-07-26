class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = collections.Counter(nums)
        result = [0,0]
        for k,v in c.items():
            if v%2!=0:
                result[1] += 1
            result[0] += v//2
        return result
