/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    /*
    Neetcode: https://youtu.be/S5bfdUTrKLM?si=JNt0SkDP9tlrL00K      
    1) find the middle of the linked list
    2) reverse the second half
    3) merge both sides together
    */
    
    var reverseList = function(head) {
        let prev = null
        let temp = head
        while (temp != null){
            cur = temp
            temp = temp.next
            cur.next = prev
            prev = cur
        }
        return prev
    }

    let slow = head
    let fast = head.next
    while (fast != null && fast.next != null){
        slow = slow.next
        fast = fast.next.next
    }
    let secondHalf = slow.next
    slow.next = null
    
    secondHalf = reverseList(secondHalf)
    
    let temp1 = head
    let temp2 = secondHalf
    while (temp1 != null && temp2 != null){
        let temp1Next = temp1.next
        let temp2Next = temp2.next
        
        temp1.next = temp2
        // this takes temp2.next and places it between temp1 and temp1.next
        temp2.next = temp1Next

        temp1 = temp1Next
        temp2 = temp2Next
        
    }
};

/* 
Slightly different solution that involves creating new nodes during the merging phase 
If done this way, the algorithm is essentially insertion between every other node:
assuming "temp" is the left half
and "prev" is the reversed right half
while (temp && temp.next && prev)
1) saving the old next node
2) creating the new next node
3) setting the new next node's next value to be the old next node
4) set temp.next to be the new next
5) prev = prev.next
6) temp = temp.next.next

7) If there are any remaining prev nodes, 
set temp.next = prev

The reason why it's temp.next.next is because once we insert the node we want, we have
the proper "configuration" for three nodes, so we need to get to the last node (the old "next")
i.e 
1 -> 2
4 -> 3

1 -> 4 -> 2 (this is correct), so we want to start at 2 now instead of 4 (which is temp.next.next)

*/
var reorderList = function(head) {
    /*
    split list in half
    reverse the second half
    interchange the first and reversed second half
    */
    let slow = head
    let fast = head.next
    while (fast && fast.next){
        slow = slow.next
        fast = fast.next.next
    }
    // slow should now be at the middle
    let rightHalf = slow.next
    // cut list in half
    slow.next = null
    
    // reverse the right half
    let prev = null
    while (rightHalf){
        let curr = rightHalf
        rightHalf = rightHalf.next
        curr.next = prev
        prev = curr
    }
    let temp = head
    while (temp && temp.next && prev){
        let oldNext = temp.next
        let newNext = new ListNode(prev.val)
        newNext.next = oldNext
        temp.next = newNext
        prev = prev.next
        temp = temp.next.next
    }
    temp.next = prev
};