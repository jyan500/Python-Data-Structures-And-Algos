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
     * @return {ListNode}
     */
    insertGreatestCommonDivisors(head) {
        /* 
        GCD calculation using the euclidean algorithm
        a b
        a becomes b, and b becomes a % b, repeat this process
        until the mod value is 0, in which the gcd is now the value of a

        Time: O(N * log(min(a,b))), where log(min(a,b)) is the time complexity of the gcd function
        Space: O(N) space for the gcd listnodes
        */
        const gcd = (a,b) => {
            if (b === 0){
                return Math.abs(a)
            }
            return gcd(b, a % b)
        }
        let cur = head
        // having cur.next ensures that there's always at least two nodes in the list,
        // so it handles the edge case of having only one node
        while (cur.next){
            let gcdVal = gcd(cur.val, cur.next.val)
            // save the reference to the old next
            let next = cur.next
            let temp = new ListNode(gcdVal)
            // set the next of the current node to the new list node with our gcd value
            cur.next = temp
            // set the new list node to our old next so it's inserted in between
            temp.next = next
            // move the pointer over our new node onto the old next node
            cur = cur.next.next
        }
        return head
    }
}
