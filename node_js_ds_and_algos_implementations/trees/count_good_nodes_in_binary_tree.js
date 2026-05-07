/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    goodNodes(root) {
        /*
        Revisited 5/7/2026
        storing the current max while we traverse the tree,
        if the node is greater or equal to the current max, that means
        that there is no node in the path that has a value greater than
        the current, so this would be considered a "good" node 

        for example
           1
         1   1

        technically, all 3 nodes here are good nodes, because they are all equal,
        but no value is greater than the other, which explains why its >= and not just >

        Time: O(N)
        Space: O(1)
        */
        if (!root){
            return 0
        }
        let res = 0
        const search = (node, curMax) => {
            if (node){
                let newMax = curMax
                if (node.val >= curMax){
                    res += 1
                    newMax = node.val
                }
                search(node.left, newMax)
                search(node.right, newMax)            
            }
        }
        search(root, root.val)
        return res
    }
}

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