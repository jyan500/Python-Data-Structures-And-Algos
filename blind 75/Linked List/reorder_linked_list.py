'''
https://leetcode.com/problems/reorder-list/
https://www.youtube.com/watch?v=To_uAJRu8NQ&ab_channel=SaiAnishMalla
https://www.youtube.com/watch?v=XIJMdQUzs-I&ab_channel=TimothyHChang
https://www.youtube.com/watch?v=xRYPjDMSUFw&t=611s&ab_channel=NickWhite
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Revisited on 9/30/2024 with the same solutions as below
        https://neetcode.io/problems/reorder-linked-list
        find the middle of the linked list and cut the linked list in half
        reverse the 2nd half
        interchange the two nodes from each linked list
        """
        # find middle using two pointers
        # slow pointer starts at head, but fast pointer starts at head.next
        # move fast pointer twice as fast as the slow, so once fast becomes None
        # the slow pointer should be in the middle

        slow = head
        fast = head.next

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        # cut the linked list in half by setting the second half to be
        # slow.next, and then setting slow.next to be None
        secondHalf = slow.next
        slow.next = None

        prev = None
        curr = secondHalf

        while (curr != None):
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        
        curHead = head
        curPrev = prev
        while (curHead != None and curPrev != None):
            tmp1 = curHead.next
            tmp2 = curPrev.next
            curHead.next = curPrev
            curPrev.next = tmp1
            curHead = tmp1
            curPrev = tmp2

"""
Revisited 9/25/2023
https://www.youtube.com/watch?v=S5bfdUTrKLM&ab_channel=NeetCode

1) find the middle of the linked list
2) split into two parts, reverse the second half
3) merge the two parts together:

For the merge, we modify head directly by
1) Saving the "original" next values for the pointers for both halves
3) For the pointer for the first half, we want to set that to the remainder of the second half
4) For the pointer for the second half, we set that to the "next" value for the first half
5) advance to the "original" next

example:
after splitting 1 -> 2 -> 3 -> 4 -> 5 and then reversing
1 -> 2 -> 3
5 -> 4

------ 1st iteration -------
tmp1, tmp2 = 2, 4

curHead.next = curPrev, which will set 1 -> 5
curPrev.next = tmp1, which sets 5 -> 2

curHead = tmp1, sets to 2
curPrev = tmp2, sets to 4

------ 2nd iteration --------
tmp1, tmp2 = 3, None

curHead.next = curPrev, which will set 1 -> 5 -> 2 -> 4
curPrev.next = tmp1, which sets 4 -> 3

curHead = tmp1, sets to 3
curPrev = tmp2, sets to None

curPrev is now None

1 -> 5 -> 2 -> 4 -> 3

is the final answer


"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        # split the list down the middle by setting slow.next equal to None
        # so that head only goes up to slow
        # save the remainder of the LL starting from slow.next in the temp variable

        secondHalf = slow.next
        slow.next = None
        
        # reverse the list starting from temp      
        prev = None
        while (secondHalf != None):
            curr = secondHalf
            secondHalf = secondHalf.next
            curr.next = prev
            prev = curr
        
        # merge
        curHead = head
        curPrev = prev
        while (curHead != None and curPrev != None):

            tmp1, tmp2 = curHead.next, curPrev.next
            curHead.next = curPrev
            curPrev.next = tmp1
            
            curHead = tmp1
            curPrev = tmp2
            
        return head
        

from collections import deque
class Solution:
	# O(N) time, O(N) space solution, can we do better in terms of space?
	## create a queue
    ## loop through the linked list and push the nodes onto the queue
    
    ## when looping through the linked list again, alternate popping off the 
    ## the queue from the front/back depending on whether the number of node 
    ## we're currently on is odd/even
    
    ## set the node.next value equal to the popped node
	def reOrderList(self, head: ListNode) -> None:
        q = deque()
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while (cur != None):
            q.append(cur)
            cur = cur.next
        even = False
        cur = dummy
        while (q):
            node = None
            if (even):
                node = q.pop()
            else:
                node = q.popleft()
            print(node.val)
            node.next = None
            cur.next = node
            cur = cur.next
            ## XOR operation to flip False to True, and True to False
            even ^= True
        return head
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        ## There is a way to do this with O(1) Space
        ## Approach:
        ## find the middle node of the linked list
        ## reverse only the right half of the linked list
        ## merge the left and right half of the linked list together 
        
        ## to find the middle node, utilize a slow and fast pointer
        ## where the fast pointer moves two times as fast as the slow
        ## when the fast pointer reaches the end of the linked list
        ## the slow would now point to the middle node
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        
        ## slow is now pointing to the middle node
        
        ## now we reverse the second half of the linked list
        prev = None
        ## note that we point cur to the next node of slow,
        ## since we don't want to include the middle node in the reversal
        ## only the node after and onwards until the end
        cur = slow.next
        
        ## we need to separate the left and right half of the list by setting slow.next to be None
        slow.next = None
        while (cur != None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
       
        ## now we need to merge the left and the right halves together
        even = False
        cur = head
        head2 = prev
        while (head2 != None):
            ## similar to the reverse link list above, we make a temp to keep track of the current next 
            temp = cur.next
            ## set the current next to be equal to the right half of the linked list's head 
            cur.next = head2
            ## tricky part, we set cur to be equal to the right half of the linked list's head
            ## for example 1->2->3->4
            ## middle node is 2
            ## left half = 1->2 right half = 3->4, after reversal its right half = 4->3
            ## we set 1 first, then set cur = 4 (which is where prev is pointing to)
            cur = head2
            ## then, we set head2 to be temp, which is the current next
            ## for example, head2 is pointing to 4, but now we set it to 2
            head2 = temp
        return head
    

    # def printList(self, head: ListNode):
    #     s = ''
    #     cur = head
    #     while (cur != None):
    #         if (cur.next != None):
    #             s += str(cur.val) + '->'
    #         else:
    #             s += str(cur.val)
    #         cur = cur.next
    #     return s
      