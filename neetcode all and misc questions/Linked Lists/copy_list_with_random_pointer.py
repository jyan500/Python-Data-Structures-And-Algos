"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
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
        https://neetcode.io/problems/copy-linked-list-with-random-pointer
        Revisited 9/30/2024
        This solution appears to be cleaner than my last solution, using only 2 maps instead of 3

        2 Hashmaps:
        hashmap #1: the key is the old pointer memory address, and the value
        is its new LL node.
        hashmap #2: the new LL memory address is mapped to old Node
        create a new linked list with the next nodes, at the same time,
        we build hashmap #2, mapping id(newNode) to old node and hashmap #1, mapping id(old node) to newNode
        Loop through the new linked list again, but this time, call id() on the new linked list node,
        and use the id access hashmap #2 to find the old counterpart. Then, use the id() of the old counterpart's random pointer
        to access hashmap #1, which will help determine which new LL node the random pointer
        should point to. 
        Note that if the old counterpart's random pointer is pointing to None, just set the new node's random
        to be None as well so we don't call id() on None
        """
        temp1 = head
        newList = Node(0)
        map1 = {}
        map2 = {}
        ptr = newList
        while (temp1 != None):
            newNode = Node(temp1.val)
            ptr.next = newNode
            map2[id(newNode)] = temp1
            map1[id(temp1)] = newNode
            ptr = ptr.next
            temp1 = temp1.next
        temp2 = newList.next
        while (temp2 != None):
            old = map2[id(temp2)]
            if (old.random):
                newValForRandom = map1[id(old.random)]
                temp2.random = newValForRandom
            else:
                temp2.random = None
            temp2 = temp2.next
        return newList.next

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
        