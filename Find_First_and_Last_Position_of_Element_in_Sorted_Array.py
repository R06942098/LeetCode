class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums: 
            ### minimum one ... 
            a = nums.index(target)
            ans = []
            ans.append(a)
            if len(nums) == 1 : 
                return [a, a]
            else: 
                #for i in range(a+1, len(nums)):
                    #if nums[i] == target: 
                    #ans.append(i)
                num = nums.count(target)
                ans.append(a+num-1)
                #return [ans[0], ans[-1]]
                return ans 
        else: 
            return [-1,-1]