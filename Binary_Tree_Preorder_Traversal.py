class Solution(object):
    def preorderTraversal(self, root):
        ## **********************
        ## Instead of using recusive in tree algortithm.
        ## We may consider iterative. 
        ## **********************

        """
        :type root: TreeNode
        :rtype: List[int]

        Input: [1,null,2,3]
               1
                \
                 2
                /
               3
        Output: [1,2,3]
        """
        
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                """
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                """
        return ret
