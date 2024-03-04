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
 * @return {boolean}
 */
var isValidBST = function(root) {
    /*
    keep track of a current min and current max
    node must be less than the current max
    node must be greater than the current min
    */
    var search = function(root, currentMin, currentMax){
        if (!root){
            return true
        }
        test = root.val > currentMin && root.val < currentMax && 
            search(root.left, currentMin, root.val) && 
            search(root.right, root.val, currentMax)
        return test
        
    }
    
    return search(root, -(2**32), (2**32))
};