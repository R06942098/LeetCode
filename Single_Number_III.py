class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        index = 0 
        count = 0 
        while True: 
            if count == 2 :
                break 
            if nums.count(nums[index]) == 2 :
                index += 2 
            
            else: 
                ans.append(nums[index])
                index += 1
                count += 1 
        return ans