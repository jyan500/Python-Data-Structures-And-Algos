# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://www.youtube.com/watch?v=1UOPsfP85V4&t=548s&ab_channel=NeetCode
        def kthNode(cur, k):
            while (cur and k > 0):
                cur = cur.next
                k -= 1
            return cur
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        while (True):
            kth = kthNode(groupPrev, k)
            if (not kth):
                break
            # if you use kth.next instead of groupNext in the conditional
            # for the while loop below, it breaks, so you have to save the value of kth.next before reversing. I think what's happening is that 
            # kth.next value is being updated within the loop (you can see that if you print kth.next in the while loop below), so you need to save its initial value
            groupNext = kth.next
            prev = kth.next
            curr = groupPrev.next
            while (curr != groupNext):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
        