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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Revisited 9/30/2024
        this solution uses a dummy node to prevent the edge case when deleting the head of the linked list
        iterate to the end of the linked list to get the length of the list
        iterate through the list again, but this keeping track of an index, as well
        as a previous pointer
        once we get to length of list - n, delete this node from the linked list
        by setting the previous pointer's next to be the current node's next
        """
        length = 0
        temp = head
        while (temp != None):
            temp = temp.next
            length += 1
        i = 0
        dummy = ListNode()
        prev = dummy
        temp2 = head
        indexToRemove = length - n
        while (temp2 != None):
            if (i == indexToRemove):
                prev.next = temp2.next
                temp2 = temp2.next
            else:
                prev.next = temp2
                temp2 = temp2.next
                prev = prev.next
            i+=1
        return dummy.next

"""
Revisited on 7-8-2023
Two Pass solution (O(2N))
1) 1st pass, traverse the list to find out the amount of elements
2) check the index that needs to be removed, since this is counting from the back
we would subtract the total length - n to give the index we need to remove
3) Special case: if we need to remove the head of the linked list (index = 0), we simply
set the head to the next element, and then return the head
4) Otherwise, we loop through the remainder of the linked list starting from head,
and track a previous element, if we find the element we want to delete, just 
set the previous' next to be equal to the current elements' next to skip over it
"""
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy1 = head
        dummy2 = head
        prev = head
        length = 0
        while (dummy1 != None):
            dummy1 = dummy1.next
            length += 1
        indexToRemove = length - n
        counter = 0
        if indexToRemove == 0:
            head = head.next
            return head
        else:
            while (dummy2 != None):
                if counter == indexToRemove:
                    prev.next = dummy2.next
                    dummy2 = dummy2.next
                else:
                    prev = dummy2
                    dummy2 = dummy2.next
                counter += 1
            return head        

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