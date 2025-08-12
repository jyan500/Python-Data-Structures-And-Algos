# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/add-two-numbers-ii/

        Normally when doing addition, you start from the back and work your way towards the front
        of the number (which is its highest place digit). However in this problem, the linked list is
        not in reverse order like in add numbers I, so you don't know what the last element of the linked list is (where you'd normally
        start adding).

        To solve this, you'd have to reverse the LL's first. And also figure out which LL is longer, and then pad the 
        shorter LL with 0's after its been reversed to avoid edge cases with carryovers and needing
        to handle one pointer while the other has already ended due to being a shorter list

        after doing addition, you'll need to re-reverse the result to get the original order since the result would be reversed otherwise.

        Time: O(N), (although there are 3 different reverse operations, but all taking O(N))
        Space: O(1)
        """
        def reverse(node):
            prev = None
            cur = node
            while (cur):
                temp = cur
                cur = cur.next
                temp.next = prev
                prev = temp
            return prev

        lengthL1 = 0
        lengthL2 = 0

        # reverse both LL
        prev1 = reverse(l1)
        prev2 = reverse(l2)
        newHead1 = prev1
        newHead2 = prev2
        newHeadCur1=  newHead1
        newHeadCur2 = newHead2

        while (newHeadCur1.next):
            newHeadCur1 = newHeadCur1.next
            lengthL1 += 1
        
        while (newHeadCur2.next):
            newHeadCur2 = newHeadCur2.next
            lengthL2 += 1
        
        # figure out which LL is longer, and pad the shorter LL with 0's at the end 
        # to make the addition steps easier, since you don't need to worry about one list ending before the other.
        if lengthL1 < lengthL2:
            diff = lengthL2 - lengthL1
            for i in range(diff):
                newNode = ListNode(0)
                newHeadCur1.next = newNode
                newHeadCur1 = newHeadCur1.next
        elif lengthL2 < lengthL1:
            diff = lengthL1 - lengthL2
            for i in range(diff):
                newNode = ListNode(0)
                newHeadCur2.next = newNode
                newHeadCur2 = newHeadCur2.next
        
        # prepare the addition with a new ListNode that contains the sum
        dummy = ListNode(0)
        cur = dummy
        carryover = 0
        while (newHead1 and newHead2):
            res = carryover + newHead1.val + newHead2.val
            # carryover of 1 if the result of the sum is >= 10
            carryover = 1 if res >= 10 else 0
            newNode = ListNode(res - 10 if res >= 10 else res)
            cur.next = newNode
            cur = cur.next
            newHead1 = newHead1.next
            newHead2 = newHead2.next

        # if there's a remaining carryover, add 1 as the final node in the list
        if carryover == 1:
            cur.next = ListNode(1)
            cur = cur.next
        
        # reverse dummy.next to get the result in the original order
        resHead = dummy.next
        return reverse(resHead)
        

        