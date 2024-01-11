# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        A slightly more optimal approach that doesn't require finding the length
        first
        O(N) Time and O(1) Space, by NeetCode:
        https://www.youtube.com/watch?time_continue=315&v=4LsrgMyQIjQ&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MjM4NTE&feature=emb_title&ab_channel=NeetCodeIO
        
        1) By using two pointers, we use the first pointer to find where the first index where k needs to swap, this would be k - 1.
        2) using the second pointer, we then begin from where the first pointer was, and then iterate to the last node of the list (where cur.next != None). This ensures that the second pointer will always be 
        k distance from the end, which would be where we need to swap with our first pointer.
        
        1 -> 2 -> 3 -> 4 -> 5
        k = 2
        
        2 would be the first pointer
        left = 2
        cur = 2
        right = head (which is 1)
        
        by the time cur reaches the end,
        1 -> 2 -> 3 -> 4 -> 5
                      right cur
        
        right would be at 4, which is the correct place to swap
        
        swaps values of 2 and 4 for the right answer.
        """
        cur = head
        # this gives us the left side to swap
        for i in range(k-1):
            cur = cur.next
        left = cur
        right = head
        # by the time cur reaches the end of the list, since we have the "right" pointer starting from
        # head, it would've reached the proper 2nd value (which is k distance away)
        while (cur.next):
            cur = cur.next
            right = right.next
        left.val,right.val=right.val,left.val
        return head
        
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Initial Approach:
        1) find the length of the linked list
        2) calculate the indices in which we need to swap between using the length of the linked list
          k1 = k - 1
          k2 = lenOfList - k
        3) Use dummy pointer strategy and have a previous value, where as soon as we reach
        either k1 or k2, we hold previous constant and don't increment it. As soon as we reach the other
        side (if k1, then k2 or vice versa), then we perform the swap of cur's value with prev's value.
        Once we've swapped, we can break out of the loop
        
        O(N) Time O(1) Space
        """
        lenOfList = 0
        cur1 = head
        while (cur1):
            lenOfList += 1
            cur1 = cur1.next
      
        k1 = k - 1
        k2 = lenOfList - k
        if lenOfList == 1 or k1 == k2:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        i = 0
        reached = False
        while (cur):
            if i == k1 or i == k2:
                if not reached:
                    reached = True
                    cur = cur.next
                    prev = prev.next
                else:            
                    # prev should be on the proper value where it can be swapped with cur
                    prev.val, cur.val = cur.val, prev.val
                    # once we're swapped, we can just break
                    break
            # if i is between the range of k1 or k2, don't increment prev
            elif k1 < i < k2 or k2 < i < k1:
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
            i += 1
        return dummy.next
            
            