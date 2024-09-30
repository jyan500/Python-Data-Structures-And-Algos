'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://neetcode.io/problems/merge-two-sorted-linked-lists
        Revisited 9/30/2024
        use two pointers
        iterate through the two lists simultaneously until one of the lists becomes None
        at each point, compare which node's value is greater. If so, set the curr.next
        to be the remainder of that list, then increment the pointer for that list,
        as well as curr's pointer. The reason why this works is because each time,
        you are basically overwriting the remainder of the list with the other "remainder of the list"
        and then moving the curr pointer, while not mutating the original list1 and list2 (except for when you increment
        the pointers on each list)
        """
        dummy = ListNode()
        curr = dummy
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
            	# set the next to the remainder of list1, then increment list1.
                curr.next = list1
                list1 = list1.next
            # this accounts for cases when list1.val >= list2.val
            else:
            	# set the next to the remainder of list2
                curr.next = list2
                list2 = list2.next
            curr = curr.next
               
        if (list1 != None):
            curr.next = list1
        elif (list2 != None):
            curr.next = list2
        
        return dummy.next

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





