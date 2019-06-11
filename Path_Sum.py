# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        ans = []
        def dfs(node, path = []):
            
            if not node:
                return None 
            
            dfs(node.left, path + [node.val])
            dfs(node.right, path + [node.val])
            
            if not node.left:
                if not node.right:
                    temp = path + [node.val]
                    temp_sum = sum(temp)
                    if temp_sum == target: 
                        ans.append(temp)
        dfs(root)
        if len(ans) >= 1:
            return True
        else:
            return False
            
            
            