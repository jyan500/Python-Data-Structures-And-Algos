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
     * @param {number} left
     * @param {number} right
     * @return {ListNode}
     */
    reverseBetween(head, left, right) {
        /*
        4/21/2026
        O(N) Time
        Uses O(N) memory to hold all the list nodes

        extract the node elements from the index
        reverse them
        splice them back into the original list 
        */ 
        let copy = []
        let i = 1
        let temp = head
        // create new list nodes with the values intact
        while (temp){
            copy.push(new ListNode(temp.val))
            temp = temp.next
        }

        let res = new ListNode(0)
        let dummy = res
        let l = left-1
        let r = right-1
        // reverse the node elements in place between the boundaries
        while (l <= r){
            [copy[l], copy[r]] = [copy[r], copy[l]]
            ++l
            --r
        }
        // re-connect the linked list values with the dummy pointer
        for (let k = 0; k < copy.length; ++k){
            dummy.next = copy[k]
            dummy = dummy.next
        }
        return res.next

    }
}
