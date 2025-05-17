class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # nums = nums.sort()
        # return nums
        for i in range (len(nums)):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
