# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # May use the 


        self.ans = []
        if not head: 
            return []

        if k == 0:
            return head 

        if not head.next : 
            return head 

        le = 0 
        compute = head
        while True:
            if not compute.next:
                le += 1
                break 
            else:
                le += 1 
                compute = compute.next
                
        k = k % le
        def rotate(a, count = 0):
            if count == k :
                self.ans.append(a)
                return None

            start = a
            pass_rout = start
            while True:
                if not pass_rout.next.next:
                    val = pass_rout.next.val 
                    pass_rout.next = None 
                    break 
                else:
                    pass_rout = pass_rout.next

            ans = ListNode(val)
            ans.next = start
            rotate(ans, count+1)

        final_ans = rotate(head)
        #print(self.ans[0])
        return self.ans[0]



a = [1,2,3]
count = 0 
for i in a : 
    if count == 0 : 
        head = ListNode(i)
        ans = head 
        count +=1 
        continue
    else: 
        ans.next = ListNode(i)
        ans = ans.next
b = Solution()
c = 2
print(b.rotateRight(head, c))
