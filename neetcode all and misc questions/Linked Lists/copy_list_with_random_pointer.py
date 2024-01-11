"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        the node's values don't have to be unique, so we can't
        rely on the node's values, we can use the memory addresses instead (id function)
         
        Key Concepts:
        1) We need three hashmaps:
        
        oldAddresses = mapping old node id to it's old random id (if old node doesn't have a random, map it to null)
        newAddresses = map the newNode id to the oldNode id
        
        idToNode = map the oldNode id to the actual newNode itself 
        
        2) Loop through the old linked list, creating the new linked list using the dummy node strategy, and mapping all the appropriate
        values into their hashmaps
        
        3) Using the newly created linked list, we take the id of each node, 
           take the new node id and find the old node id using newAddresses
           
           Then, take the old node id and find it's old random node id using oldAddresses
           
           Then, take the old random node id and find it's new node equivalent using idToNode
           
           Then, map our new node's random to the equivalent found in idToNode
           
           If the old random node id was None, just map new node's random to None
         
         4) Return the new head
           
         Time complexity: O(N)
         Space Complexity: O(N)
        
        
        """
        oldAddresses = dict()
        newAddresses = dict()
        idToNode = dict()
        oldHead = head
        dummy = ListNode(0)
        newHead = dummy
        # map the old node to it's old random memory address
        # map the new node id to the old node id
        # map the old node id to it's new node equivalent 
        while (oldHead != None):
            oldNodeAddress = id(oldHead)
            if (oldHead.random):
                oldRandomAddress = id(oldHead.random)
            else:
                oldRandomAddress = None
            oldAddresses[oldNodeAddress] = oldRandomAddress
            newNode = ListNode(oldHead.val)
            newHead.next = newNode
            newAddresses[id(newNode)] = oldNodeAddress
            idToNode[oldNodeAddress] = newNode
            oldHead = oldHead.next
            newHead = newHead.next
        # go back and map the new random nodes on the newly copied linked list
        resHead = dummy.next
        cur = resHead
        while (cur):
            idOldNode = newAddresses[id(cur)]
            oldRandomAddress = oldAddresses[idOldNode]
            if oldRandomAddress != None:
                newNode = idToNode[oldRandomAddress]
            else:
                newNode = None
            cur.random = newNode
            cur = cur.next
        return resHead
        