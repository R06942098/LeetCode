"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root : 
            return [] 
        ans = [] 
        ans.append([root.val])
        def dfs(node, count=2):
            if not node:
                return None 
            
            if len(ans) < count:
                ans.append([])
            
            for i in node.children:
                ans[count-1].append(i.val)
            """
            if node.children[0]:
                ans[count-1].append(node.children[0].val)
                
            if node.children[1]:
                ans[count-1].append(node.children[1].val)
                
            if node.children[2]:
                ans[count-1].append(node.children[2].val)
            """
            for i in node.children:
                dfs(i, count+1)
                
        dfs(root)
        return ans[:-1]