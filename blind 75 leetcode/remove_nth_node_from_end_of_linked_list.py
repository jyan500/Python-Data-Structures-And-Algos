## Given the head of a linked list, remove the nth node from the end of the list and return its head.
## Explanation
## while iterating through the linked list
## move the fast pointer first
## once the distance between the fast and slow pointer is n, then start incrementing the slow pointer
## that way, once the fast pointer reaches the end of the linked list
## the slow pointer will be pointing to the node before the node we want to remove, which is the nth node of the end of the list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	## create a dummy node at the very front of the list before the head
	dummy = ListNode()
	slow = dummy
	fast = dummy
	dummy.next = head
	## keep track of the distance between the fast and the slow pointer
	fast_n = 0
	## see explanation above
	while (fast.next != None):
	    fast = fast.next
	    if (fast_n >= n):
	        slow = slow.next
	    else:
	        fast_n += 1
	## once the fast pointer has reached the end of the linked list, the slow pointer will then point 
	## to the node before the node we want to delete
	## all that is needed is to point the slow pointer's next node to the nth node's successor
	## which will remove the nth node
	slow.next = slow.next.next

	## return the dummy.next
	## note that there's an edge case where you just have one item in the linked list (the head)
	## and you have to remove the nth node
	## in this case, returning the head won't work since it should return a null value
	return dummy.next