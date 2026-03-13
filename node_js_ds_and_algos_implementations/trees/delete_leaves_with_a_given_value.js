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
     * @param {number} target
     * @return {TreeNode}
     */
    removeLeafNodes(root, target) {
        /*
           1
          2
         2  
        
        if root.left == null && root.right == null,
        it is a leaf node

        if leaf node value === target
            parent.left = null if this leaf
            is the parent's left child,
            or 
            parent.right - null if this is the
            right parent's child
        */
        function search(node, parent, isLeft){
            if (node){
                search(node.left, node, true)
                search(node.right, node, false)
                if (node.left == null && node.right == null){
                    if (node.val == target){
                        if (isLeft){
                            if (parent){
                                parent.left = null
                            }        
                        }
                        else {
                            if (parent){
                                parent.right = null
                            }
                                 
                        }
                    }
                }
            }
        }
        search(root, null, false)
        // last edge case, if the root no longer has
        // any children and val === target, this
        // is the last node to delete
        if (!root.left && !root.right && root.val === target){
            return null
        }
        return root
    }
}
