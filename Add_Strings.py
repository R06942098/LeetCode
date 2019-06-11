class Solution:
    def addStrings(self, nums1: str, nums2: str) -> str:
        a = [len(nums1), len(nums2)]
        q = a.index(min(a))
        if q == 0: 
            ans = '' 
            count = 0
            for i in range(len(nums1)):
                a = int(nums1[-(i+1)]) + int(nums2[-(i+1)])
                if count != 0 : 
                    a += 1 
                    
                if a >= 10 : 
                    ans += str(a)[-1]
                    count = 1 
                else: 
                    ans += str(a)
                    count = 0 
                    
            index = 2 
            while True : 
                if count == 1 :
                    if i+index > len(nums2):
                        ans += '1'
                        return ans[::-1]
                    a = int(nums2[-(i+index)]) + 1 
                    if a >= 10 : 
                        count = 1 
                        ans += str(a)[-1]
                        index += 1 
                    else: 
                        ans += str(a)
                        index += 1 
                        count = 0
                else:
                    break      
            temp = - (i + index) + len(nums2)
            ans += nums2[:temp+1][::-1]
            return ans[::-1]
        else:
            ans = '' 
            count = 0
            for i in range(len(nums2)):
                a = int(nums1[-(i+1)]) + int(nums2[-(i+1)])
                
                if count != 0 : 
                    a += 1 
                    
                if a >= 10 : 
                    ans += str(a)[-1]
                    count = 1 
                    
                else: 
                    ans += str(a)
                    count = 0 
                    
            index = 2 
            while True : 
                if count == 1 :
                    if i+index > len(nums1):
                        ans += '1'
                        return ans[::-1]
                    a = int(nums1[-(i+index)]) + 1 
                    if a >= 10 : 
                        count = 1 
                        ans += str(a)[-1]
                        index += 1 

                    else: 
                        ans += str(a)
                        index += 1 
                        count = 0
                else:
                    break     
            temp = - (i + index) + len(nums1)
            ans += nums1[:temp+1][::-1]
            return ans[::-1]