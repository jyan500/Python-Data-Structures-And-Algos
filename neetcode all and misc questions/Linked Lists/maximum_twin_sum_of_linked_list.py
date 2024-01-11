# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Concept:
        1) The twin nodes are in a similar sequence to the way you'd check
        a palindrome in a linked list
        
        1 -> 2 -> 2 -> 3 
        you start with the two inwards ones (2 + 2), and then go outwards (1 + 3)
        
        to do this, find the middle of the linked list
        and then reverse the second half
        
        add the sums together at each point and find the max

        https://www.youtube.com/watch?v=doj95MelfSA&ab_channel=NeetCodeIO
        
        """
        
        def split(head):
            slow = head
            fast = head.next
            while (fast != None and fast.next != None):
                slow = slow.next
                fast = fast.next.next

            return slow
    
        def reverse(head):
            prev = None
            while (head != None):
                curr = head
                head = head.next
                curr.next = prev
                prev = curr
            return prev
        """
        1 2 3 4 5
        
        curr = 1
        head = 1
        
        curr = 1
        head = head.next = 2
        curr.next = None
        prev = 1
        
        1 -> None
        
        curr = 2
        head = head.next = 3
        curr.next = 1
        prev = 2
        
        2 -> 1 -> None
        """
        
        """
        split the list down the middle
        after split, this will be one node "before" the true middle of the linked list
        so we save the next value in tmp, set the next value to 0, and then set mid to tmp
        """
        mid = split(head)
        tmp = mid.next
        mid.next = None
        mid = tmp
        
        mid = reverse(mid)
        
        maxSum = float("-inf")
        while (head != None and mid != None):
            maxSum = max(head.val+mid.val, maxSum)
            head = head.next
            mid = mid.next
        return maxSum