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
     * @param {number} key
     * @return {TreeNode}
     */
    deleteNode(root, key) {
        /*
        O(H) Time (height of the tree)
        O(H) Space for the recursive stack

        because this is a binary search tree, the properties of left child
        is smaller than parent, and right child is bigger than parent must remain,
        so if we have to propagate one of the children to the new parent, it needs to maintain
        the BST properties.

        if the node we're trying to delete only has one child, we can just return the non-null
        child in the recursion

        But if the node has two children, we have to take the "min" of the right subtree,
        by iterating on the right subtree's LEFT child until there is no more left child. Then,
        we have to pass in the node and call the "search" recursive function on that node
        */
        const search = (node, key) => {
            if (!node){
                return node
            }
            if (key < node.val){
                node.left = search(node.left, key)
            }
            else if (key > node.val){
                node.right = search(node.right, key)
            }
            // once we've found the node, determine whether the node to delete
            // has two non-null children or only one
            else {
                // if only one side has child, just return the other side to replace the deleted node
                if (!node.left) return node.right
                if (!node.right) return node.left
                // make a temp reference to node.right (so we don't lose track of our current position at node)
                // figure out the min of the right subtree by iterating
                // only on the left side (similar to a linked list)
                let cur = node.right
                while (cur.left){
                    cur = cur.left
                }
                // once we find this, we need to propagate this back to the original parent
                // by "replacing" the value of this min value with the node
                // and then recursively calling the function to delete the node that had the min value
                // by setting the "key" as that min vaule
                node.val = cur.val
                node.right = search(node.right, node.val)
            }
            return node
        }
        root = search(root, key)
        return root
    }
}
