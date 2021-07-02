'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

https://leetcode.com/problems/linked-list-cycle

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	## first attempt, put the ids of the listnodes into hashmap, and check if we've visited the node before
    def hasCycle(self, head: ListNode) -> bool:
        root = head
        visited = dict()
        while (root != None):
            if (visited.get(root.val) != None):
                if (id(root) == visited[root.val]):
                    return True
                else:
                    visited[root.val] = id(root)
            else:
                visited[root.val] = id(root)
            root = root.next
        return False


    ## most efficient version is Floyd's cycle finding algorithm
    ## Traverse linked list using two pointers
    ## move one pointer (slow) by one, and another pointer (fast) by two
    ## if the two pointers meet at the same node, then there is a loop. If the pointers do not meet, then the linkedlist doesn't have a loop
    def floydCycleAlgorithm(self, head: ListNode) -> bool:
    	p1 = head
        p2 = head
        ## since we move the fast pointer (p2) by two, make sure that the current and next are not null
        while (p1 != None and p2 != None and p2.next != None):
            p1 = p1.next
            p2 = p2.next.next
            if (id(p1) == id(p2)):
                return True
        return False

            
  