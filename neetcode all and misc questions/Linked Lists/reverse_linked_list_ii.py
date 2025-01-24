# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        save the original head
        iterate through the head
            save the previous node right before the left node
            find the left node within the LL and save the pointer here
            find the right node, and then save the remainder of the LL after the right node

        apply the reverse LL algorithm starting from the left node, until the right node
        
        set the previous node right before to the left
        iterate all the way to the end of the new LL and set it to the remainder

        Note that in the edge case where left == right, just return head,

        The other edge case is when left == 1. In this case, there's nothing that occurs before left,
        so we just reverse everything up to the right node.
        And then attach the end of the reversedHead to the remainder of the LL after the right node.
        
        Time: O(N)
        Space: O(1)
        """
        if left == right:
            return head
        copy = head
        prev = None
        curr = None
        startLeft = None
        i = 1
        while (copy != None):
            if i + 1 == left:
                # cut the original head to be one node before the left.
                temp = copy.next
                startLeft = temp
                copy.next = None
                copy = temp
            elif i == right:
                # save the pointer of the node immediately after the right node
                startRight = copy.next
                copy.next = None
                break
            else:
                copy = copy.next
            i += 1
        # if we're starting at i = 1, then there's nothing that comes before left,
        # so we start at head instead
        if not startLeft:
            startLeft = head
        reversedHead = None
        while (startLeft != None):
            curr = startLeft
            startLeft = startLeft.next
            curr.next = reversedHead
            reversedHead = curr
        # if left > 1, there's a portion of the linked list before the left node
        # which is the head, we iterate to the end of the head and then set next
        # to the reversed portion.
        # and then continue iterating, and once it's hit the end again,
        # set the next to the pointer after the right node
        if left > 1:
            copy = head
            while (copy.next != None):
                copy = copy.next
            copy.next = reversedHead       
            while (copy.next != None):
                copy = copy.next
            copy.next = startRight
            return head
        # however, if left == 1, then we can skip the first part and just start
        # from the reversedHead instead since there's nothing before the left node,
        # just iterate to the end of the reversed head, and set it to the pointer
        # after the right node
        copy = reversedHead
        while (copy.next != None):
            copy = copy.next
        copy.next = startRight
        return reversedHead

