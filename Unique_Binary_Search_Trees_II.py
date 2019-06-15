class Solution:
	#def generateTrees(self, n: int) -> List[TreeNode]:
	def generateTrees(self, n):
		candidate_list = [i for i in range(n)]
		if n == 0 :
			return []
		def dfs(left, right):

			### 書上也是都用此終點方式
			if left > right:
				return [None]
			### 若不是正整數則整用我的方式list[start:i]
			res = []
			for i in range(left, right+1): 
				## 此range要多加注意
				left_node = dfs(left, i-1)
				right_node = dfs(i+1, right)
				for q in left_node: 
					for k in right_node:
						node = TreeNode(i)
						node.right = k
						node.left = q
						res.append(node)
			return res
		ans = dfs(1, n)
		return ans 