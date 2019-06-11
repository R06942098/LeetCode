# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return []
        if m == n :
            return head
        index = 1
        ans = head
        sort_list = [] 
        while True : 
            if not ans :
                break
            if m > 1:       
                if index == m-1 :
                    start = ans 
            else:
                if index == 1:
                    start = ans
                
            if index >=m:
                if index < n:
                    sort_list.append(ans.val)
            if index == n : 
                start.next = None
                sort_list.append(ans.val)
                end = ans.next 
                sort_list.reverse()
                if m == 1:
                    count = 0
                    for i in sort_list:
                        if count == 0: 
                            start.val = i
                            count += 1
                        else:
                            start.next = ListNode(i)
                            start = start.next
                            
                else:
                    for i in sort_list:
                        start.next = ListNode(i)
                        start = start.next
                start.next = end
                break 
            ans = ans.next
            index += 1 
        return head