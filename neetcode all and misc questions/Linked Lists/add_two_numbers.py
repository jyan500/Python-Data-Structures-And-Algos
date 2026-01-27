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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Revisited 1/27/2026 with the same solution
        Revisited 3/6/2025 with a similar solution
        because the numbers in the LL are stored in reverse order, they're in the same order
        that we normally use when performing addition (starting from the end first)

        if the two digits sum >= 10, save a carryover of 1, and save sum - 10 to the new LL

        it's also easier to pad the shorter LL with 0's on the back
        for example
        342 + 4 would be the equivalent of
        342 + 004
        which is the equivalent of these two LL's
        4 -> 0 -> 0
        2 -> 4 -> 3,
        so the padding occurs on the backside
        """
        copy1 = l1
        copy2 = l2
        len1 = 0
        len2 = 0
        while (copy1.next != None):
            len1 += 1
            copy1 = copy1.next
        while (copy2.next != None):
            len2 += 1
            copy2 = copy2.next
        # pad the shorter list with 0's based on the difference in lengths
        if len1 > len2:
            for i in range(0, len1 - len2):
                copy2.next = ListNode(0)
                copy2 = copy2.next
        elif len2 > len1:
            for i in range(0, len2 - len1):
                copy1.next = ListNode(0)
                copy1 = copy1.next
        dummy = ListNode()
        newHead = dummy
        carryover = 0
        while (l1 != None and l2 != None):
            cur = carryover + l1.val + l2.val
            if cur >= 10:
                carryover = 1
                digit = cur - 10
                newHead.next = ListNode(digit)
            else:
                carryover = 0
                newHead.next = ListNode(cur)
            newHead = newHead.next
            l1 = l1.next
            l2 = l2.next
        # if there's a carryover, of 1 at the end, add to the end
        if carryover == 1:
            newHead.next = ListNode(carryover)
        return dummy.next
            
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Revisited 9/30/2024
        This solution is improved and doesn't use any intermediate arrays
        https://neetcode.io/problems/add-two-numbers

        because the numbers are stored in reverse order, we can start adding the two digits
        starting from the beginning of each linked list, as this is the same order as we'd do 
        by-hand addition.

        track a carryover at 0, and whenever we add the values + existing carryover, 
        check if the sum >= 10
        if so, the value we set is 10 - 10, and the carryover is 1. If the sum is < 10,
        we just set the value as the sum and set the carryover to 0

        In the case we finish iterating and there's still carryover,
        set a remaining next node with a value of 1

        In the case the linked lists are not the same length, it's easier to pad the shorter
        linked list with nodes with value 0 to make edge case handling easier. So I would first
        iterate through both linked lists until you get to the last non-null value, and as the other LL continues,
        I'd add new list nodes onto the shorter linked list with value 0.
        """
        tmp1 = l1
        tmp2 = l2

        # get to the last non-null value of each linked list
        while (tmp1.next and tmp2.next):
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        # pad the shorter linked list with zeroes to prevent edge cases
        # when one linked list is longer than the other while adding
        if tmp1.next == None and tmp2.next != None:
            while (tmp2.next != None):
                tmp1.next = ListNode(0)
                tmp1 = tmp1.next
                tmp2 = tmp2.next
        elif tmp1.next != None and tmp2.next == None:
            while (tmp1.next != None):
                tmp2.next = ListNode(0)
                tmp2 = tmp2.next
                tmp1 = tmp1.next

        # begin performing addition,
        # tracking carryover. sum at each point is always carryover + the two values
        dummy = ListNode()
        cur = dummy
        carryover = 0
        while (l1 != None and l2 != None):
            sumVal = carryover + l1.val + l2.val
            newNode = None
            if (sumVal >= 10):
                newNode = ListNode(sumVal - 10)
                carryover = 1
            else:
                newNode = ListNode(sumVal)
                carryover = 0
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        # if there's still carryover, set the next node to be a new node with the carryover value 
        if (carryover > 0):
            cur.next = ListNode(carryover)
        return dummy.next
            
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
                
                
            
