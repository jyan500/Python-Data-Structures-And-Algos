'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

https://leetcode.com/problems/sort-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Revisited on 9/8/2023
https://www.youtube.com/watch?v=TGveA1oFhrc&ab_channel=NeetCode

O(NLogN) time O(1) memory solution 
1) use merge sort by continually finding the middle of the linked list
until we reach a case with individual nodes
3) Apply adding two sorted linked lists (simplest case being two individual nodes)
"""
class Solution2:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(NLogN) time O(N) memory solution 
        1) convert to array
        2) sort
        3) convert back to linked list
        """
        # temp = []
        # p1 = head
        # while (p1):
        #     temp.append(p1.val)
        #     p1 = p1.next
        # temp.sort()
        # l = ListNode()
        # res = l
        # for i in range(len(temp)):
        #     res.next = ListNode(val=temp[i])
        #     res = res.next
        # return l.next
        """
        O(NLogN) time O(1) memory solution 
        1) use merge sort by continually finding the middle of the linked list
        until we reach a case with individual nodes
        3) Apply adding two sorted linked lists (simplest case being two individual nodes)
        """    
        
        def split(head1):
            # continually split
            l1 = head1
            l2 = head1.next
            # if the fast pointer has reached the end, the slow pointer will be at the middle of the LL
            while (l2 != None and l2.next != None):
                l1 = l1.next
                l2 = l2.next.next
            
            return l1
    
        def merge(head1, head2):
            l1 = head1
            l2 = head2
            newHead = ListNode()
            cur = newHead
            while (l1 and l2):
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return newHead.next

        
        # if we have null, or an individual node, return the node
        if not head or not head.next:
            return head
        left = head
        right = split(head)

        # because the middle of the linked list is one node to the left
        # of where we want to start the second half,
        # we need to set the next node to None to "disconnect" the two linked lists
        # and then set our new "right" so that it starts at the second half
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)


class Solution:
    ## O(NLogN) time and O(N) space
    ## can we solve it in O(NLogN) time but O(1) memory?
    def sortList(self, head: ListNode) -> ListNode:
        # if (not head):
        #     return None
        # a = []
        # cur = head
        # while (cur != None):
        #     a.append(cur.val)
        #     cur = cur.next
        # a = sorted(a)
        # head = ListNode()
        # cur = head
        # for i in range(len(a)):
        #     cur.val = a[i]
        #     if (i != len(a)-1):
        #         cur.next = ListNode()
        #         cur = cur.next
        # return head
        
        '''
        O(NLogN)
        The O(1) space solution makes use of merge sort on the linked list
        '''
        ## if head is None or head.next is None, that means that we've split
        ## up this particular half so that its only a single node, so we just return the node
        if (head == None or head.next == None):
            return head
        ## get the middle of our current linked list in the recursive call
        mid = self.getMid(head)
        ## head should now be modified in memory so that it only contains the left half
        left = self.sortList(head)
        ## mid should now contain the start of the right half
        right = self.sortList(mid)
        
        ## once we've received a left half (just one node initially), and a right half (just one node initially)
        ## we merge the two sorted lists and return the reference (dummy.next) to the merged list
        ## this process will backtrack recursively so that it will progressively merge larger and larger lists
        return self.merge(left,right)
        
        
    def getMid(self, head):
        slow = head
        fast = head
        prev = head
        ## once the fast pointer reaches the end of the list, because it increments
        ## through the pointer twice as fast, then the node 
        ## we also need a previous pointer so that we can get the node that is right before slow
        ## in order to cut the list
        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        ## the midpoint will be where our slow node is located
        mid = slow
        ## and we cut the list in half by doing prev.next = None, so head will now stop in the middle
        prev.next = None
        return mid
    
    def merge(self, left, right):
        dummy = ListNode()
        head = dummy
        ## apply the algorithm for merge two sorted linked lists
        while (left != None and right != None):
            if (left.val < right.val):
                ## if the left half's node value is less than the right half,
                ## we set head.next to the remainder of the left half
                head.next = left
                left = left.next
                head = head.next
            elif (right.val < left.val or right.val == left.val):
                ## if the right half's node value is less than the right half or equals
                ## we set head.next to the remainder of the right half
                head.next = right
                right = right.next
                head = head.next
        ## after iteration, if the left half is longer than the right half, set the remainder of the list to the left half
        if (left != None):
            head.next = left     
        ## after iteration, if the right half is longer than the left half, set the remainder of the list to the right half
        elif (right != None):
            head.next = right
            
        return dummy.next
                    

        