'''
ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1: 
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        carryover = 0
        dummy = ListNode(None)
        head = dummy
        ## iterate through both linked lists simultaneously, adding l1.val and l2.val
        ## and accounting for carryover
        ## we also need to construct a new linked list while iterating
        while (l1 != None and l2 != None):
            val = l1.val + l2.val
            if (carryover == 1):
                val += carryover
                carryover = 0

            if (val >= 10):
                val -= 10
                carryover = 1
            head.val = val
            head.next = ListNode(None)
            ## in the case that we're on our last digit for both linked lists and don't have any more carryover
            ## end the linked list
            if (l1.next == None and l2.next == None and carryover == 0):
                head.next = None
            head = head.next
            l1 = l1.next
            l2 = l2.next
        ## if one linked list length is greater than the other, 
        ## we need to continue the process on either l1 or l2
        if (l1 != None):
            while (l1 != None):
                val = l1.val
                if (carryover == 1):
                    val += carryover
                    carryover = 0
                if (val >= 10):
                    val -= 10
                    carryover = 1
                head.val = val
                head.next = ListNode(0)
                ## in the case that we're on our last digit and don't have any more carryover
                ## end the linked list
                if (l1.next == None and carryover == 0):
                    head.next = None
                head = head.next
                l1 = l1.next
                
        elif (l2 != None):
            while (l2 != None):
                val = l2.val
                if (carryover == 1):
                    val += carryover
                    carryover = 0
                if (val >= 10):
                    val -= 10
                    carryover = 1
                head.val = val
                head.next = ListNode(0)
                ## in the case that we're on our last digit and don't have any more carryover
                ## end the linked list
                if (l2.next == None and carryover == 0):
                    head.next = None
                head = head.next
                l2 = l2.next
        ## special case where we still have a carryover after fully iterating both lists
        ## just set the last linked list item to 1
        if (carryover == 1):
            head.val = 1
        return dummy
                
                
            
