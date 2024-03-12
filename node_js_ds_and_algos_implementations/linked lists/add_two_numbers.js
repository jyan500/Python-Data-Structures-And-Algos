/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    /*
    pull both numbers out into an array
    perform add two numbers algorithm to get the sum
    put the numbers back into a linked list
    */
    let array1 = []
    let array2 = []
    while (l1){
        array1.unshift(l1.val)
        l1 = l1.next
    }
    while (l2){
        array2.unshift(l2.val)
        l2 = l2.next
    }
    let diff = Math.abs(array1.length-array2.length)
    if (diff > 0){
        for (let i = 0; i < diff; ++i){
            array1.length < array2.length ? array1.unshift(0) : array2.unshift(0)
        }
    }
    let res = []
    let carryover = 0
    for (let i = array1.length-1; i >= 0; --i){
        let sum = carryover + array1[i] + array2[i]
        if (sum >= 10){
            carryover = 1
            // note that we want the numbers to be in reverse order, so we 
            // push instead of unshift here
            res.push(sum - 10)
        }
        else {
            carryover = 0
            res.push(sum)
        }
    }
    if (carryover > 0){
        res.push(1)
    }
    let dummy = new ListNode(0)
    let head = dummy
    for (let i = 0; i < res.length; ++i){
        head.next = new ListNode(res[i])
        head = head.next
    }
    return dummy.next
};