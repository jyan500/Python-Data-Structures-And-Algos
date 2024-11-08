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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Revisited on 11/8/2024
        Merge Sort
        1) Split the lists in half
        2) Perform merge sorted lists algorithm
        """
        
        def mergeSort(head):
            def split(node):
                slow = node
                fast = node.next
                while (fast and fast.next):
                    slow = slow.next
                    fast = fast.next.next
                # slow will be the middle of the list
                return slow

            def merge(h1, h2):
                """
                example:
                1 -> 3
                2 -> 4
                cur = 0 -> null
                1 < 2, so we set cur.next to be 0 -> 1 -> 3 
                and then move, the temp1 pointer to 3
                cur = cur.next, so cur is now 1

                3 > 2, so we want to set cur.next to temp2 now
                0 -> 1 -> 2 -> 4

                temp2 = temp2.next, which brings from 2 to 4
                cur is now 2

                comparing temp1 to temp2, 3 < 4, so we now set cur.next to temp1 again, temp1 = temp1.next, is now null
                0 -> 1 -> 2 -> 3 -> null

                cur is now 3

                because temp1 is now null, we can set the remainder
                of list to temp2
                """
                temp1 = h1
                temp2 = h2
                dummy = ListNode(0)
                cur = dummy
                while temp1 and temp2:
                    # if the current val of temp1 is less,
                    # we can set the next value of cur to be 
                    # the remainder of list1
                    if temp1.val < temp2.val:
                        cur.next = temp1
                        temp1 = temp1.next
                    else:
                        cur.next = temp2
                        temp2 = temp2.next
                    cur = cur.next
                if temp1:
                    cur.next = temp1
                elif temp2:
                    cur.next = temp2
                return dummy.next
            if head.next:
                mid = split(head)
                second = mid.next
                # split in half
                mid.next = None
                firstHalf = mergeSort(head)
                secondHalf = mergeSort(second)
                merged = merge(firstHalf, secondHalf)
                return merged
            return head
        
        if head:
            return mergeSort(head)

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
                    

        