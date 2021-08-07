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
                    

        