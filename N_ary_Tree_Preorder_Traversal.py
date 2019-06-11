"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return [] 
        ans = []
        stack = [root]
        while stack : 
            node = stack.pop()
            ans.append(node.val)
            ### for longer the list.. differtiate from append.
            stack.extend(node.children[::-1])
        return ans
