"""
https://leetcode.com/problems/odd-even-linked-list/
https://leetcode.com/problems/odd-even-linked-list/solution/

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) time but O(N) space, can we do it in O(1) space?
#         if not head:
#             return None
#         # take two separate linked lists and then splice the end of them together
#         odds = ListNode(0, None)
#         evens = ListNode(0, None)
#         evensCurr = evens
#         oddsCurr = odds
        
#         ptr1 = head
#         i = 0
#         while (ptr1 != None):
#             if i % 2 == 0:
#                 evensCurr.next = ListNode(ptr1.val)
#                 evensCurr = evensCurr.next
#             else:
#                 oddsCurr.next = ListNode(ptr1.val)
#                 oddsCurr = oddsCurr.next
#             ptr1 = ptr1.next
#             i+=1

#         ptr2 = evens.next
#         while (ptr2.next != None):
#             ptr2 = ptr2.next
#         ptr2.next = odds.next
#         return evens.next

        # O(N) time O(1) space, same idea as above modifies head directly
        if not head:
            return None
        
        odd = head
        even = head.next
        evenHead = even
        while (even != None and even.next != None):
            # set the odd numbered node to be the next
            # odd numbered node
            odd.next = even.next
            # advance odd
            odd = odd.next
            # set the even numbered node to be the next
            # even numbered node, which happens to be one position
            # after odd, since we just advanced odd
            even.next = odd.next
            # advance even node
            even = even.next
        # set the end of the odd node list to the head of the even node list
        odd.next = evenHead
        return head