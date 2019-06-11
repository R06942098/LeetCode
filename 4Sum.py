class Solution:
    #def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    ### Recursive is too slow..., but it is a insight for me that i understand how it works.
    '''
    def fourSum(self, nums, target):
        le = len(nums)
        nums = sorted(nums)
        res = []
        #感覺可以用recursive下去做... 因為一次取一個然後每次都剩下list去找
        def dfs(a, q, count=0, path=[]): 
            le = len(a)
            if count == 3:       
                #print(count)
                #number = a.count(q)
                #if number > 1 : 
                if q in a : 
                    path += [q]
                    path.sort()
                    if path not in res: 
                        res.append(path)

            elif count <= 2: 
                for i in range(le): 
                    k = a[i]
                    s = q - k 
                    other_list = a[:i] + a[i+1:]
                    print(len(other_list))
                    dfs(other_list, s, count+1, path+[k])
            else: 
                pass

        dfs(nums, target)
        return res 
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## Sum problem needs K-1 index to move...
        nums.sort()
        le = len(nums)
        ans_set = []
        count = 0
        '''
        ### not faster more..
        for i in range(le-3) :
            if count > 0 : 
                if nums[i] == nums[i-1]:
                    continue 
        '''
        i = 0
        while i < le-3: 
            j = i + 1
            while j < le-2 :
                k = j + 1
                l = le - 1 
                remain = target - nums[i] - nums[j]
                while k < l : 
                    if nums[k] + nums[l] > remain: 
                        l -= 1 
                    elif nums[k] + nums[l] < remain:
                        k += 1
                    else : 
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        if temp not in ans_set: 
                            ans_set.append(temp)
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1        
                        k+=1 
                        l-=1 
                while j < le-2 and nums[j] ==nums[j + 1] :
                    j+=1 
                j+= 1 
            
            while i < le-3 and nums[i] == nums[i+1]:
                i+=1
            i+=1 
        return ans_set

a = Solution()
b = [1,0,-1,0,-2,2]
target = 0
b = [-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492]
target = 1682

print(a.fourSum(b, target))