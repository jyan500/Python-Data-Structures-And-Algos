/* 
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
*/
var ListNode = function(value){
    this.value = value
    this.next = null
}
var MyHashSet = function() {
    this.set = []
    for (let i = 0; i < 10**4; ++i){
        this.set.push(new ListNode(null))
    }
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
    let index = key % this.set.length
    let cur = this.set[index]
    while (cur.next){
        let { value } = cur.next
        if (cur.next.value === key){
            return
        }
        cur = cur.next
    }
    cur.next = new ListNode(key)
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
    let index = key % this.set.length
    let cur = this.set[index]
    while (cur.next){
        let {value} = cur.next
        if (cur.next.value === key){
            cur.next = cur.next.next
        }
        else{
            cur = cur.next
        }
    }
};

/** 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
    let index = key % this.set.length
    let cur = this.set[index]
    while (cur.next){
        let {value} = cur.next
        if (cur.next.value === key){
            return true
        }
        cur = cur.next
    }
    return false
};

/** 
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */