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
     * @return {boolean}
     */
    isValidBST(root) {
        /* 
            need a global max and global min parameter that initially
            starts at Number.POSITIVE_INFINITY and Number.NEGATIVE_INFINITY
            
            Check whether the current node is less than the current min and greater than the current max

            if going left,
            set the global max to the current node, since every child node
            must be less than this value

            if going right,
            set the global min to the current node, since every child node
            on the right must be greater than this value

            Base Case:
            If the current node is null,
            an empty tree is considered a valid binary search tree, so return true

            Time: O(N)
            Space: O(N) ( recursion stack )
        */
        const search = (root, curMax, curMin) => {
            if (!root){
                return true
            }
            return root.val < curMax && root.val > curMin && search(root.left, root.val, curMin) && search(root.right, curMax, root.val)
        }
        return search(root, Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY)

    }
}
