# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	#def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
	def levelOrderBottom(self, root):
		if not root:
			return []
		ans = [] 
		ans.append([root.val])
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
		print(ans)
		ans = ans[:-1]
		ans.reverse()
		return ans




		