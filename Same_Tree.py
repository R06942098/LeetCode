# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.ans_1 = []
        self.ans_2 = [] 
        
        def dfs(node, ans_list=[]):
            if not node:
                return None 
            ans_list += [node.val] 
            
            if not node.left: 
                if node.right : 
                    ans_list += ['null']
                    dfs(node.right, ans_list)
            else:
                dfs(node.left, ans_list)
                dfs(node.right, ans_list)
                
        dfs(p, self.ans_1)
        dfs(q, self.ans_2)
        print(self.ans_1)
        print(self.ans_2)
        return self.ans_1 == self.ans_2
            