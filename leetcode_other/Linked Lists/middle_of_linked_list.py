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
            