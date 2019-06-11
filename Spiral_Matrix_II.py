class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = []
        for i in range(n):
            ans.append([[] for _ in range(n)])
        r_lim = n
        l_lim = 1
        u_lim = 0
        b_lim = n
        count = 1
        prefix = 1
        symbol = 0
        i = 0
        j = 0 
        while True :
            #print(i,j)
            if count == n**(2):
                ans[i][j] = n**(2)
                break
            ans[i][j] = count 
            count += 1
            if prefix % 2 == 0: 
                if symbol % 2 == 0: 
                    i += 1
                    if i == (r_lim-1) : 
                        prefix += 1 
                        r_lim -= 1
                        symbol += 1
                else:
                    i -= 1
                    if i == l_lim :
                        prefix +=1
                        l_lim += 1
                        symbol += 1
            else:
                if symbol % 2 == 0:
                    j += 1
                    if j == (b_lim-1):
                        prefix += 1
                        b_lim -=1 
                        #symbol += 1
                else:
                    j -= 1        
                    if j == u_lim:
                        prefix += 1 
                        u_lim += 1 
                        #symbol += 1 
            
        return ans 