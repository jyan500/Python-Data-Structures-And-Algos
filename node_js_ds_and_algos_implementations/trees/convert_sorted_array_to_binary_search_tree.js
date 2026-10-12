/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    /* 
    note that an inorder traversal of a binary search tree will result in a sorted array
    generally, the root should be in the middle, and the left subtree and right subtrees
    would be the slice of everything to the left of the root, and everything to the right of it
    */ 
    if (nums.length){
        let mid = Math.floor(nums.length/2)
        let left = sortedArrayToBST(nums.slice(0, mid))
        let right = sortedArrayToBST(nums.slice(mid+1, nums.length))
        return new TreeNode(nums[mid], left=left, right=right)
    }
    return null
};