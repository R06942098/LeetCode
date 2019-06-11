# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




### ****************************
### fuck, it's somehow too slow.
### ****************************


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans = []
        def dfs(node, a=[],b=[]): 
            if not node:
                return None   
            dfs(node.left, a+["left"], b+[node.val])
            dfs(node.right, a+["right"], b+[node.val])
            if not node.left:
                if not node.right:
                    a = self.validate(a, b+[node.val])
                    ans.append(a)
        dfs(root)
        if False in ans :
            return False
        else:
            return True

        
    def validate(self, a, b):
        for i in range(len(a)):
            symbol = a[i] 
            if symbol == "right":
                if b.count(b[i]) >1:
                    return False
                
                if b[i] == min(b[i:]):
                    pass
                else:
                    return False
            else:
                if b.count(b[i]) >1:
                    return False
                
                if b[i] == max(b[i:]):
                    pass
                else:    
                    return False
        return True



















