# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        """
        O(N) time and O(1) space solution
        1) iterate through list1, set two pointers where we're one node before a and one node after b  keeping track of the index (i == a-1, i == b + 1), since we don't want to include the actual values of a and b in the new list
        2) on a, set the next value of a to the beginning of list2
        3) after setting, we iterate on this pointer to its end (which is the end of list2)
        4) set the next of list2 to b
        """
        begin = None
        end = None
        i = 0
        head1 = list1
        # iterate through list1, keeping track of one node before a and one node after b when reached
        while (head1):
            if (i == a-1):
                begin = head1
            elif (i == b+1):
                end = head1
            head1 = head1.next
            i += 1
        begin.next = list2
        # iterate to the end of list2
        while (begin.next):
            begin = begin.next
        # set the end of begin to b
        begin.next = end
        return list1
            
        
        