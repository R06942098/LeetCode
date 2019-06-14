class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        index = 0
        while True:
            if index == len(nums)-1:
                break
            if nums[index] != nums[index+1]:
                break
            else:
                index += 2
        return nums[index]