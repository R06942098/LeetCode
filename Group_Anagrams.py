class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = dict() 
        temp = []
        ans = []
        count = 0 
        for i in strs: 
            c = self.combine(sorted(list(i)))
            
            if c not in a.keys(): 
                a[c] = count 
                count += 1 
                ans.append([i])
            else: 
                ans[a[c]].append(i)
        return ans 
    
    def combine(self, l1):
        a = '' 
        for i in l1: 
            a += i 
        return a 