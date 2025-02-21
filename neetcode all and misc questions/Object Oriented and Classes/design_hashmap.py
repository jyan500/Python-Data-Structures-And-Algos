"""
    Very similar to design hash set problem

    Hashmap = Array, where each index contains a linked list in order to 
    handle collisions where we have two keys that hash to the same value

    Because at most 10^4 calls will be made, assuming these were all "add" operations,
    we'd set the upperbound to 10^4
    
    We use the key % 10^4 as our hash value, so that way when we add an item,
    whether it's 1 or 10001, both will map to the index 1 so we can handle collisions

    O(1) add on average (if there's too many collisions, this could be O(N) at worst)
    O(N) Time

    Put:
    Get the index using key % len(s)
    Iterate to the end of the linked list (head.next != None) and add a new node
    However, if there exists a key in the linked list already, we update the existing value in the key pair 
    and break out of the loop

    Remove:
    Get the index using key % len(s)
    Iterate to the end of the linked list (head.next != None)
    If the next node has a value == key param, we set the current head's next equal to the head.next.next so it 
    skips the next node

    Get:
    Similar to remove, except if the next node's key == key param,
    we return the value. If we can't find the key, return -1

    Time Complexity:
    O(1) on average (O(N) at worst though depending on the amount of collisions)

    O(N) time
    
    
"""

# revisited on 2/20/2025
class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.value = value
        self.key = key
        self.next = next
    def __str__(self):
        return f"value: {self.value} next: {self.next}"

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.hashmap)
        head = self.hashmap[index]
        while (head.next):
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next
        head.next = ListNode(key, value) 

    def get(self, key: int) -> int:
        index = key % len(self.hashmap)
        head = self.hashmap[index]
        while (head.next):
            if head.next.key == key:
                return head.next.value
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.hashmap)
        head = self.hashmap[index]
        while (head.next):
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
class ListNode:
    def __init__(self, k= None, v= None, n = None):
        self.keyPair = (k, v)
        self.next = n 
class MyHashMap:

    def __init__(self):
        self.map = [ListNode(None,None) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.map)
        cur = self.map[index]
        while (cur.next != None):
            k, v = cur.next.keyPair
            # if a key pair already exists, update the key pair
            if k == key:
                cur.next.keyPair = (key, value)
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % len(self.map)
        cur = self.map[index]
        while (cur.next != None):
            k, v = cur.next.keyPair
            if k == key:
                return v
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        cur = self.map[index]
        while (cur.next != None):
            if cur.next.keyPair[0] == key:
                cur.next = cur.next.next
            else:
                cur = cur.next
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)