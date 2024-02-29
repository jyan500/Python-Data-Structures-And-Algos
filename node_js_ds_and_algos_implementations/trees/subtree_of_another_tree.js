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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function(root, subRoot) {
    const isSameTree = (p, q) => {
        if ((!p && q) || (p && !q)){
            return false
        }
        else if (!p && !q){
            return true
        }
        else if (p && q){
            return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
        }
    }
    if (!root){
        return false
    }
    // at each node, check if this is the same as the subroot
    let sub = isSameTree(root, subRoot)
    if (sub){
        return true
    }
    // if not, we continue down the left and right subtrees, checking at each
    // node whether it's the same as the subroot
    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
};