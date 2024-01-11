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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Revisited 9/8/2023
O(N) Time and O(N) memory solution
1) convert both linked lists into arrays
2) create a temp array while adding the numbers together
3) If sum of digits > 10, placeholder = sum % 10 and carry over is always 1 (max should be 9 + 9, so carry over 1 and then placeholder 8)
we add the placeholder to the temp array to represent the digit and then carry over 1. 
If there's no carryover because the sum of digits < 10, just the sum of digits + carryover
4) If len(l1) != len(l2), account for additional spots to cover carryover after the last digit of the shorter linked list 
by padding shorter list with zeroes (i.e 99999+999 is effectively 99999+00999 when performing carryover addition)
5) If there's an additional carryover at the end, add to the temp array
6) convert temp array back to linked list
"""
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        list1 = []
        list2 = []
        while (p1):
            list1.append(p1.val)
            p1 = p1.next
        while (p2):
            list2.append(p2.val)
            p2 = p2.next
        # if one of the lists is shorter than the other, pad the shorter list with zeroes
        # to make addition easier
        if len(list1) < len(list2):
            list1.extend([0 for i in range(len(list2)-len(list1))])
        else:
            list2.extend([0 for i in range(len(list1)-len(list2))])
        temp = []
        carryover = 0
        for a, b in zip(list1, list2):
            # if sum is less than 10, add and reset the carryover
            if carryover + a + b < 10:
                temp.append(carryover + a + b)
                carryover = 0
            # if the sum is greater than 10, recalculate the new placeholder
            # and set carryover to 1
            # i.e 9 + 9 = 18, placeholder = 8 and carryover = 1
            else:
                newSum = carryover + a + b 
                placeholder = newSum % 10
                carryover = 1
                temp.append(placeholder)
        # append final digit of carry over if it exists
        if carryover != 0:
            temp.append(carryover)
        l = ListNode()
        head = l
        # convert back to linked list
        for i in range(len(temp)):
            head.next = ListNode(val=temp[i])
            head = head.next
        return l.next
        

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
                
                
            
