class Solution:
    ## First transpose and reverse.
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        ans = []
        for i in matrix: 
            ans.append(i)
        count = 0
        for i in range(len(matrix)):
            count_1 = 0
            for j in range(len(matrix)):
                #ans[i].append(matrix[(-1*j)-1][count])
                print(ans[-3][count])
                matrix[i][count_1] = ans[(-1*j)-1][count]
                count_1 += 1 
            count += 1 
        '''
        ## Firse transpose the matrix: 
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
                
        print(matrix)