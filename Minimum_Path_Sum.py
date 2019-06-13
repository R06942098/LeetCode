class Solution(object):
	### DFS may cause time limited.....
	def minPathSum(self, grid):
		"""
		m = len(grid)
		n = len(grid[0])
		self.ans = []

		def dfs(i=0, j=0, count=0):

			if i == (m-1) and j == (n-1) : 
				self.ans.append(count+grid[i][j])
				return None 

			if i == (m-1) : 
				dfs(i, j+1, count + grid[i][j])

			elif j == (n-1) : 
				dfs(i+1, j, count + grid[i][j])

			else:
				dfs(i+1, j, count + grid[i][j])
				dfs(i, j+1, count + grid[i][j])

		dfs()
		return min(self.ans)
		"""
		#consider to use DP動態規劃, 每一格都選一從上或從左來最小的那一個 !!!
		# This is really tricky..
		m = len(grid)
		n = len(grid[0])
		
		for i in range(1,m):
			grid[i][0] = grid[i-1][0] + grid[i][0]
		for j in range(1,n):
			grid[0][j] = grid[0][j-1] + grid[0][j]
		
		for i in range(1,m):
			for j in range(1,n):
				grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])
				
		return grid[-1][-1]


b = Solution()
a = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(b.minPathSum(a))