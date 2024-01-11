"""
O(N) Time 
1) Traverse linked list to find the length
2) Calculate the middle, if the length is even, we want to return the second middle,
so mid + 1
3) Traverse the linked list again until we reach the middle and return
"""
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
O(N) Time O(1) Space
11/22/2023
Using the cycle detection algorithm,
with slow and fast pointer.

If the fast pointer reaches the end of the list, that means it is an even number of nodes.
If it is none, that means it's odd number. In that case, we need to 
make sure to return the "second" middle node, so in the case of even numbered nodes,
return slow.next, and for odd numbered, return slow

Odd Numbered:

1 -> 2 -> 3 -> 4 -> 5 -> None
^    ^
slow fast

1 -> 2 -> 3 -> 4 -> 5 -> None
     ^         ^
    slow      fast

1 -> 2 -> 3 -> 4 -> 5 ->None
          ^               ^
         slow           fast

Here the middle is slow, so return slow

Even Numbered
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
^    ^
slow fast

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    ^          ^
    slow      fast

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
          ^              ^
          slow          fast

here, the proper middle is 4, so return slow.next instead of slow
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow.next if fast != None else slow

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = head
        lenList = 0
        while (cur1 != None):
            cur1 = cur1.next
            lenList += 1
        mid = (lenList - 1)//2
        if lenList % 2 == 0:
            mid += 1
        i = 0
        while(head != None):
            if i == mid:
                return head
            head = head.next
            i+=1
            