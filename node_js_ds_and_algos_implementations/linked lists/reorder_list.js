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