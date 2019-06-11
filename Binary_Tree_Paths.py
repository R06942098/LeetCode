class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        def dfs(node, a=''):
            if not node:
                return None
            dfs(node.left, a+str(node.val)+'->')
            dfs(node.right, a+str(node.val) +'->')
            if not node.left:
                if not node.right: 
                    ans.append(a+str(node.val))
        dfs(root)
        return ans