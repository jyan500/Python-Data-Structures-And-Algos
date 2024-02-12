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
 * @return {number}
 */
 // Time Complexity: O(N)
var maxDepth = function(root) {
	// base case: a binary tree with no root is a depth of 0
    if (!root){
        return 0
    }
    // get the depths of the left and right subtrees,
    // and the find the max between the two
    // we add 1 to signify that this particular node adds "1" to our overall depth,
    // so after finding our max depth between the left and right, we add 1 and go back to the previous
    // recursive call
    let left = maxDepth(root.left)
    let right = maxDepth(root.right)
    return 1 + Math.max(left, right)
};