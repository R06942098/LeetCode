class Solution:     
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
        ans = ans[:-1]
        return self.mean(ans)
    
    def mean(self, a):
        temp = []
        for i in a :
            temp.append((sum(i)/len(i)))
        return temp 