class Solution(object):
    def jump(self, nums):
        ans = 0
        n = len(nums)
        currEnd = 0
        currFarthest = 0
        for i in range(n-1):
            currFarthest = max(currFarthest, i + nums[i])
            if i == currEnd:
                ans += 1
                currEnd = currFarthest
    
        return ans
