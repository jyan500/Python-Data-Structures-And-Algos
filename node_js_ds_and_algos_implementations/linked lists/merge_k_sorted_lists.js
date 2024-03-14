/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
 /*
 Set a prev variable to be the first sorted list that needs to be merged
 as we iterate through lists from 1 ... n,
 merge prev and lists[i], and then in the following iteration...
 prev = merge(prev, lists[1]) 
 prev = merge(prev, lists[2]) ...

 Time Complexity:
 O(length of lists * length of each inner list)

 Space Complexity:
 O(N)
 */
var mergeKLists = function(lists) {
    var mergeTwoLists = function(l1, l2){
        let dummy = new ListNode(0)
        head = dummy
        while (l1 && l2){
            if (l1.val < l2.val){
                head.next = new ListNode(l1.val)
                l1 = l1.next
                head = head.next
            }
            else if (l2.val < l1.val){
                head.next = new ListNode(l2.val)
                l2 = l2.next
                head = head.next
            }
            else {
                head.next = new ListNode(l1.val)
                l1 = l1.next
                head = head.next
                head.next = new ListNode(l2.val)
                l2 = l2.next
                head = head.next
            }
        }
        // if one of the lists is longer than the other,
        // set it to the remaining
        if (l1){
            while (l1){
                head.next = new ListNode(l1.val)
                l1 = l1.next
                head = head.next
            }
        }
        else if (l2){
            while (l2){
                head.next = new ListNode(l2.val)
                l2 = l2.next
                head = head.next
            }
        }
        return dummy.next
    }
    if (lists.length === 0){
        return null
    }
    else if (lists.length === 1){
        return lists[0]
    }
    let prev = lists[0]
    for (let i = 1; i < lists.length; ++i){
        // merge the previous list with the current list,
        // after merging set it to prev
        prev = mergeTwoLists(prev, lists[i])
    }
    return prev
};