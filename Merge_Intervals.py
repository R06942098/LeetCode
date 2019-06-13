class Solution:
    def merge(self, intervals):

        intervals = sorted(intervals)
        self.ans = []

        if len(intervals) == 0 : 
            return []

        while True: 
            if len(intervals) == 0 :
                break

            if len(intervals) == 1 :
                self.ans.append(intervals[0])
                break 

            start = intervals[0]
            count = 0 
            temp = []
            for i in range(1, len(intervals)):
                end = intervals[i]
                if start[1] >= end[0] and start[1] <= end[1]:
                    if count == 0 : 
                        temp.append(start)
                    temp.append(end)
                    start = [start[0], end[1]]
                    count += 1
  
                elif start[1] >= end[0] and start[1] >= end[1]:
                    if start[0] <= end[0] and start[0] <= end[1]:
                        if count == 0 : 
                            temp.append(start)
                        temp.append(end)
                    count += 1
                
                else: 
                    pass 

            if count > 0: 
                self.ans.append(start)
                for k in temp:
                    intervals.remove(k)
            else:
                self.ans.append(start)
                intervals.remove(start)

        return self.ans

b = Solution()
#a = [[1,3],[2,6],[8,10],[15,18]]
a = [[1,4], [0,4 ]]
a = [[1,4],[0,2],[3,5]]
a = [[1,2],[2,3],[4,11],[5,8]]
print(sorted(a))
print(b.merge(a))