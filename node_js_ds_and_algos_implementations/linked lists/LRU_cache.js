/* 
Revisited 2/20/2026 

Using doubly linked list solution
Note for future reference, you can also use the Map() data structure
in javascript which will maintain the ordering of the keys based on insertion order,
this can be used to simulate the LRU cache here for most recently/least recently used
*/
class ListNode {
    constructor(key=null,val=null){
        this.prev = null
        this.next = null
        this.val = val
        this.key = key
    }
}

class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        /*
        how to keep track of recently used?
        we need an object to track key value pairs, but also need to track
        the order of get/put, which an object in javascript doesn't do natively.

        any time a get/put is done on a key/value pair, it's considered recently used.

        if we track an object with all cache items, and then use a separate data structure to track
        their order.

        Based on the hints, we can use a doubly linked list, where the least recently used node is the Head,
        and the most recently used is the tail. Whenever we get/put a specific key/value pair, remove the corresponding
        node and reinsert at the tail

        the special thing about doubly linked list is that the head is directly connected to the tail with
        just a pointer between them, so it speeds up the process of locating the node
        */
        this.capacity = capacity
        this.curCapacity = 0
        this.cache = {} // map key to node
        // two dummy nodes where the "next" of left and the "prev" of right
        // will be considered the true two ends of the LL
        this.left = new ListNode()
        this.right = new ListNode()
        // connect the two ends of the doubly list node
        this.left.next = this.right
        this.right.prev = this.left
    }

    /* remove from LL */
    remove(node){
        /*
        [] <-> [] <-> []
              node
          ------------>
        []     []     []
    node.prev        node.next
          <------------
        the node.prev.next = node.next
        and node.next.prev becomes node.prev
        this way, node is disconnected from its neighbors and therefore deleted
        */
        let prev = node.prev
        let next = node.next
        prev.next = next
        next.prev = prev
    }

    /* insert into LL on the right side (most recently used)*/
    insert(node){
        /*
        since our right pointer is the dummy, the "true" right side is the 
        this.right.prev, which is where we want to insert.

        this.right.prev    this.right
                [] <->  () <->   []
        where () is the insertion spot

        therefore, we save the old this.right.prev
        set the old prev's next to be node
        then set the current this.right's prev to be node

        then we connect it from the inserted node to its neighbors
        */
        let oldPrev = this.right.prev
        oldPrev.next = node
        this.right.prev = node

        node.next = this.right
        node.prev = oldPrev
    }
    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        let res = -1;
        if (key in this.cache){
            // remove from LL and re-insert to most recently used
            this.remove(this.cache[key])
            this.insert(this.cache[key])
            res = this.cache[key].val
        }
        // update the order
        return res
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        // if key is already in cache, have to move it most recently used
        if (key in this.cache){
            let node = this.cache[key]
            // update the node's value
            node.val = value
            // move it to the most recently used
            this.remove(node)
            this.insert(node)

        }
        // key not in cache
        else {
            // if we have not hit capacity
            if (this.curCapacity < this.capacity){
                this.cache[key] = new ListNode(key,value)
                this.insert(this.cache[key])
                this.curCapacity++
            }
            // otherwise, remove least recently used first
            else {
                let leastRecentlyUsed = this.left.next
                this.remove(leastRecentlyUsed)
                // delete least recently used from cache
                delete this.cache[leastRecentlyUsed.key]
                // insert new node
                this.cache[key] = new ListNode(key, value)
                this.insert(this.cache[key])
            }
        }
    }
}

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