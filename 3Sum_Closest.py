class Solution:
    #def threeSumClosest(self, nums: List[int], target: int) -> int:
    ### this algorithm is too slow.... (360ms)
    ### 此種雙指針的方式，好像不用遍歷每個中間元素
    def threeSumClosest(self, nums, target):
        #sorted(nums)
        #nums.sort()
        '''
        nums = sorted(nums)
        #print(nums)
        ans = []
        distance = []
        
        for i in range(len(nums)):
            j = i+1
            while j <= (len(nums)-2):
                k = len(nums) - 1
                while j < k : 
                    temp = nums[i]+nums[j]+nums[k]
                    ans.append(temp)
                    print(ans)
                    #print(ans)
                    distance.append(abs(temp - target))
                    if temp < target: 
                        break       
                    #print(k)
                    k -= 1 
                    while nums[k] == nums[k+1]:
                        if j < k: 
                            k-=1 
                        else:
                            break 
                    ### add the constraint about the boundary 
                j+=1   
                while nums[j] == nums[j-1]: 
                    if j < k : 
                        j+=1 
                    else:
                        break
        index = distance.index(min(distance))
        return ans[index]
        '''

        ### For accepted answer.... 128ms
        res = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k : 
                ans = nums[i]+nums[j]+nums[k]
                if abs(ans - target) < abs(res-target): 
                    res = ans 
                if ans > target : 
                    k -= 1
                elif ans < target: 
                    j += 1
                else: 
                    return target 
        return res 
        

a = Solution()
b = [-73,-78,-47,65,22,21,-28,-87,86,-78,-29,97,30,98,-38,-68,76,-91,70,-48,-67,-26,-52,-17,76,-21,-25,15,-58,41,47,-40,86,44,-18,47,-94,-12,52,48,-90,65,52,-2,25,-39,-18,-60,41,59,95,10,44,-65,-17,-56,47,89,33,75,0,-62,-24,22,-23,-58,52,-71,-23,-91,-13,13,100,25,-25,22,-12,-77,-37,34,-45,10,-93,-92,49,88,61,89,69,25,46,-52,64,-60,-94,-61,18,34,18,24,-73,-30,13,27,65,75,-32,34,-54,-30,20,-85,-27,48,43,-13,-85,-82,94,11,-94,0,-78,54,-95,-11,-6,-86,-80,-80,73,-71,-68,20,94,52,-50,-78,87,25,-48,94,-65,89,46,33,26,-75,55,-20,58,0,-91,1,42,90,-62,11,-28,-4,33,58,-74,85,-93,42,9,-91,18,76]
#-283
b = [1,2,4,8,16,32,64,128]
#b = [-1,2,1,-4]
#1
print(a.threeSumClosest(b, 82))





