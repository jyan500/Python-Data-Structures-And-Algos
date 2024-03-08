/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    cur1 = list1
    cur2 = list2
    // create dummy node to avoid edge cases where one of the linked lists is empty
    dummy = new ListNode()
    head = dummy
    while (cur1 && cur2){
    	// take the node with the lesser value first and increment that list's pointer
        if (cur1.val < cur2.val){
            head.next = new ListNode(cur1.val)
            cur1 = cur1.next
            head = head.next
        }
        else if (cur1.val > cur2.val){
            head.next = new ListNode(cur2.val)
            cur2 = cur2.next
            head = head.next
        }
        // if both sides are the same, take values from both lists and increment both pointers
        else {
            head.next = new ListNode(cur1.val)
            cur1 = cur1.next
            head = head.next
            head.next = new ListNode(cur2.val)
            cur2 = cur2.next
            head = head.next
        }
    }
    // because the lists can have different lengths, check to see which list is non null,
    // and set the next pointer to be the remainder of the non-null list
    if (cur1){
        head.next = cur1
    }
    else if (cur2){
        head.next = cur2
    }
    // dummy.next will refer to the beginning of the new linked list (since the dummy is just null)
    return dummy.next
};