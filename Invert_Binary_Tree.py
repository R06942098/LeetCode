# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Input 

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''
### Google's examination ...., but I can not do it well so far..

class Solution:

    #def invertTree(self, root: TreeNode) -> TreeNode:
    """
    def invertTree(self, root):
        if not root :
            return root

        def dfs(node):  
            if not node : 
                return root
            #tmp = node.left
            node.left = dfs(node.right)
            node.right = dfs(node.left)
            return node

        k = dfs(root)
        return k 
    """

    def invertTree(self, root):

        if root is None:
            return None

        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        
        return root





     