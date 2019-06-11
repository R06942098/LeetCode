class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 :
            return []
        if numRows == 1 :
            return [[1]]
        ans = [[1],[1, 1]]
        for i in range(2, numRows):
            temp = [] 
            temp.append(1)
            for j in range(len(ans[i-1])-1):
                temp.append(ans[i-1][j]+ans[i-1][j+1])
            temp.append(1)
            ans.append(temp)
        return ans 