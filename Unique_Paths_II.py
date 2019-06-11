class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        index_list = []
        ff = False
        first_row = False
        first_column = False
        first_column_index = []
        for i in range(len(obstacleGrid)):
            if 1 in obstacleGrid[i]:
                num = obstacleGrid[i].count(1)
                temp = [i, obstacleGrid[i].index(1)]
                if i == 0:
                    if temp[1] != 0:
                        first_row = True 
                        first_row_index = temp[1]
                if temp[1] == 0: 
                    if i !=0 : 
                        first_column_index.append(i)
                        first_column = True 
                if num > 1 :
                    qq = [j for j in range(len(obstacleGrid[i])) if obstacleGrid[i][j] ==1]                         
                    for j in qq : 
                        index_list.append([i, j])
                else:
                    index_list.append([i, obstacleGrid[i].index(1)])
                ff=True
        if len(first_column_index)>0:
            first_column_index = min(first_column_index)
        
        if ff:
            pass
        else :
            index = [-1, -1]
        
        if [0,0] in index_list :
            return 0 
        
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        ans = []
        for i in range(height):
            ans.append([0 for _ in range(width)])
        
        for j in range(width):
            for i in range(height) :
                if i == 0 or j == 0:
                    if i == 0 : 
                        if first_row:
                            if j < first_row_index: 
                                ans[i][j] = 1 
                            else: 
                                ans[i][j] = 0
                        else: 
                            ans[i][j] = 1

                    else:
                        if first_column:
                            if i < first_column_index: 
                                ans[i][j] = 1 
                            else: 
                                ans[i][j] = 0
                        else:
                            ans[i][j] = 1
                    
                
                else:
                    if [i,j] in index_list:
                        pass
                    else:
                        ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[height-1][width-1]