class Solution:
    def intToRoman(self, num: int) -> str:
        
        dict = {}
        dict['I'] = 1 
        dict['V'] = 5 
        dict['X'] = 10 
        dict['L'] = 50 
        dict['C'] = 100 
        dict['D'] = 500
        dict['M'] = 1000 
        dict['IV'] = 4
        dict['IX'] = 9 
        dict['XL'] = 40 
        dict['XC'] = 90
        dict['CD'] = 400 
        dict['CM'] = 900 
        k = dict.keys()
        v = dict.values() 
        d = {} 
        for i, j in zip(k, v):
            d[j] = i 
        
        res = '' 
        if len(str(num))== 4 : 
            # Must above than 1000: 
            ind = num // 1000
            for _ in range(ind):
                res += d[1000]
                num -= 1000 
                
        if len(str(num)) == 3 : 
            if num >= 900: 
                res += d[900] 
                num -= 900 
                
            if num >= 500 :
                res += d[500]
                num -= 500 
            
            if num >= 400 and num < 500 : 
                res += d[400]
                num -= 400 
            
            if num <400 and num >= 100 : 
                
                ind = num // 100 
                for _ in range(ind) : 
                    res += d[100]
                    num -= 100 
        if len(str(num)) == 2 : 
            if num >= 90: 
                res += d[90] 
                num -= 90 
                
            if num >= 50 :
                res += d[50]
                num -= 50 
            
            if num >= 40 and num < 50 : 
                res += d[40]
                num -= 40
            
            if num <40 and num >= 10 : 
                
                ind = num // 10 
                for _ in range(ind) : 
                    res += d[10]
                    num -= 10
        
        if len(str(num)) == 1 : 
            if num >= 9: 
                res += d[9] 
                num -= 9 
                
            if num >= 5 :
                res += d[5]
                num -= 5
            
            if num >=4 and num <5: 
                res += d[4]
                num -= 4
            
            ind = num // 1
            for _ in range(ind):
                res +=d[1]
                num -= 1
        
        print(num)
        return res 
                   
            