class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

"""
For instance, 

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

"""

class Solution:
	def partition(self, head: ListNode, x: int) -> ListNode:
		list_1 = []
		list_2 = []

		if not head : 
			return []

		if head.next == None:
			return head

		while True : 
			if head.next == None:
				if head.val < x :
					list_1.append(head.val)
					break
				else:
					list_2.append(head.val)
					break 

			if head.val < x : 
				list_1.append(head.val)
			else: 
				list_2.append(head.val)

			head = head.next
		list_1 += list_2
		print(list_1)
		ans = self.costruct_node(list_1)
		return ans 

	def costruct_node(self, a):
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
		return head

a = [1,4,3,2,5,2]
a = [3,1,4,5,6]
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
c = 3
c = 2
d = b.partition(head, c)
print(d.val)


