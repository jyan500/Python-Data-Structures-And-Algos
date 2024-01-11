'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Revisited in 7/26/2023
Key concept:
1) when iterating through both lists,
because the lists are sorted, if one ptr value is less than the other,
you can continue iterating down that pointer, adding more nodes to the list
until that condition is no longer true

2) If one of the lists finishes iterating before the other,
append the remainder of the linked list

Time Complexity: O(N)
Space Complexity: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        cur = newHead
        
        ptr1 = list1
        ptr2 = list2
        
        # iterate through both lists
        while (ptr1 != None and ptr2 != None):
            # if one val is less than the other,
            # keep iterating through that side until it's no longer less,
            # then switch to iterating on the other side
            if ptr1.val < ptr2.val:
                n1 = ListNode(val=ptr1.val)
                cur.next = n1
                cur = cur.next
                ptr1 = ptr1.next
            else:
                n2 = ListNode(val=ptr2.val)
                cur.next = n2
                cur = cur.next
                ptr2 = ptr2.next
                
        # append the remainder of the linked list
        # if iteration didn't complete on one side
        if ptr1 != None:
            cur.next = ptr1
        elif ptr2 != None:
            cur.next = ptr2
        return newHead.next

## my attempt
## where I went wrong was that I assumed that you could always traverse down
## the lists simultaneously, rather than alternating traversing between one list or the other
## like in the solution. If the value is less, than continue traversing down the list that contained the lesser value
## and then replace the "next" for the L3 with the rest of the linked list (of either L1 or L2) rather than just the node itself
## also the dummy node helps keep track of the original head of the list while building L3
# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
# 	 head1 = l1
#     head2 = l2
#     L3 = ListNode()
#     head = L3
#     end_of_l1 = None
#     end_of_l2 = None
#     if (head1 != None and head2 != None):
#         while (head1.next != None and head2.next != None):
#             head1 = head1.next
#             head2 = head2.next
#         end_of_l1 = head1.val
#         end_of_l2 = head2.val
#         while (l1.next != None and l2.next != None):
#             print(l1.val)
#             print(l2.val)
#             if (l1.val <= l2.val):
#                 head.next = ListNode(l1.val)
#                 head = head.next
#                 head.next = ListNode(l2.val)
#                 head = head.next
#             else:
#                 head.next = ListNode(l2.val)
#                 head = head.next
#                 head.next = ListNode(l1.val)
#                 head = head.next
#             if (l1.next != None and l1.next.val <= end_of_l2):
#                 l1 = l1.next
#             if (l2.next != None and l2.next.val <= end_of_l1):
#                 l2 = l2.next
#     if (l1 != None):
#         head.next = l1 
#         head = head.next
#     if (l2 != None):
#         head.next = l2
#         head = head.next
#     return L3.next 

## solution
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
	if (not l1):
		return l2
	if (not l2):
		return l1
	L3 = dummy = ListNode(0)
	while (l1 != None and l2 != None):
		## if the l1 value is less than l2, continue traversing
		## the l1 pointer
		if (l1.val < l2.val):
			## set the next to the rest of the L1 linked list
		    L3.next = l1
		    l1 = l1.next
		## if the l2 value is less than l1, continue traversing
		## the l2 pointer
		else:
			## set the next to the rest of the L2 linked list
		    L3.next = l2
		    l2 = l2.next
		L3 = L3.next
	if (l1 != None):
		L3.next = l1
	if (l2 != None):
		L3.next = l2
	return dummy.next





