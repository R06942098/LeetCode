#import sys
#sys.setrecursionlimit(1000000)
class Solution:
    def generateParenthesis(self, n):
        ans = []
        #left = ['(', ')']
        """
        Recursive is not a good way to implement. But the problem of permutation need it...
        How to insert the () ? 想法有到位，但是自己寫的解法不夠好..
        """
        def dfs(left, right, path=''):
            if right == 0 and left == 0:
                ans.append(path) 
                ### May give the ouput to reduce computation.
                return 
            if left > 0 :
                dfs(left - 1, right, path + '(')

            if left < right : 
                dfs(left , right-1, path + ')')
                
        dfs(n,n)
        return ans 
a = 3
b = Solution()
print(b.generateParenthesis(3))
"""
n = 3 
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""