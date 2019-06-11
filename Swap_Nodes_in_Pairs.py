# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        index = 0 
        temp = [] 
        while True :
            if head == None:
                break 
            else:
                temp.append(head.val)
            head = head.next
        '''
        ans = head
        while True: 
            if ans:
                a = ans.next 
                if a == None :
                    break 
                else: 
                    ans.val, a.val = a.val, ans.val 
                    for _ in range(2):
                        ans = ans.next
            else:
                break
        return head