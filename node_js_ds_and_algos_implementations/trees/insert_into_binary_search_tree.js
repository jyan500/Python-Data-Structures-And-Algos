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
     * @param {number} val
     * @return {TreeNode}
     */
    insertIntoBST(root, val) {
        /*
        use binary search to figure out the insertion point

        */
        function insert(root, val){
            if (root){
                if (val > root.val){
                    if (root.right){
                        insert(root.right, val)
                    }
                    else {
                        root.right = new TreeNode(val)
                    }

                }
                else {
                    if (root.left){
                        insert(root.left, val)
                    }
                    else {
                        root.left = new TreeNode(val)
                    }

                }
            }
        }
        if (!root){
            return new TreeNode(val)
        }
        insert(root, val)
        return root
    }
}
