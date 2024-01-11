"""
https://leetcode.com/problems/rotate-list/
O(N) time
O(N) space
1) put LL values in list
2) rotate the list using the rotation factor to get new indices.
    rotation factor to determine new index is always i + k % len(list)
3) create new linked list using the rotated version

Revisit at some point to figure out the in-place version
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        
        """
        cur = head
        l = []
        while (cur):
            l.append(cur.val)
            cur = cur.next
        # rotate list
        rotated = l.copy()
        for i in range(len(l)):
            newIndex = (i + k) % (len(l))
            rotated[newIndex] = l[i]
        dummy = ListNode(0)
        head = dummy
        # create new linked list using rotated version
        for i in range(len(rotated)):
            head.next = ListNode(rotated[i])
            head = head.next
        return dummy.next