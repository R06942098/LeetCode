class Solution:
    def summaryRanges(self, nums):
        ans = []
        if len(nums) ==0 :
            return [] 
        i = 0
        while True:
            if i > len(nums)-1:
                break 
            if i == (len(nums)-1):
                ans.append(str(nums[i]))
                break
            start = nums[i] 
            qq = str(start)+'->'
            count = 0 
            while True:
                #print(i)
                if i < len(nums)-1:
                    if nums[i+1] == start+1:
                        start +=1
                        i += 1
                        count += 1
                        pass
                    else:
                        end = nums[i]
                        if end == nums[i-count] : 
                            ans.append(str(nums[i]))
                        else:
                            qq += str(end)
                            ans.append(qq)
                        i += 1 
                        break
                else:
                    end = nums[i]
                    #print(end)
                    if  end == nums[i-count]: 
                        ans.append(str(nums[i]))
                    else:
                        qq += str(end)
                        ans.append(qq)
                        i +=1
                    break
        print(ans)
        return ans 

b = Solution()
a = [0,1,2,4,7]
b.summaryRanges(a)