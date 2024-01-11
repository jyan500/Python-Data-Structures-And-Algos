# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Very similar logic to remove linked list elements leetcode problem
        
        Key Concepts:
        1) Because the list is already sorted,
        we know that if the previous value == current value, this is a duplicate
        2) Set a dummy.next node to head, set a current pointer to head, and then set a prev pointer to dummy so we can keep a prev pointer that is always behind the current pointer
        3) While iterating through, if the prev pointer's value is the same as the current pointer's value,
        we set the prev.next = cur.next, and then increment cur = cur.next. Note that we don't increment
        prev's pointer though until the prev.val != cur.val in the case we run into consecutive elements
        that are the same.
        
        1 -> 1 -> 1 -> 2 -> 3 -> 3
        
        prev = None
        cur = 1       
          
        0 -> 1 -> 1 -> 1 -> 2 -> 3 -> 3
             ^    ^
            prev cur
        
        prev.val == cur.val,
        prev.next = cur.next
        
         0 -> 1 -> 1 -> 1 -> 2 -> 3 -> 3
              prev      ^
                       cur
                       prev.next
        Notice how prev still refers to the first "1" that we encountered
        
        We repeat where prev.val == cur.val,
        so we set cur = 2, and prev.next is now also 2
        
        0 -> 1 -> 1 -> 1 -> 2 -> 3 -> 3
              prev          ^
                           cur
                          prev.next
        
        Now prev.val != cur.val, so we set cur = cur.next, prev = prev.next
        
         0 -> 1 -> 1 -> 1 -> 2 -> 3 -> 3
                             ^    ^
                            prev  cur
        
        
       
        """
        dummy = ListNode(None)
        dummy.next = head
        cur = head
        prev = dummy
        while (cur != None):
            if prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
        