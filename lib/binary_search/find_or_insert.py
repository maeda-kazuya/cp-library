# https://leetcode.com/problems/search-insert-position/solution/

class Solution(object):
    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        while l <= r:
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = (l + r) // 2

        # return l + 1
        return l

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target)

# v1, v2 = [1,3,5,6], 5
# v1, v2 = [1,3,5,6], 7
v1, v2 = [1,3,5,6], 0
print(Solution().binary_search(v1, v2))
