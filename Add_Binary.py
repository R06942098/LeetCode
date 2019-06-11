class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = self.to10base(a)
        print(a)
        b = self.to10base(b)
        print(b)
        c = a + b
        print(c)
        return self.to2base(c)
    
    def to10base(self, a):
        
        le = len(a)
        count = 0
        index = 1
        for i in a : 
            count += (int(i)*2**(le-index))
            index += 1 
        return count 
    
    def to2base(self, a):
        ans = '' 
        while True:
            ans += str(a%2)
            a = a // 2
            if a == 0 :
                break 
        return ans[::-1] 