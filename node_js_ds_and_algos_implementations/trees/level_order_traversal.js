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
 * @return {number[][]}
 */

/* 
A few quirks with the JS implementation vs the Python Implementation
1) Using an array as a queue (since there's no native queue implementation in JS),
and doing shift(), which pops the leftmost element of the array
2) Make sure to store the original length of the queue before entering the for loop,
and adding items to the queue.
*/
var levelOrder = function(root) {
    if (!root){
        return []
    }
    let q = []
    let levels = []
    q.push(root)
    while (q.length){
        let level = []
        let qLength = q.length
        for (let i = 0; i < qLength; ++i){
            let node = q.shift()
            if (node){          
                if (node.left){
                    q.push(node.left)
                }
                if (node.right){
                    q.push(node.right)
                }
                level.push(node.val)
            }
        }
        levels.push(level)
    }
    return levels
};