/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    /* 
    fast and slow pointer approach
    1 -> 2 -> 3 -> 4 -> 5

    initially, both fast and slow are at 1
    slow = slow.next (slow is now 2)
    fast = fast.next.next (fast is now at 3)

    next iteration
    slow = slow.next (slow is now at 3)
    fast = fast.next.next (fast is now at 5)

    because fast.next is null, we can't continue the loop
    so slow is at 3, which is the correct middle element

    O(N) time O(1) space 
    */
    let slow = head
    let fast = head
    while (fast && fast.next){
        slow = slow.next
        fast = fast.next.next
    }
    return slow
};