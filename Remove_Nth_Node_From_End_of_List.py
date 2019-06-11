class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        temp = []
        ans = head
        while True :
            if ans :
                temp.append(ans.val)
                ans = ans.next
            else :
                break 
                
        index = len(temp) - n
        temp = temp[:index] + temp[index+1:]
        print(temp)
        if len(temp) == 0:
            return []
        count = 0 
        for i in temp:
            if count == 0 :
                head = ListNode(i)
                ans = head 
                count += 1
            else : 
                ans.next = ListNode(i)
                ans = ans.next
        
        return head  