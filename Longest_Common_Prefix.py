class Solution:
    def longestCommonPrefix(self, strs) :
    	if len(strs)== 0 : 
    		return ""
        le = [len(i) for i in strs] 
        mi = le.index(min(le))
        if min(le) == 0:
        	return ""
        inspect = strs[mi]
        i = 0
        while i <= min(le): 
        #for i in range(min(le)):
            temp = inspect[:i+1]
            print(i)
            print(temp)
            count = 0
            for j in strs:
            	print(j[:i+1])
            	if temp == j[:i+1]: 
            		count +=1 

            if count == len(strs):
            	if i == min(le)-1:
            		return inspect
            	i += 1 
            else : 
            	print("*******")
            	if i == 0 :
            		return ""
            	else: 
            		print(i)
            		return inspect[:i]


a = ["flower","flow","flight"]
a = ["dog","racecar","car"]
a = ['abd', 'abcd', 'abcde']
a = [""]
b = Solution()
print(b.longestCommonPrefix(a))