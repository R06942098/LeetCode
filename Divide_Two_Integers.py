#class Solution:
    '''
    ### this function is too slow, for operation O(n)
    def divide(self, dividend: int, divisor: int) -> int:
        ### How to break through the time limit....
        ans = 0
        while True : 
            if dividend > 0: 
                if divisor < 0: 
                    if dividend > -1 * divisor: 
                        ans -= 1 
                        dividend += divisor
                    if dividend < -1 * divisor: 
                        break 
                    
                if divisor > 0: 
                    if dividend > divisor: 
                        ans +=1 
                        dividend -= divisor 
                        
                    if dividend <  divisor: 
                        break 
                        
            else: 
                if divisor < 0: 
                    if -1 * dividend > -1 * divisor: 
                        ans += 1 
                        dividend -= divisor
                        
                    if -1 * dividend < -1 * divisor: 
                        break 
                        
                if divisor > 0: 
                    if -1 * dividend > divisor: 
                        ans -=1 
                        dividend += divisor  
                        
                    if -1 * dividend < divisor: 
                        break 
        print(ans)
        return ans 
    '''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0
        count = 0
        res = 0
        ### I totally know that the abs function is innerable.
        a = abs(dividend)
        b = abs(divisor)
        ### I have this think, but never implement it..
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res     
        print(res)
        #### some constraint should be put in here.
        if res <= -1 * 2**(31):
            return -1 * 2**(31)
        
        if res >= 2**(31)-1: 
            return 2**31-1 
        
        return res








