/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        /* 
        Revisited 8/5/2026
        figure out how long the linked list is
        perform deletion on nth

        edge case:
        if the target node we need to delete is the head,
        you'd need a dummy node to handle this case,
        to reference the previous node
        */
        let temp1 = head
        let length = 0
        while (temp1){
            ++length
            temp1 = temp1.next
        }
        let dummy = new ListNode()
        let prev = dummy
        let temp2 = head
        let i = 0
        // from the end of the linked list, length - n
        let toRemoveIndex = length - n
        while (temp2){
            if (i === toRemoveIndex){
                prev.next = temp2.next
                break
            }
            else {
                prev.next = temp2
                prev = prev.next
                temp2 = temp2.next
            }
            ++i

        }
        return dummy.next
    }
}

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    /*
    figure out the length of the list
    loop through the list again, this time when the next
    node is equal to length - n (0 indexed), 
    set the node next to next next

    edge case:
    if the node we want to remove is index 0 (the first one),
    just return head.next, as this will become the remainder of the list
    after the head
    */
    let temp = head
    let i = 0
    while (temp != null){
        ++i
        temp = temp.next
    }
    let target = i - n 
    if (target === 0){
        return head.next
    }
    let newHead = head
    let prev = head
    let j = 0

    while (newHead != null){
        if (j === target){
            prev.next = newHead.next
            newHead = newHead.next
        }
        else {
            prev = newHead
            newHead = newHead.next
        }
        ++j
    }
    return head
};