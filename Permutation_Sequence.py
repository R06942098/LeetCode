class Solution(object):
	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		### dfs can not find the best solution .......

		ss = self.fac(n)

		k = k % ss 
		if k == 0:
			k = ss 
		q = [(i+1) for i in range(n)]

		if len(q) == 1 : 
			return str(q[0])

		self.count = 0
		self.ans = [] 
		def dfs(a, q=''):
			if len(a) == 0 : 
				self.ans.append(q)
				self.count += 1 
				if self.count == k: 
					print(q)
					self.ans.append(q)
					return None

			for i in range(len(a)):
				dfs(a[:i] + a[i+1:], q+str(a[i]))
		dfs(q)
		print(self.ans)
		return self.ans[0]

	def fac(self, n):
		if n == 1 : 
			return 1
		else: 
			return n * self.fac(n-1)


b = Solution()
n = 3
k = 3
print(b.getPermutation(n, k))