'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

https://leetcode.com/problems/reverse-linked-list/

'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	"""
    	Revisited 9/29/2024
    	In this version, 3 pointers are used. Curr points to head so that we don't mutate the original head
    	save the position of curr in temp
    	advance curr
    	set the temp pointer's next backwards towards prev
    	and then advance prev to where temp is
    	"""
        prev = None
        curr = head
        while (curr != None):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev

class Solution2:
	def reverseList(self, head: ListNode) -> ListNode:
		""" 
		in place solution approach:
        we keep track of prev, which is the head of our new list
        on each iteration, we track curr, which is the placement of our head currently before we 
        do head.next to advance to the next node
        we then set the value of curr.next to be prev, which is basically setting equal to the 
        previous element in the list, and then setting prev to be the "head" of this new list
        example:
        1 -> 2 -> 3 -> 4 -> 5 -> None
        1st iteration, we build 1 -> None
        prev = None
        curr = head (curr = 1)
        head = head.next (head = 2)
        curr.next = prev ( curr.next = None)
        prev = curr (prev = 1)
        
        2nd iteration, we build 2 -> 1 -> None
        prev = 1
        curr = head (curr = 2)
        head = head.next ( head = 3)
        curr.next = prev ( curr.next = 1)
        prev = curr ( prev = 2)
        
        3rd iteration, we build 3 -> 2 -> 1 -> None, etc
        
        finally at the last iteration
        prev = 4
        curr = head ( curr = 5)
        head = head.next (head = None)
        curr.next = prev ( curr.next = 4)
        prev = curr ( prev = 5 )
        
        head is now none, so our loop is done
        
        """
        prev = None
        while (head != None):
            curr = head
            head = head.next
            curr.next = prev
            prev = curr	
        return prev

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
	# Note this version does not mutate the head argument
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
