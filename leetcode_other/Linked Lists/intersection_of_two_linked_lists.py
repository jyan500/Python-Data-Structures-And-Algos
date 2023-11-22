'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Revisited on 11/22/2023
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Using O(M+N) time and O(N) space
        1) Keep a hashmap of the memory address to the node
        2) If the second node ever hits the same address, we've found the intersection
        """
#         lookup = dict()
#         while (headA != None):
#             lookup[id(headA)] = headA
#             headA = headA.next
#         while (headB != None):
#             if id(headB) in lookup:
#                 return headB
#             headB = headB.next
        """
        O(M+N) time and O(1) Space
        1) Figure out the lengths of both linked lists first
        2) Then, find the difference between the lengths (say len(m) - len(n)),
        and then iterate through the longer list by len(m) - len(n), such that the pointers
        at both lists are now aligned, and we can iterate through both lists together
        3) if the nodes at list m and n have equal id, then this is an intersection
        """
        lenA = 0
        lenB = 0
        curA = headA
        curB = headB
        while (curA != None):
            lenA += 1
            curA = curA.next
        while (curB != None):
            lenB += 1
            curB = curB.next
        # figure out which list is longer
        if lenA != lenB:
            longer = lenA if lenA > lenB else lenB
            shorter = lenA if lenA < lenB else lenB
            difference = longer - shorter
            for _ in range(difference):
                if longer == lenA:
                    headA = headA.next
                else:
                    headB = headB.next
        while (headA != None and headB != None):
            if id(headA) == id(headB):
                return headA
            headA = headA.next
            headB = headB.next
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            O(N) Time and O(1) space
            1. get the lengths of the two lists at with one pass over each linked list
            2. if len(A) > len(B), we need to increment headA to the next node and decrease the length of A
               however if (len(B) > len(A), we need to increment headB to the next node instead, and decrease length of B
               the goal is to start the head of each at the same length
            3. iterate over both linked lists, and start comparing if the current node is the same 
            as the other, if so return True
            https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/219028/Python-easy-%22len%22-solution-(w-comments)
        '''
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        if (lenA > lenB):
            while (lenA > lenB):
                headA = headA.next
                lenA -=1
        else:
            while (lenB > lenA):
                headB = headB.next
                lenB -= 1
        
        while (headA != None):
            if (headA == headB):
                return headA
            headA = headA.next
            headB = headB.next
            
        return None 

    ## helper function to get the length of linked list given the head
    def getLength(self,head: ListNode):
        length = 0
        while (head != None):
            length += 1
            head = head.next
        return length
    ## My Initial approach using a hashmap
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
            Time Complexity: O(2N) (two separate iterations), which is still O(N)
            Space Complexity: O(N), stores the nodes of one of the linked lists
            1. iterate through headA, map the ids of the nodes in headA to the headA node in our dict
            2. iterate through headB 
            3. check if the id of the node in headB is already in our hashmap, if so then we've found the intersection
        '''     
        node_id_map = dict()
        cur1 = headA
        ## map the ids of the node to the actual node in our dict
        while (cur1 != None):
            
            node_id_map[id(cur1)]=cur1
            cur1 = cur1.next
        cur2 = headB
        ## while iterating through the second list, check if the id of the node
        ## is already in our hashmap, if so then we've found the intersection
        while (cur2 != None):
            if (id(cur2) in node_id_map):
                return node_id_map[id(cur2)]
            cur2=cur2.next
        return None
        '''
            Test case 
            node_id_map = {}
            cur1 = headA
            cur1 = 4
            node_id_map = {'1':node 4}
            cur1 = cur1.next
            cur1 = 1
            node_id_map = {'1':node 4, '2' : node 1}
            cur1 = cur1.next
            cur1 = 8
            node_id_map = {'1':node4,'2':node1,'3':node8}
            cur1= 4
            node_id_map = {'1':node4,'2':node1,'3':node8,'4':node4}
            cur1 = 5
            node_id_map = {'1':node4,'2':node1,'3':node8,'4':node4, '5':node5}

            cur2 = headB
            cur2 = 5
        '''
   
    
    
    
    
    
                
                