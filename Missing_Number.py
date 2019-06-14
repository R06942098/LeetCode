class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = (1+len(nums)) * len(nums) /2
        b = sum(nums)
        return a - b
        