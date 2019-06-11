# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ### There is also another question that findst the minimum path.
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = []
        def dfs(node, count=0):
            if not node: 
                return None
            dfs(node.left, count+1)
            dfs(node.right, count+1)
            if not node.left:
                if not node.right:
                        self.ans.append(count+1)   
        dfs(root)
        return max(self.ans)