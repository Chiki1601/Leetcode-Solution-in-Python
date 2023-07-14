class Solution:
    def longestSubsequence(self, nums, difference):
        dp = {}
        max_length = 1

        for num in nums:
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1

            max_length = max(max_length, dp[num])

        return max_length
