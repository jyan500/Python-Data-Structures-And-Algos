/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */

var lowestCommonAncestor = function(root, p, q) {
    /*
        for BST, we know that the left side is always
        smaller than root, and the right side is always bigger than root
        Using reverse thinking, we know that if both p and q are both
        smaller than our root, we haven't reached the LCA yet, since we can still go
        to the left
        If both p and q are both to the right of root, we also haven't reached LCA yet.
        since we can still go to the right
        If neither of these conditions are true, that means we're actually at the LCA
        at this point, because p and q would both be descendents on the left and right
        subtrees respectively
        
    */
    if (p.val < root.val && q.val < root.val){
        return lowestCommonAncestor(root.left, p, q)
    }
    else if (p.val > root.val && q.val > root.val){
        return lowestCommonAncestor(root.right, p, q)
    }
    else {
        return root
    }
};