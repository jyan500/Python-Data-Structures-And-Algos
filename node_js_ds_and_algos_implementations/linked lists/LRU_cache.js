// node will be used to construct a doubly linked list
class Node {
    constructor(key, val){
        this.key = key
        this.val = val
        this.prev = null
        this.next = null
    }
}
/**
 * @param {number} capacity
 */
var LRUCache = function(capacity) {
    this.cap = capacity
    // to avoid time limit exceeded, we can't use Object.keys(this.cache),
    // so we have to manually track the current length of the cache instead
    this.length = 0
    this.cache = {} // map key to node
    this.left = new Node(0, 0)
    this.right = new Node(0, 0)
    // Left = least recently used
    // right = most recently used
    /*
      next
      -->
   []     []
      <-- 
      prev

    initialize two dummy nodes of key = 0, val = 0, and point at each other
    Note that whenever we add/remove nodes, we're always removing them BETWEEN
    these two dummy nodes
    */
    this.left.next = this.right
    this.right.prev = this.left
};

/* Helper functions to manipulate the doubly linked list, insert a node at the right */
LRUCache.prototype.insert = function(node){
    /*
    When inserting a node at the right to be the most "recently used",
    technically, this is one node BEFORE the right dummy node, so right.prev
    
               -->
        [1]          [3]
    right.prev       right
               <--
               
    node (2) between right.prev and right,
         -->     -->
    [1]      [2]      [3]
         <--     <--
    
    [1].next needs to point to 2
    [3].prev needs to point to 2

    [2].prev needs to point to 1
    [2].next needs to point to 3
    
    2 will now be considered the "most recently used"
    */
    let prev = this.right.prev
    let next = this.right
 
    prev.next = node
    next.prev = node
    
    // make sure the newly inserted node points back to the previous and next respectively
    node.prev = prev
    node.next = next
}

/* Helper functions to manipulate the doubly linked list, remove a node */
LRUCache.prototype.remove = function(node){
    /*
    when removing a node from a doubly linked list:
    
       -->   -->
    [1]   [2]   [3]
       <--   <--
    
    If node was the middle node (2),
    prev is referring 1,
    and next is referring to 3
    
    [1].next should now be 3
    [3].prev should now be 1,
    
    this causes [2] to no longer be referenced
    */
    let prev = node.prev
    let next = node.next   
    prev.next = next
    next.prev = prev
}

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (key in this.cache){
        // we need to update this value to be the most recent
        // by removing the node from the list...
        this.remove(this.cache[key])
        // and then re-inserting to be the most recently used
        this.insert(this.cache[key])
        return this.cache[key].val
    }
    return -1
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (key in this.cache){
        // we need to remove the existing node from our list
        this.remove(this.cache[key])
        --this.length
    }
    // create a new node
    this.cache[key] = new Node(key, value)
    this.insert(this.cache[key])
    ++this.length
    
    // if the cache's length exceeds capacity, we need to remove the 
    // least recently used
    if (this.length > this.cap){
        // find the least recently used which is the left most node that isn't the dummy node
        // which would be left.next
        let lru = this.left.next
        this.remove(lru)
        delete this.cache[lru.key]
        --this.length
    }
    
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */