class Solution(object):
    def setZeroes(self, matrix):
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        i = []
        j = []
        store_list = [k for k in range(n)]

        for row in range(m):
        	temp = matrix[row]

        	if 0 in temp:
        		i.append(row)

        	for column in range(n):
        		if temp[column] == 0 : 
        			if column not in j :
        				j.append(column)

        for row in range(m):
        	if row in i : 
        		matrix[row] = [0 for _ in range(n)]

        	else:
        		for k in j : 
        			matrix[row][k] = 0

        return matrix

b = Solution()
a = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
a = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

a =[
[3,9,4,6,2,4,0,1,7],
[1,9,7,3,7,0,2,0,7],
[1,8,9,9,4,6,1,1,8],
[6,2,4,4,5,3,0,4,7],
[4,6,9,3,7,8,1,3,7],
[3,5,7,0,8,7,0,7,1],
[6,0,2,4,8,7,0,2,2]
]
print(b.setZeroes(a))



