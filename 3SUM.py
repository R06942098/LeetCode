class Solution:
    ### two index for intitial state and end state, then near one.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        results_list = []
        nums.sort()
        temp = []
        for i in range(length-2):
            #if i ==0 or nums[i] > nums[i-1]:
            if i ==0 or nums[i] not in temp:
                j = i+1  
                k = length -1
                while j < k :
                    if nums[j]+nums[k] == -nums[i]:
                        #results = [nums[i], nums[j], nums[k]]
                        #if results not in results_list : 
                        #    results_list.append(results)
                        temp.append(nums[i])
                        results_list.append([nums[i], nums[j], nums[k]])
                        j += 1 
                        ## 一變大另一就得變小了!
                        k -= 1 
                        while j < k and nums[j] == nums[j-1]:
                            j += 1 

                        while j < k and nums[k] == nums[k+1]:
                            k -= 1 

                    elif  nums[j]+nums[k] < -nums[i]:
                        while j < k :
                            j+=1
                            if nums[j] > nums[j-1] :
                                break
                    else : 
                        while j < k:
                            k -= 1
                            if nums[k] < nums[k+1]:
                                break
        return results_list
