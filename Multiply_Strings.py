class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = self.convert_to_integer(num1)
        #print(a)
        b = self.convert_to_integer(num2)
        #print(b)
        c = a * b 
        #print(c)
        #return self.convert_to_str(c)
        return str(c)
    
    def convert_to_integer(self, a: str):
        b = 0
        n = len(a)
        for i in a : 
            n -= 1 
            b += int(i) * (10**(n))
        return b 

    def convert_to_str(self, a):
        b = ''
        count = [i for i in range(0,6)]
        count.reverse()
        start = 0
        for i in count : 
            if a > 10**(i):
                index = a // 10**(i)
                print(index)
                a -= index *(10 ** (i))
                print(a)
                b += str(index)
            else: 
                if len(b)>1: 
                    b += str(0)
            
        return b 