'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/

'''

class Solution:
	## my first attempt using O(N) time and O(N) space
	def reverseList(self, head: ListNode) -> ListNode:
	    cur = head
	    if (cur):
	        new_head = None
	        stack = []
	        ## get to the last element
	        ## push every element onto to the stack to allow us to create new list nodes in reverse
	        while (cur.next != None):
	            stack.append(cur.val)
	            cur = cur.next
	        new_head = cur
	        ## set the last element to the new head
	        ## and pop the elements off of the stack to construct the linked list in reverse
	        pointer = new_head
	        while (stack):
	            val = stack.pop()
	            n = ListNode(val)
	            pointer.next = n
	            pointer = pointer.next
	        return new_head
	## O(N) time and O(1) space iterative solution
	def reverseList(self, head:ListNode) -> ListNode:
		prev = None
		cur = head
		## the idea is that you point the current node's next value to the previous node
		while (cur != None):
			## store the cur's next value since we'll be reassigning it
			temp = cur.next
			## set the current node's next to the prev
			cur.next = prev
			## set the previous node to be the cur
			prev = cur
			## continue to iterate through the list by setting cur to the next value that we saved
			cur = temp
		## return prev because this will contain the last Node
		## this will also be the "head" of the reversed linked list because every next value will be the previous node
		return prev

	## O(N) time and O(N) space recursive solution
	def reverseList(self, head: ListNode) -> ListNode:
		return self.reverseHelper(head, None)

	## the basic idea behind the recursion similar to the iterative solution
	## where we pass in the head and the new_head (which plays a similar role to the "prev" variable in the iterative solution)
	## where we set the head's next to the previous node (in this case previous node is the new_head variable)
	## and the base case would be when the head reaches None
	def reverseHelper(self, head, new_head):
		if (head == None):
			return new_head

		temp = head.next
		head.next = new_head
		new_head = head
		head = temp

		return self.reverseHelper(head, newHead)
