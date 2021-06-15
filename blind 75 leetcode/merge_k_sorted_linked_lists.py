''' You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it. '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	### make use of the merge two lists solution
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1):
            return l2
        if (not l2):
            return l1
        L3 = dummy = ListNode(0)
        while (l1 != None and l2 != None):
            ## if the l1 value is less than l2, continue traversing
            ## the l1 pointer
            if (l1.val < l2.val):
                L3.next = l1
                l1 = l1.next
            ## if the l2 value is less than l1, continue traversing
            ## the l2 pointer
            else:
                L3.next = l2
                l2 = l2.next
            L3 = L3.next
        if (l1 != None):
            L3.next = l1
        if (l2 != None):
            L3.next = l2
        return dummy.next
    ## iterate through the array of linked lists
   	## the concept is that we take the first list, and set to variable as output
   	## and then merge the next list with the first and set that to the new output 
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if (len(lists) == 0):
            return None
        elif (len(lists) == 1):
            return lists[0]
        else:
            output = lists[0]
            for i in range(1, len(lists)):
                output = self.mergeTwoLists(output, lists[i])
            return output
        
        