class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## Maybe more faset...
        n = len(nums)
        if target > max(nums):
            nums.append(target)
        elif target < min(nums):
            nums = [target] + nums
        elif target <= min(nums):
            nums = [target] + nums
        elif target >= max(nums):
            nums.append(target)
        else :
            for i in range(0, n):
                print(i)
                if target > nums[i] : 
                    if target < nums[i+1] :
                        nums = nums[:i+1] + [target] + nums[i+1:]
                        break
                    if target <= nums[i+1]:
                        nums = nums[:i+1] + [target] + nums[i+1:]
                        break
                if target >= nums[i]: 
                    if target < nums[i+1]:
                        nums = nums[:i] + [target] + nums[i:]
                        break 
                    elif target <= nums[i+1]:
                        nums = nums[:i] + [target] + nums[i:]
                        break 
                        
                '''
                if target >= nums[i]:
                    if target < nums[i+1]:
                        nums = nums[:i] + [target] + nums[i:]
                        break
                    elif target <= nums[i+1]:
                        nums = nums[:i] + [target] + nums[i:]
                        break
                    else: 
                        break
                '''    
        print(nums)
        return nums.index(target)
                        