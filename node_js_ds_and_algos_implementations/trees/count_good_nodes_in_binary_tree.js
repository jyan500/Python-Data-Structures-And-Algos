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
var goodNodes = function(root) {
    if (!root){
        return []
    }
    let nodes = []
	// keep track of the current max as a function param 
	// while we traverse the tree.
    var search = function(root, curMax){
        if (root){
        	// if the current root's val is >= to the current max,
        	// this is a "good" node, so we append to our list,
            if (root.val >= curMax){
                nodes.push(root.val)
	        	// update the current max by passing in our current node val
                search(root.left, root.val)
                search(root.right, root.val)
            }
            else {
            	// if we didn't find a greater value, just pass in the current max
                search(root.left, curMax)
                search(root.right, curMax)
            }

        }
    }
    search(root, root.val)
    // take only the length of the list
    return nodes.length
};