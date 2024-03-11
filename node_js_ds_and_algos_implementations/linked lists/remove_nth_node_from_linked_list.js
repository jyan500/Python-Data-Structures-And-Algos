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