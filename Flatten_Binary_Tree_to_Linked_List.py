# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        val = []
        def dfs(node):
            if not node:
                return None 
            if node.left:
                val.append(node.left.val)
                dfs(node.left)
            if node.right:
                val.append(node.right.val)
                dfs(node.right)
        dfs(root)
        #print(val)
        root.left = None 
        root.right = None 
        ans = root
        for i in val : 
            ans.right = TreeNode(i)
            ans = ans.right 