# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        https://leetcode.com/problems/palindrome-linked-list/description/
        you can also try splitting the LL in half using slow and fast pointers, and then reversing the second half,
        then iterating through each half simultaneously to see if its the same. Note that if its an odd number
        of list nodes on one side, we only need to check up to the shorter list node
        1 -> 2 -> 3 -> 2 -> 1
        if we split the LL in half using the slow and fast pointers:
        1->2->3
        2->1, and then reverse 1->2
        
        so we have 1->2->3
        1->2
        we only need to compare up to 2 to see that it is indeed a palindrome
        """
        # when fast pointer reaches the end, the slow pointer should now be in the middle
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        # disconnect the two halves,
        # the second half should now be at slow.next
        secondHalf = slow.next
        slow.next = None
        prev = None
        curr = secondHalf
        while (curr != None):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        # head should now be the first half of the list, since we disconnected the two halves
        # we go up to prev, since prev should always be the shorter half
        while (prev != None):
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True