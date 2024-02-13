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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (root){
        // in lieu of python's swap syntax:
        /*
        we set a temp variable for root.left's value
        we set a temp2 variable for root.right's value
        
        Set root.right's value now to be the temp variable,
        which was root.left's value
        Set root.left's value now to be the temp2 variable,
        which was root.right's value
        */
        tmp = root.left
        tmp2 = root.right
        root.right = tmp
        root.left = tmp2
        invertTree(root.left)
        invertTree(root.right)
    }
    return root
};