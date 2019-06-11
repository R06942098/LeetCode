class Solution:
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
		if not root:
			return []

		ans = [] 
		ans.append([root.val])

		"""
		def dfs(node, count = 2):

			if not node:
				return None 

			if len(ans) < count : 
				ans.append([])

			if count % 2 == 0 : 
				if node.right:
					ans[count-1].append(node.right.val)
				if node.left:
					ans[count-1].append(node.left.val)
				dfs(node.left, count+1)
				dfs(node.right, count+1)
			else: 
				if node.left:
					ans[count-1].append(node.left.val)
				if node.right:
					ans[count-1].append(node.right.val)			
				dfs(node.right, count+1)
				dfs(node.left, count+1)
			#dfs(node.left, count+1)
			#dfs(node.right, count+1)
		"""
		def dfs(node, count = 2):

			if not node:
				return None 

			if len(ans) < count : 
				ans.append([])
			if node.left:
				ans[count-1].append(node.left.val)
			if node.right:
				ans[count-1].append(node.right.val)
			dfs(node.left, count+1)
			dfs(node.right, count+1)
		dfs(root)
		ans = ans[:-1]
		ans = self.examine(ans)
		#ans.reverse()
		return ans

	def examine(self, a):
		temp = []
		for i in range(len(a)):
			if i % 2 == 0 :
				temp.append(a[i])
			else:
				a[i].reverse()
				temp.append(a[i])
		return temp







