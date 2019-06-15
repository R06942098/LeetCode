class Solution(object):
    def singleNumber(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        index = 0
        while True :
            if nums.count(nums[index]) == 3 :
                index += 3 
            else: 
                break 
        return nums[index]
                
        