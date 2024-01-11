'''
https://leetcode.com/problems/remove-linked-list-elements/
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


## Approach: 
-iterate through the linked list
-keep two pointers, we'll create a dummy node, where dummy.next is head
-one previous node which will be set to dummy
-one current node which is set to head
-if our current node val is equal to val
-set the previous node's next to be equal to the cur next
-in the case that cur.next is None, prev.next will be set to None as well
-in this case, since we always want previous to be one node behind cur, just increment cur
-otherwise, increment both prev and cur
-return dummy.next (rather than returning head) at the end to avoid cases like [7,6,7], val = 7 
-because we would need to delete head in this case since the head also contains the value we want to delete

(further test case explaning why the dummy node is needed below)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy
        
        while (cur != None):
            if (cur.val == val):
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
    
        '''
        test cases
        1: 1->2->6->3->4->5->6, val = 6
        dummy = 0
        cur = 1
        prev = 0
        0->1->2->6->3->4->5->6
        cur = 2
        prev = 1
        cur = 6
        prev = 2
        prev.next = 3
        increment cur to be 3
        continue
        prev still at 2
        cur at 3
        prev 3
        cur 4
        prev 4
        cur 5
        prev 5
        cur 6
        prev.next = None
        cur = cur.next
        cur is None so break out
        
        2: 7->7->7->7
        (this is where the dummy node comes in play)
        dummy = 0
        head = 7
        cur = 7
        prev = 0
        0->7->7->7->7
        
        cur.val == val, so we set prev.next = cur.next and increment cur
        prev = 0
        cur = cur.next, cur = 7
        prev.next = 7
        
        cur.val == val, so we set prev.next = cur.next and increment cur
        prev = 0
        cur = cur.next, cur = 7
        prev.next = 7
        
        cur.val == val, so we set prev.next = cur.next and increment cur
        prev = 0
        cur = cur.next, cur = 7
        prev.next = 7
        
        cur.val == val, so we set prev.next = cur.next and increment cur
        prev = 0
        cur = cur.next, (but cur is now None)
        prev.next = None (will also be set to None)
        
        cur = None, so breaks out of the loop
        as we can see head still points to the original 7,7,7,7
        because our prev value always stayed at 0, and we never called prev = prev.next to
        move us into the memory space where head begins, so the original head node is unchanged
        
        
        '''