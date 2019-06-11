class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = []
        temp_1 = []
        while True: 
            if l1 : 
                temp.append(l1.val)
                l1 = l1.next
            else:
                break 
                
        while True: 
            if l2 : 
                temp_1.append(l2.val)
                l2 = l2.next
            else:
                break 
        
        temp += temp_1 
        temp.sort()
        #print(temp)
        if len(temp) == 0:
            return [] 
        count = 0 
        for i in temp:
            if count ==0 : 
                a = ListNode(i) 
                ans = a 
                count += 1
            else : 
                ans.next = ListNode(i) 
                ans = ans.next
        return a 
        