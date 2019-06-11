class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.digits = (list(digits))
        self.digits
        print(self.digits)
        self.res = []
        dic = dict()
        dic['1'] = ' '
        dic['0'] = ' '
        dic['2'] = 'abc'
        dic['3'] = 'def'
        dic['4'] = 'ghi'
        dic['5'] = 'jkl'
        dic['6'] = 'mno'
        dic['7'] = 'pqrs'
        dic['8'] = 'tuv'
        dic['9'] = 'wxyz'
        
        ### This is my first attemp to the dfs .... example for all permutation .. binary tree.
        def dfs(digits=self.digits, cur='', count=0): 
            if count == (len(digits)):
                self.res.append(cur)
            else: 
                if count < len(digits):
                    for i in dic[digits[count]]: 
                        dfs(digits, cur+i, count+1)
        if len(digits) == 0 : 
            return []
        else: 
            dfs()
        return self.res