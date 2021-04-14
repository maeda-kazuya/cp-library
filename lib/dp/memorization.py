'''
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
'''

class Solution(object):
    def solve(self, nums, S, idx, res, dp):
        if dp[idx][res] is not None:
            return dp[idx][res]

        if idx == len(nums):
            if res == S:
                return 1
            else:
                return 0
        else:
            # +
            plus = self.solve(nums, S, idx + 1, res + nums[idx], dp)
            # -
            minus = self.solve(nums, S, idx + 1, res - nums[idx], dp)
            dp[idx][res] = plus + minus

            return dp[idx][res]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[None] * 2001 for _ in range(len(nums)+1)]
        return self.solve(nums, S, 0, 0, dp)

# nums = [1, 1, 1, 1, 1]
# S = 3
# nums = [25,29,23,21,45,36,16,35,13,39,44,15,16,14,45,23,50,43,9,15]
# S = 32
nums = [16,40,9,17,49,32,30,10,38,36,31,22,3,36,32,2,26,17,30,47]
S = 49

print(Solution().findTargetSumWays(nums, S))


