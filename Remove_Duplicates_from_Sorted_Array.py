class Solution:
    #def removeDuplicates(self, nums: List[int]) -> int:
    ### For instance: 

    """
    Given nums = [0,0,1,1,1,2,2,3,3,4]
    Your function should return length = 5, 
    with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
    It doesn't matter what values are set beyond the returned length.
    """
    def removeDuplicates(self, nums):
        ## I use the in-place algorithm 
        ## but it just needs the number of distinct value..
        index = 0
        nums.sort()
        for i in nums: 
            count = 1
            q = nums.index(i)
            count = nums.count(i)
            '''
            while True :
                if q+count < len(nums):
                    if nums[q] == nums[q+count]:
                        count += 1 
                    else: 
                        break 
                else:
                    break
            '''
            nums[index:index+count] = [i]
            #print(nums)
            index += 1
        #print(nums)
        return len(nums)

    """
    From CSDN. 
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                cur += 1
                nums[cur] = nums[i]
            print(nums)
        return cur+1

    """

b = Solution()
a = [0,0,1,1,1,2,2,3,3,4]
a = [1,1,2]
print(b.removeDuplicates(a))
