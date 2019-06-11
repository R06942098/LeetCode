class Solution:
	#def removeElement(self, nums: List[int], val: int) -> int:
	def removeElement(self, nums, val) :
		if len(nums) == 0 :
			return len([])
		nums.sort()
		if val not in nums : 
			return len(nums)
		else: 
			q = nums.index(val)
			count = nums.count(val)
			nums[q:q+count] = ['wei']
			nums.remove('wei')
			#print(nums)
			return len(nums)
b = Solution()
a = [3,2,2,3]
c = 3
print(b.removeElement(a, c))
