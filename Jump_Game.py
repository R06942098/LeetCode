class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		reach = 0
		for i, num in enumerate(nums):
			if i > reach:
				return False
			reach = max(reach, i + num)
		return True

	### This is my implementation, but it's fail due to the time limit constraint.
	def canJump(self, nums: List[int]) -> bool:
		if len(nums)==1:
			return True 
		ans = []
		def dfs(num, index=0): 
			if index > (len(nums)-1):
				return None 
			if index == (len(nums)-1):
				ans.append(True)
				return None 
			if nums[index] == 1 :
				dfs(nums[index+1], index+1)
			else:
				for i in range(1, nums[index]+1):
					if index +i < len(nums):
						dfs(nums[index+i], index+i)
		dfs(nums)
		if True in ans:
			return True 
		else: 
			return False
			
