/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    /*
    Iterative In Order Solution
    1) using a stack, continue going left as much as you can, while pushing onto the stack
    2) Once you can no longer go to the left, pop off the stack, and then using the node
    you just popped off, go to the right
    3) If the right has more nodes, we can continue pushing onto our stack. Otherwise, we will pop again
    https://www.youtube.com/watch?v=5LUXSvjmGCw&ab_channel=NeetCode
   Note that neetcode's video has an error in the while loop conditional,
   it should've been while ( cur || stack ) {...} rather than while (cur && stack), otherwise
   the loop wouldn't have entered because the stack starts out empty 
    */
    let cur = root
    let stack = []
    let n = 0
    while (cur || stack){
        while (cur){
            stack.push(cur)
            cur = cur.left
        }
        cur = stack.pop()
        ++n
        if (n === k){
            return cur.val
        }
        cur = cur.right
    }
};