/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    // https://www.youtube.com/watch?v=1UOPsfP85V4&t=548s&ab_channel=NeetCode
    // get the kth node in the linked list
    var getKth = function(cur, k){
        while (cur && k > 0){
            cur = cur.next
            --k
        }
        return cur
    }
    
    let dummy = new ListNode(0)
    dummy.next = head
    let groupPrev = dummy
    while (true){
        let kth = getKth(groupPrev, k)
        // if the kth node doesn't exist, that means the group isn't
        // large enough to reverse, so we can break
        if (!kth){
            break
        }
        // reverse group
        /*
        if you use kth.next instead of groupNext in the conditional
        for the while loop below, it breaks, so you have to save the value of kth.next before reversing. 
        I think what's happening is that 
        kth.next value is being updated within the loop (you can see that if you print kth.next in the while loop below), 
        so you need to save its initial value
	    */
        let groupNext = kth.next
        let prev = kth.next
        // groupPrev.next is the first node of this group since
        // gropPrev starts at the dummy node
        let curr = groupPrev.next
        while (curr != groupNext){
            let temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        }
        /*
        This is tricky:
        'reset' the dummy node's next to be the new head of the list
        which is the newly reversed group, since after the group is reversed
        kth is at the beginning of the list instead of at the end of the group.
        
        For example:
        1 -> 2 -> 3 -> 4 -> 5
        looking at the first k group, below:
        dummy -> 1 -> 2 -> 3 
        where groupPrev.next points to 1
        groupPrev points to dummy
        after reversing it's now
        2 -> 1 -> 3 
        however, we now want groupPrev to point to 1
        and we want groupPrev.next to point to 2, since
        groupPrev.next will retain the connection between the dummy and the head of the list. And then groupPrev being set to 1 allows us to continue the rest of our loop starting at the proper node to continue onto the next group.
        
        tmp = groupPrev.next saves the initial value before we change it, which is 1
        groupPrev.next = kth sets groupPrev.next to be 2
        and then groupPrev = tmp will set groupPrev to be 1, so in the following iteration, we start at 1 and then call the kthNode helper to get to 4, etc
        dummy -> 2 -> 1 -> 3
                 ^       ^
                 A       B           
        A) groupPrev.next was set here to retain the connection between dummy and the first node of the group
        B) group prev starts here so we can continue our iteration
        */
        let tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    }
    return dummy.next

};