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
 * @return {number}
 */
var maxPathSum = function(root) {
    /*
    https://www.youtube.com/watch?v=Hr5cWUld4vU&ab_channel=NeetCode
    In a path sum, if a node has both a left and right, we need to make a choice 
    on whether to take the max amount from the left or right, because a path cannot 
    contain both left and right. We also want to see if the value is greater than 0, because
    we don't want to include any negative numbers that would otherwise bring our cumulative sum down.
    We would then return this value in the recursive call.
    
    However, we also keep a global variable that contains the max between our cumulative sum,
    and the sum of the left, right, and current node's values, because this is the max path sum
    assuming this node is the "top" of our path, and we are allowed to include both the left and right values. At each recursive call,
    we want to see whether a new max cumulative sum, so we check max(cumulativeSum, left max, right max)
    
    Time Complexity: O(N)
    
    */
    let maxCumulativeSum = [root.val]
    var search = function(root){
        if (root){
            let leftMax = search(root.left)
            let rightMax = search(root.right)

            /* calculate the max between the left and right subtrees when a split occurs
               we add leftMax and rightMax here because this would be the path sum from 
               left to root to right
                   ROOT
               LEFT    RIGHT
               
               we also need to include 0 to make sure that our cumulative sum does not decrease by preventing the
               inclusion of negative numbers. If there's a negative number, adding 0 implies that we don't include this
               side as a part of our path
            */
            leftMax = Math.max(leftMax, 0)
            rightMax = Math.max(rightMax, 0)
            maxCumulativeSum[0] = Math.max(maxCumulativeSum[0], leftMax + rightMax + root.val)
            return root.val + Math.max(leftMax, rightMax)
        }
        // if there's no node, this would be a sum of 0
        return 0
    }
    search(root)
    return maxCumulativeSum
};