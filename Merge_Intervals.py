class Solution:
    def merge(self, intervals):
        self.ans = []    
        def recursive(a, index=0):
            ans = a[:index]
            if index >= len(a):
                self.ans.append(a)
            first_item = a[index]
            count = 1
            while True: 
                if index + count >= len(a):
                    break
                b = a[index+count]
                temp = first_item[1]
                count_1 = 0
                if temp > b[0]:
                    if temp< b[1]:
                        ans.append([first_item[0],b[1]])
                        count_1 +=1
                else: 
                    if count_1 == 0 : 
                        ans.append(first_item)
                        ans.append(b)
                        count_1 += 1 
                    else: 
                        ans.append(b)
                        count_1 += 1
                count+=1 

            print(ans)
            recursive(ans, index+1)
        recursive(intervals)
        print(self.ans)

b = Solution()
a = [[1,3],[2,6],[8,10],[15,18]]
b.merge(a)