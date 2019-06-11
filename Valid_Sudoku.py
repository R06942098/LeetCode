class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        a = self.transpose(board)
        for i in range(9): 
            for j, k in zip(board[i], a[i]) : 
                if j == "." :
                    pass
                else:
                    if board[i].count(j) > 1 :
                        return False
                if k == ".":
                    pass
                else : 
                    if a[i].count(k) > 1 :
                        
                        return False
        for i in range(0, 9, 3): 
            for j in range(0, 9, 3):
                temp = [] 
                for k in range(j, j+3):
                    temp += board[k][i:i+3]
                for q in temp: 
                    
                    if q ==".":
                        pass
                    else:
                        if temp.count(q) > 1:
                            return False    
                    
        return True 
                            
    def transpose(self, board):
        a = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                a[i].append(board[j][i])
        return a 