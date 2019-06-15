class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: 
            return None
        _len = len(nums)
        mid = _len // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0 :
            return None 
        if len(nums) == 1 :
            return TreeNode(nums[0])
        
        if len(nums) == 2 : 
            root = TreeNode(nums[0])
            if nums[0] > nums[1]:
                root.left = TreeNode(nums[1])
            else:
                root.right = TreeNode(nums[1])
            return root
        ans = []
        if len(nums) % 2 != 0 : 
            n = int((len(nums)-1) / 2)
        else: 
            n = int(len(nums) / 2)
        left = nums[:n] 
        left.reverse()
        right = nums[n+1:]
        right.reverse()
        root = TreeNode(nums[n])
        root.left = TreeNode(left[0])
        root.right = TreeNode(right[0])
        ans_left = root.left
        ans_right = root.right
        left = left[1:]
        right = right[1:]
        max_len = max(len(left), len(right))
        for i in range(max_len):
            ans_left.left = TreeNode(left[i])
            ans_left = ans_left.left
            if i < len(right):
                ans_right.right = TreeNode(right[i])
                ans_right = ans_right.right
        return root
"""
