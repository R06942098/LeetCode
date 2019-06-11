class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: 
            return ''
        ans = str(t.val)
        if t.left or t.right: 
            ans += '(' + self.tree2str(t.left) + ')'

        if t.right: 
            ans += '(' + self.tree2str(t.right) + ')'

        return ans

"""
class Solution:
    def tree2str(self, t):
        '''
        :type t: TreeNode
        :rtype: str
        '''
        if not t:
            return ''
        if not t.left and not t.right:
            return str(t.val)

        if not t.left:
            return str(t.val) + '()' + '(' + self.tree2str(t.right) + ')'

        if not t.right:
            return str(t.val) + '(' + self.tree2str(t.left) + ')'

        return str(t.val) + '(' + self.tree2str(t.left) + ')' + '(' + self.tree2str(t.right) + ')'

"""