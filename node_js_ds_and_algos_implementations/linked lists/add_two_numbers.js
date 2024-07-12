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
/*
Approach without using extra memory:
similar to add two strings where you pad the shorter number with zeroes
to avoid edge cases
With this problem, you can start iterating from the front of the linked list since
the digits are stored in reverse, so it's the same order when performing elementary addition normally.

Time: O(N)
Space: O(1)
*/
var addTwoNumbers = function(l1, l2) {

    let dummy = new ListNode(0)
    let curr = dummy
    let carryover = 0
    let temp1 = l1
    let temp2 = l2
    let len1 = 0
    let len2 = 0
    while (temp1.next){
        ++len1
        temp1 = temp1.next
    }
    while (temp2.next){
        ++len2
        temp2 = temp2.next
    }
    /* since the loops above only go to the second to last element,
    we can add 1 to both lengths for correctness sake, but it's not really necessary
    since we only care about the difference in length and not the exact lengths of both LL's
    */
    ++len1
    ++len2
    
    if (len1 !== len2){
        /* insert zeroes to account for the difference in length
        note that because the digits are in reverse, we'd want to pad
        the zeroes at the end of the linked list (i.e 999 + 10, would be [9, 9, 9], and [0, 1] in LL form)
        to avoid edgecases, we'd want [9, 9, 9] and [0, 1, 0], with the zero padded at the end
        we'd get [9, 0, 0, 1] once performing the addition
        */
        if (len1 > len2){
            let numZeroes = len1 - len2
            // insert new LL nodes with value 0 at the end of the shorter LL
            for (let i = 0; i < numZeroes; ++i){
                temp2.next = new ListNode(0)
                temp2 = temp2.next
            }
        }
        else {
            let numZeroes = len2 - len1
            for (let i = 0; i < numZeroes; ++i){
                temp1.next = new ListNode(0)
                temp1 = temp1.next
            }
        }
    }
    
    /*
    because the digits are already stored in reverse order,
    we can start iterating and performing adding/carryover operations.
    We don't need to worry about the numbers not having the same amount of digits
    and dealing with edgecases there since we did the padding operation above.
    
    similar to elementary addition, add the two digits at the current spot + carryover,
    if sum >= 10, set carryover to 1 and then put the sum - 10 as the value of the LL node
    else, set carryover back to 0 and put the sum as the value of the LL node
    */
    while (l1 && l2){
        let sum = carryover + l1.val + l2.val
        if (sum >= 10){
            carryover = 1
            curr.next = new ListNode(sum - 10)
        }
        else {
            carryover = 0
            curr.next = new ListNode(sum)
        }
        curr = curr.next
        l1 = l1.next
        l2 = l2.next
    }
    // if there's still carryover, add one last LL node with the carryover value
    if (carryover === 1){
        curr.next = new ListNode(carryover)
    }
    return dummy.next
};

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