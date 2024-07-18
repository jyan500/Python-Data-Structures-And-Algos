/*
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
*/
var ListNode = function(k=null, v=null, next=null){
    this.keyPair = {key: k, value: v}
    this.next = next
}

var MyHashMap = function() {
    this.map = []
    for (let i = 0; i < 10**4; ++i){
        // these will be the heads of new linked lists
        this.map.push(new ListNode())
    }
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    let index = key % this.map.length
    let cur = this.map[index]
    // note that cur is the head of this linked list
    while (cur.next){
        let {key: k, value: v} = cur.next.keyPair
        if (k === key){
            cur.next.keyPair = {key: k, value: value}
            return
        }
        cur = cur.next
    }
    cur.next = new ListNode(key, value, null)
};

/** 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    let index = key % this.map.length
    let cur = this.map[index]
    // very similar to trieNode question
    while (cur.next){
        let {key: k, value: v} = cur.next.keyPair
        if (k === key){
            return v
        }
        cur = cur.next
    }
    return -1
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    let index = key % this.map.length
    let cur = this.map[index]
    // very similar to trieNode question
    while (cur.next){
        let {key: k, value: v} = cur.next.keyPair
        if (k === key){
            // removing the list node by setting the next to be next.next, so it skips over
            // the next node
            cur.next = cur.next.next
        }
        else {
            cur = cur.next
        }
    }
};

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */