# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/remove-nodes-from-linked-list/
        O(N) time and O(N) space solution
        1) iterate through the linked list, adding elements to a monotonic decreasing stack,
        such that all elements are strictly decreasing, which is what the problem states,
        since we have to remove any elements with a greater value anywhere to the right side of it
        2) reconstruct a new linked list using the two elements
        
        A slightly better solution (Which is still O(N)), would be to store the nodes (instead of just the values) on the stack, such that you can simply just re-connect the nodes by setting their next values
        instead of making a new linked list
        """
        stack = []
        cur = head
        while (cur):
            while (stack and cur.val > stack[-1].val):
                stack.pop()
            stack.append(cur)
            cur = cur.next
        for i in range(len(stack)-1):
            stack[i].next = stack[i+1]
        return stack[0]
        