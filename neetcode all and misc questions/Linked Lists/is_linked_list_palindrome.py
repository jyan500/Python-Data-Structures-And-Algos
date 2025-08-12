'''
https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a palindrome.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Revisited 8/12/2025
    O(N) Time
    O(1) Space
    solution using two pointers to find the middle of the LL
    and then reversing the second half,
    and then comparing the two halves to see if they're equal values
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # separate the second half of the linked list 
        secondHalf = slow.next
        slow.next = None

        # reverse the second half
        cur = secondHalf
        prev = None
        while (cur):
            temp = cur
            cur = cur.next
            temp.next = prev
            prev = temp
        
        # iterate through both simultaneously to see if the nodes are equal
        while (head and prev):
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

class Solution:
	## O(N) time but O(N) space, is it possible to do this in O(1) space?
	def isPalindrome(self, head: ListNode)->bool:
		ptr = head
        vals = []
        while (ptr != None):
            vals.append(ptr.val)
            ptr = ptr.next
        reverse = []
        
        for i in range(len(vals)-1,-1,-1):
            reverse.append(vals[i])
        return vals == reverse

    ## Using O(1) space
    ## utilizing two pointers and reversing a linked list in place

    ## helper function that takes a head of a linked list and reverses the linked list in place
    def reverseLinkedList(self, head):
        cur = head
        prev = None
        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        
        first_half = head
        second_half = None
        slow = head
        fast = head
        ## Get the middle of linked list by utilizing a fast and slow pointer, where the fast pointer goes through
        ## twice as fast as the slow
        ## because fast iterates through twice as fast, slow will contain the middle of the linked list
        ## this is the same as floyd's cycle detection algorithm
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        ## to account for edge case for odd number of list nodes (when fast pointer is None, for even number nodes, fast pointer would be the last element and not None), we need to shift the slow pointer by one over since
        ## in an odd number, you need to shift one over to go from the middle to the second half
        # Update: 7/28/2023 this might not be necessary?
        # if (fast != None):
        #     slow = slow.next
            
        
        
        ## Reverse the second half of the linked list
        second_half = self.reverseLinkedList(slow)

        ## Check if the first and second half are identical
        ## if all nodes matched, return true, else false
        while (first_half != None and second_half != None):
            if (first_half.val != second_half.val):
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True



