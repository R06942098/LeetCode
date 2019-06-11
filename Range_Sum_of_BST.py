class Solution:
    ### Too slow...... 32%...
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        qq = []
        def dfs(node): 
            if not node :
                return None 
            temp = node.val
            if temp >= L:
                if temp <= R:
                    qq.append(temp)
            dfs(node.left)
            dfs(node.right) 
        dfs(root)
        return sum(qq)