class Solution:
    ### if all the number in the list are different ..
    def permute(self, nums):
        res = []
        def dfs(nums=nums, path=[]):
            ### for empty list ....
            if not nums: 
                if path not in res: 
                    ### avoid duplicate list.
                    res.append(path) 
            else : 
                for i in range(len(nums)):
                    dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        
        dfs()
        print(res)
        return res 
b = Solution()
b.permute([1,2,3])
    