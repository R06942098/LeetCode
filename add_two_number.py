# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ''
        b = ''
        count = 0 
        while True :
            if count == 0:
                a+=str(l1.val)
                #print(a)
                count+=1 
                temp = l1.next
            else :
                if not temp: 
                    break 
                else:
                    a+=str(temp.val)
                    temp = temp.next
                    #print(a)
        count = 0
        while True :
            if count == 0:
                b+=str(l2.val)
                #print(b)
                count+=1 
                temp = l2.next
            else :
                if not temp: 
                    break 
                else: 
                    b+=str(temp.val)
                    temp = temp.next

        ### reverse string command line
        a = int(a[::-1])
        b = int(b[::-1])
        c = str(a + b)[::-1]
        ### bulid the answer node list.
        count = 0
        for i in c: 
            if count == 0 : 
                head = ListNode(i)
                answer = head
                count += 1 
            else: 
                a =  ListNode(i)
                head.next = a 
                head = head.next
                count += 1 
        return answer