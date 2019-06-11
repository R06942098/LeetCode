class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return [] 
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children)
        #ans.reverse()
        return ans[::-1]