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
var diameterOfBinaryTree = function(root) {
	// you can use let as a declaration for a global variable in the recursion
	// this is valid because when using diameter inside the helper, 
	// it's technically in the same scope as the diameterOfBinaryTree function
	// due to closure
    let diameter = 0
    const helper = (root) => {
        // the base case is when there's no root, the height would be 0
        if (!root){
            return 0
        }            
        /* 
        calculate the height of the left and right subtrees,
        and as we do that, we then calculate the diameter
        by taking the max between the current diameter and the sum of the heights of the left and right subtrees
        */
        let heightLeft = helper(root.left)
        let heightRight = helper(root.right)
        diameter = Math.max(diameter, heightLeft + heightRight)
        return 1 + Math.max(heightLeft, heightRight)
    }
    helper(root)
    return diameter
};