class Solution:
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        shape = len(matrix) * len(matrix[0])
        ans = []
        r_lim = len(matrix)
        l_lim = 1
        u_lim = 0
        b_lim = len(matrix[0])
        count = 1
        prefix = 1
        symbol = 0
        i = 0
        j = 0 
        while True :
            print(i,j)
            print(ans)
            print(count)
            if count == shape:
                ans.append(matrix[i][j])
                break
            ans.append(matrix[i][j])
            count += 1
            if prefix % 2 == 0: 
                if symbol % 2 == 0: 
                    if r_lim == 1 : 
                        prefix += 1
                        b_lim -=1 
                        j += 1
                        continue     

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

                    if b_lim == 1 : 
                        prefix += 1
                        b_lim -=1 
                        i += 1
                        continue

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
        #print(ans)
        return ans 
b = Solution()
a = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
a = [[3],[2]]
a = [[3,2]]
b.spiralOrder(a)