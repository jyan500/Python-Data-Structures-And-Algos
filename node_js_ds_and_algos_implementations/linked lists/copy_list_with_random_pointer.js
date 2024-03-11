/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
   /*
   2 references:
   array of each list node, so the node can be retrieved through its index
   hashmap: key is the index of the ith node, and the value is the index of the node pointed by the random pointer
   
   7 -> 13 -> 11 -> 10 -> 1 -> null
   
   1) push each of the original list nodes into the array so we have the index
   2) Loop through the list again, but this time, use findIndex to find the node that's being 
   referenced by random pointer
   3) Add the entry to the hashmap, where the key is the current index, and the value is the index
   of the node that's being pointed to by random pointer
   
   for example,
   if 13 points to 7, this would be the equivalent of {1: 0}, because i = 1 node points to i = 0 node
   
   4) At the same time as step 3, construct the copied list using a dummy pointer
   5) Repeat step 1 on the new copied list
   6) Once we have the newNodeList, we loop through newNodeList, and then reference back to our hashmap
   
   if our current node index has a value of -1 in the hashmap, that means it originally pointed to null (as -1 means the index could not be found)
   otherwise, it should point to the index somewhere in newNodeList, so we set random pointer to be newNodeList[randPointerMap[i]], which should
   be the proper location that it was pointing to originally.
   */ 
    let nodeList = []
    let temp = head
    while (temp){
        nodeList.push(temp)
        temp = temp.next
    }
    let temp2 = head
    let randPointerMap = {}
    // at this time, also create the copy of the linked list through the dummy node
    let newNodeList = []
    let dummy = new ListNode(0)
    let newHead = dummy
    for (let i = 0; i < nodeList.length; ++i){
        newNode = new ListNode(nodeList[i].val)
        newHead.next = newNode
        newHead = newHead.next
        let randIndex = nodeList.findIndex(x => x === nodeList[i].random)
        randPointerMap[i] = randIndex
    }

    let temp3 = dummy.next
    // append each node to the new node list so we can retrieve the node by index
    while (temp3){
        newNodeList.push(temp3)
        temp3 = temp3.next
    }
    // loop through the new node list, this time setting the random pointers
    for (let i = 0; i < newNodeList.length; ++i){
        let index = randPointerMap[i]
        if (index === -1){
            newNodeList[i].random = null
        }
        else {
            newNodeList[i].random = newNodeList[index]
        }
    }
    return dummy.next
};