class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def inorder(root):

            if root == None:
                return None

            if root.left != None:
                inorder(root.left)

            answer.append(root.val)
            
            if root.right != None:
                inorder(root.right)

        inorder(root)
        return answer