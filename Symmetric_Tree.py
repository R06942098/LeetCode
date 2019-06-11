# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	#def isSymmetric(self, root: TreeNode) -> bool:


	def isSymmetric(self, root):
		ans = []

		if not root :
			return False

		if not root.left:
			if not root.right:
				return True 
		def dfs(node, path=[]):
			if not node:
				return None 
			dfs(node.left, path+[node.val, 1])
			dfs(node.right, path+[node.val, 0])
			if not node.left:
				if not node.right:
					ans.append(path+[node.val])
		dfs(root)
		#print(ans)
		#print(self.validate(ans))
		return self.validate(ans)
	
	def validate(self, ans):
		if len(ans) %2 != 0 :
			return False
		b = int(len(ans)/2)
		for i in range(0, b):
			temp = ans[i]
			temp_1 = ans[len(ans)-i-1]
			#print(i)
			if len(temp) != len(temp_1):
				return False
			else:
				for j in range(len(temp)):
					if j % 2 ==1:
						if abs(temp[j]-temp_1[j]) :
							pass
						else:
							#print(j)
							#print("Error")
							return False
					else:
						if temp[j] == temp_1[j]:
							pass
						else:
							return False
		return True