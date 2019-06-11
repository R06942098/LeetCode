# ****************
# This way is for find path.... but it's too slow.
# ****************
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = []
        path_list = ['Right', 'Down']
        def rec(i = 1, j = 1, path=[]):
            if i == m :
                if j == n:
                    ans.append(path)
                    return None     
            if i == m:
                rec(i, j+1, path+['down'])
                
            elif j == n :
                rec(i+1, j, path+['right'])
                
            else:
                for q in path_list:
                    if q == 'Down':
                        rec(i, j+1, path+['down'])
                    else:
                        rec(i+1, j, path+['right'])
        rec()
        return len(ans)
b = Solution()
print(b.uniquePaths(23,12))

# ****************
# 動態轉移方程式....
# 排列數必用，超鬧，實在不懂這是什麼演算法.....邏輯思考?
# ****************
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = []
        for i in range(n):
            ans.append([0 for _ in range(m)])

        for i in range(n):
            for j in range(m):
                if i ==0 or j==0:
                    ans[i][j]=1

                else:
                    ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[m-1][n-1]



