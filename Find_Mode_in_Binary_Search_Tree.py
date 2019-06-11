class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        temp = [] 
        count = dict()
        #counter = collections.Counter()
        def dfs(node):
            if not node : 
                return None 
            if node.val in count.keys():
                count[node.val] +=1 
            else:
                count[node.val] = 1 
            #counter[node.val] += 1 
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if not root :
            return []
        maxn = max(count.values())
        '''
        res = []
        for item, c in counter.items():
            if c == maxn:
                res.append(item)
        '''
        ans = []
        for i in count.keys():
            if count[i] == maxn:
                ans.append(i)
        return ans