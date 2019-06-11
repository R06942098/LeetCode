class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None 
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        return root 