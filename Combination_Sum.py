class Solution:

    """
    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]
    """

    def combinationSum(self, candidates, target):
        c = sorted(candidates)
        c.reverse()
        #print(c)
        ans = []
        iteration = 0
        #while True  : 
        def dfs(can, ans_list=[], count=1):
            ### recursive path 是要在函數輸入內改變,不要在function內部自己變動變數.
            for i in can: 
                sum_num = sum(ans_list)
                tar = target - sum_num
                if tar >= i:
                    temp = tar - i 
                    if temp != 0:
                        if temp < min(c) :
                            #dfs(can[count:], ans_list, count+1)
                            continue

                        if temp < i:
                            #ans_list += [i] 
                            ind = can.index(i)
                            dfs(can[ind+1:], ans_list+[i], count+1)

                        else: 
                            loop = temp // i
                            for k in range(loop):
                                if temp >= i:
                                    #ans_list += [i] 
                                    ind = can.index(i)
                                    dfs(can[ind+1:], ans_list+[i for _ in range(k+1)], count+1)
                                    temp -= i 

                                    if temp == 0 : 
                                        #ans_list += [i]
                                        ans.append(ans_list+[i for _ in range(k+2)]) 
                                        #ans_list = []   

                                    if k == (loop-1):
                                        if temp != 0: 
                                            if temp < i:
                                                if temp >= min(c):
                                                    ind = can.index(i)
                                                    dfs(can[ind+1:], ans_list+[i for _ in range(k+2)], count+1)  
                                                else:   
                                                    #print(True)
                                                    continue
                                elif temp < i : 
                                    #print(temp)
                                    #ans_list += [i] 
                                    if temp < min(c):
                                        #dfs(can[count:], ans_list, count+1)
                                        continue
                                    else: 
                                        ind = can.index(i)
                                        #ans_list += [i] 
                                        dfs(can[ind+1:], ans_list+[i], count+1)    

                                elif temp  == 0 : 
                                    #ans_list += [i]
                                    ans.append(ans_list+[i]) 
                                    #ans_list = []
                                    #dfs(can[count:], ans_list[:len(ans_list)-1], count+1)

                                else:
                                    pass

                    elif temp == 0 : 
                        ans.append(ans_list+[i]) 
                        #ans_list = []
                        #dfs(can[count:], ans_list[:len(ans_list)-1], count+1)

                    else:
                        pass
        dfs(c)
        #print(ans)
        return self.check(ans)

    def check(self, a): 
        ## this may cost some speed.
        temp = []
        for i in a : 
            q = sorted(i)
            if q not in temp: 
                temp.append(q)
        return temp
b = Solution()
a = [2,3,6,7]
#a = [1,2,3,4,5,6,7,8,9,10]
a = [2,6]
a = [4,2,7,5,6]

#a = [2,3,5]
#a = [1,3]
#a = [7]
c = 16
#c = 7
print(b.combinationSum(a, c))

#print(b.combinationSum(a, c))








