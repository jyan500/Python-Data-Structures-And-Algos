"""
https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
https://www.youtube.com/watch?v=o811TZLAWOo&ab_channel=NeetCode

Key Concepts:
1) We look at the linked list in pairs, so we make sure both the current
and current.next nodes are not none
2) Use a dummy node to avoid edge cases (like empty linked lists)
3) We always look at a previous and curr value, and then we perform
a swap, set the dummy to point at the new head, and then advance
curr to be next.next, so we get to the next pair

Time Complexity: O(N)
Space Complexity: O(1)

Example:
1 -> 2 -> 3 -> 4 -> None

Dummy = 0
prev = 0, curr = 1

first iteration
    nextPair = 3
    second = 2

    # 2 now points to 1 
    second.next = 1 

    # 1 now points to 3
    curr.next = 3
    
    # 0 now points to 2
    prev.next = 2

    prev = 1
    curr = 3

result: 
0 -> 2 -> 1 -> 3 -> 4 -> None
          ^    ^
          |    |
         prev curr

second iteration:
    nextPair = None
    second = 4
    
    # 4 now points to 3
    second.next = 3

    # 3 now points to None
    curr.next = None

    # 1 now points to 4
    prev.next = 4

    prev = 3
    curr = None

0 -> 2 -> 1 -> 4 -> 3 -> None
                    ^      ^
                    |      |
                   prev   curr

Because curr is None, the iteration ends

Dummy stores a reference to the beginning of this new
linked list that the prev pointer just built, so to get the start
of this linked list, return dummy.next to get

2 -> 1 -> 4 -> 3 -> None





"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # we need to look at nodes in pairs, so current and current next
        # can't be None
        prev, curr = dummy, head
        while (curr != None and curr.next != None):
            # save ptrs
            nextPair = curr.next.next
            second = curr.next
            
            # reverse pairs
            second.next = curr
            curr.next = nextPair
            
            # set the dummy to point to the new head (which was the second node
            # in our pair,
            # but is now actually the first node now 
            prev.next = second
            
            # update ptrs
            # we point prev to be the formerly first node in our pair (now the second
            prev = curr 
            # curr will be set to the first node of the next pair
            curr = nextPair
            
        return dummy.next