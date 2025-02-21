""" 
    Revisited on 2/20/2025
	Hashset = Array, where each index contains a linked list in order to 
	handle collisions where we have two keys that hash to the same value

    Because at most 10^4 calls will be made, assuming these were all "add" operations,
    we'd set the upperbound to 10^4
    
    We use the key % 10^4 as our hash value, so that way when we add an item,
    whether it's 1 or 10001, both will map to the index 1 so we can handle collisions

    O(1) add on average (if there's too many collisions, this could be O(N) at worst)
	O(N) Time

    Add:
    Get the index using key % len(s)
    Iterate to the end of the linked list (head.next != None) and add a new node
    If the next node has a value == key param, we return since we don't want a duplicate value in our hashset

    Remove:
    Get the index using key % len(s)
    Iterate to the end of the linked list (head.next != None)
    If the next node has a value == key param, we set the current head's next equal to the head.next.next so it 
    skips the next node

    Contains:
    Similar to remove, except if the next node's value == key param, we just return True 
    
    
"""

class ListNode:
    def __init__(self, value = None, n = None):
        self.value = value
        self.next = n
        
class MyHashSet:

    def __init__(self):

        self.s = [ListNode(None) for i in range(10**4)]

    def add(self, key: int) -> None: 
        index = key % len(self.s)
        head = self.s[index]
        while (head.next != None):
            if head.next.value == key:
                return 
            head = head.next
        head.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        index = key % len(self.s)
        head = self.s[index]
        while (head.next != None):
            if head.next.value == key:
                head.next = head.next.next
            else:
                head = head.next
    
    def contains(self, key: int) -> bool:
        index = key % len(self.s)
        head = self.s[index]
        while (head.next != None):
            if head.next.value == key:
                return True
            head = head.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)