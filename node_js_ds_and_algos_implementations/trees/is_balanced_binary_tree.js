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
var isBalanced = function(root) {
    /* balanced Binary Tree = the difference in height between subtrees 
    cannot be greater than 1 
    starting from the bottom of the tree, we calculate the height of each subtree
    we check if the height difference is ever greater than 1, otherwise we set
    a global flag to false
    at each recursive call, we return the height of that subtree, so that when backtracking
    to previous recursive calls, we always have the proper height
    */
    let flag = true
    const maxHeight = (root) => {
        if (!root){
            return 0
        }
        let leftHeight = maxHeight(root.left)
        let rightHeight = maxHeight(root.right)
        if (Math.abs(rightHeight - leftHeight) > 1 && flag){
            flag = false
        }
        return 1 + Math.max(leftHeight, rightHeight)
    }
    maxHeight(root)
    return flag
};