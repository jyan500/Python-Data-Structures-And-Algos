'''
https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Concept:
1) Use an ordered dict, where the dictionary retains the order when the keys are inserted
2) the idea is that we want to keep the most recently used items in the back of the dict
and the least recently used in the front, since when we add items, we'll just put them in the back
by default.
2) whenever we make a put or get to an existing key, we need to move that key to the back
to show that its been "recently used"
3) we also keep track of capacity, so if we try to put in an item and we've reached capacity,
just remove the first item in the dict

O(1) get and O(1) put
O(N) space
'''
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_items = 0
        self.cache = OrderedDict()
        ## hashmap to map the amount of usage to a set of nodes in the cache
        ## for example:
        ## {0: [1]} (put 1)
        ## {0: [1,2] (put 2)
        
        ## get 1, we need to update 1's usage to 1
        ## {0: [2], 1: [1]}
        ## put 3, were over capacity, we see that 2 is the one of the least usage so far
        ## so remove 2 from the 0 usage bucket
        

    def get(self, key: int) -> int:
        ## if getting an existing item, we need to remove it from its current place in the ordereddict
        ## and move to the back to show its the most recently used 
        if (key in self.cache):
            val = self.cache[key]
            del self.cache[key]
            ## this will append to the back since ordereddict retains the order in which keys are inserted
            self.cache[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print('key: ', key, 'value: ', value)
        ## remove the least recently used (which will be the front of the cache)
        if (self.num_items == self.capacity and key not in self.cache):
            ## get the key and value of the first item in the cache
            k, v = list(self.cache.items())[0]
            print('least recently used: ', k)
            ## delete it
            del self.cache[k]
            ## decrement num items by one
            self.num_items -= 1
            self.cache[key] = value
            # increment nums again
            self.num_items += 1  
            
        ## if we're updating an existing key
        elif (key in self.cache):
            ## bring that key to the front
            del self.cache[key]
            ## this will append to the back since ordereddict retains the order in which keys are inserted
            ## update with the new value
            self.cache[key] = value
        else:
            ## insert at the back
            self.cache[key] = value
            self.num_items += 1  
            
       

    '''
    capacity = 2
    get(2) = -1
    put key = 2 value = 6
    {2: 6}
    get(1) = -1
    put (1, 5)
    {2: 6, 1: 5}
    {2: 6, 1: 2}
    
    capacity = 2
    put (2,1) = {2:1}
    put (1,1) = {2:1,1:1}
    put (2,3) = {1:1, 2:3}
    put (4,1) = {2:3,4:1}
    get 1 = {2:3,4:1}
    get 2 = {4:1,1:1,2:3}
    
    
    
    '''
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)