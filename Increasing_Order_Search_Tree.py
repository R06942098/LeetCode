# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):
        ### whether it exists root or not? 
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    #def increasingBST(self, root: TreeNode) -> TreeNode:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        self.prev = dummy
        ## 也可以全部取出來慢慢做，但我不願意使用此easy method.
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            ## why use None ? 
            ## 此 None 為將此節點的left全部取消，因為是從屁股開始塞，所以右側的樹枝可以直接塞進去，
            ## 同時，因為指定為right =多少，故此節點是重複塞進去，所以太聰明啦！！！！！
            ## ****************************************
            node.left = None
            self.prev.right = node
            self.prev = self.prev.right
            dfs(node.right)
            """
            if node: 
                if node.left: 
                    ### Set the dummy variable.
                    dummy = TreeNode(node.right)
                    dummy.left = node.val
                    dfs(node.right)
                else: 
                    dfs(node.right)
            else: 
                return None
            """
        if root:
            dfs(root)
        return dummy.right
#[5,3,6,2,4,null,8,1,null,null,null,7,9]
root = Node(5)
root.insert(3)
root.insert(6)
root.insert(2)
root.insert(8)
root.insert(1)
root.insert(3)
root.insert(7)
root.insert(9)
root.insert(10)
root.insert(11)
root.PrintTree()
'''
print(root.data)
print(root.right.data)
print(root.right.right.data)
print(root.right.right.right.data)
print(root.right.right.left.data)
#print(root.right.left.data)

b = Solution()
c = b.increasingBST(root)
print(c.data)
print(c.right.data)
print(c.right.right.data)
print(c.right.right.right.data)
print(c.right.right.right.right.data)
print(c.right.right.right.right.right.data)
print(c.right.right.right.right.right.right.data)
print(c.right.right.right.right.right.right.right.data)
print(c.right.right.right.right.right.right.right.right.data)
count = 0 
'''


"""
newRoot=TreeNode(0)
self.p=newRoot
def InOrder(root):
    if root.left:
        InOrder(root.left)
    self.p.right=TreeNode(root.val)
    self.p=self.p.right
    if root.right:
        InOrder(root.right)
if root:
    InOrder(root)
"""


"""
def increasingBST(self, root):
    type root: TreeNode
    rtype: TreeNode

    dummy = TreeNode(-1)
    self.prev = dummy
    self.inOrder(root)
    return dummy.right
    
def inOrder(self, root):
    if not root:
        return None
    self.inOrder(root.left)
    root.left = None
    self.prev.right = root
    self.prev = self.prev.right
    self.inOrder(root.right)
"""


