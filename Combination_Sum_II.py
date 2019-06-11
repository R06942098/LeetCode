class Solution:
    """
    ###There exists duplicate element in the candidate list, but limits use them only one time.

    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
    """
    ### My solution is slower than 70% of the programmer.
    def combinationSum2(self, candidates, target):
        c = sorted(candidates)
        c.reverse()
        ans = []
        iteration = 0
        def dfs(can, ans_list=[]):
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
                            dfs(can[ind+1:], ans_list+[i])

                        else: 
                            ### Can not find the duplicate, may comment this paragraph.
                            ### Or force loop = 1 
                            #loop = temp // i
                            if temp >= i:
                                #ans_list += [i] 
                                ind = can.index(i)
                                #dfs(can[ind+1:], ans_list+[i for _ in range(k+1)])
                                dfs(can[ind+1:], ans_list+[i])
                                '''
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
                                '''

                            elif temp < i : 
                                #print(temp)
                                #ans_list += [i] 
                                if temp < min(c):
                                    #dfs(can[count:], ans_list, count+1)
                                    continue
                                else: 
                                    ind = can.index(i)
                                    #ans_list += [i] 
                                    dfs(can[ind+1:], ans_list+[i])    

                            elif temp  == 0 : 
                                kkk = sorted(ans_list+[i])
                                if kkk not in ans : 
                                    ans.append(kkk)
                                #ans_list = []
                                #dfs(can[count:], ans_list[:len(ans_list)-1], count+1)

                            else:
                                pass

                    elif temp == 0 : 
                        kkk = sorted(ans_list+[i])
                        if kkk not in ans : 
                            ans.append(kkk)
                        #ans_list = []
                        #dfs(can[count:], ans_list[:len(ans_list)-1], count+1)

                    else:
                        pass
        dfs(c)
        #print(ans)
        return ans

    def check(self, a): 
        ## this may cost some speed.
        temp = []
        for i in a : 
            q = sorted(i)
            if q not in temp: 
                temp.append(q)
        return temp
b = Solution()
a = [10,1,2,7,6,1,5]
a = [2, 5, 2, 1, 2]
c = 5
#c = 7
print(b.combinationSum2(a, c))

#print(b.combinationSum(a, c))








