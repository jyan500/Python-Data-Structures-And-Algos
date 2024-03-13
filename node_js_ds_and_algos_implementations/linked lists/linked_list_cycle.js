/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    /* 
    two pointer strategy
    fast and slow pointers
    
    if the value of fast === slow, that means there's a cycle,
    because fast went backwards
    */
    slow = head
    fast = head
    while (fast && fast.next){
        slow = slow.next
        fast = fast.next.next
        if (slow === fast){
            return true
        }
    }
    return false
};