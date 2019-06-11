class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = [] 
        def dfs(node, a=[], b=0):
            if not node : 
                return None
            dfs(node.left, a + [node.val], b + node.val)
            dfs(node.right, a + [node.val], b + node.val)
            if not node.left:
                if not node.right:
                    b += node.val
                    if b == sum:
                        ans.append(a+[node.val])
            
        dfs(root)
        return ans