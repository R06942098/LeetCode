class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        fill = gas[1:] + [gas[0]]
        ans = []
        for i in range(len(gas)): 
            temp = gas[i] 
            count = 0 
            while True: 
                if count == len(gas):
                    return i
                temp -= cost[count]
                if temp < 0 :
                    break
                else: 
                    temp += fill[count]
                    count += 1 
            cost = cost[1:] + [cost[0]]
            fill = fill[1:] + [fill[0]]  
        return -1 
        """
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        #### ***********************
        #### I think this may be a good method, but it's time consuming.
        #### ***********************

        candidate = [i for i in range(len(gas))]
        #initial_state = [i for i in gas]
        fill = gas[1:] + [gas[0]]
        n = len(gas)
        for _ in range(n):
            ca = []
            for j in candidate:
                temp = gas[j] - cost[j]
                if temp >= 0 : 
                    ca.append(j)
                    temp += fill[j]
                    gas[j] = temp 
            candidate = ca
            cost = cost[1:] + [cost[0]]
            fill = fill[1:] + [fill[0]]

        if len(candidate) == 0:
            return -1 

        else: 
            return candidate[0]
        
b = Solution()
a = [1,2,3,4,5]
c = [3,4,5,1,2]

a  = [2,3,4]
c = [3,4,3]

print(b.canCompleteCircuit(a, c))
