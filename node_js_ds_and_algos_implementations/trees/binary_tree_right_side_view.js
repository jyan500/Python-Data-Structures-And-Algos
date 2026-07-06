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
     * @return {number[]}
     */
    rightSideView(root) {
        /*
        level order traversal using BFS
        but at each level, only take the very last element into the result 

        More optimal solution that uses less memory per level:
        just save the very last element in a variable, so by default, we overwrite the variable
        within each level and only the very last iteration gets saved, that becomes the right side
        */
        if (!root){
            return []
        }
        let q = []
        q.push(root)
        let res = []
        while (q.length){
            let N = q.length
            let rightSide = null
            for (let i = 0; i < N; ++i){
                let cur = q.shift()
                if (cur.left){
                    q.push(cur.left)
                }
                if (cur.right){
                    q.push(cur.right)
                }
                rightSide = cur.val
            }
            res.push(rightSide)
        }
        return res
    }
}

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
 * @return {number[]}
 */
/*
Same as level order traversal,
but:
right side of the tree is always the last node
of each level within our level order traversal

After traversal is done, pull the last element out of each list
*/
var rightSideView = function(root) {
    if (!root){
        return []
    }
    let q = []
    let levels = []
    q.push(root)
    while (q.length){
        let originalLength = q.length
        let level = []

        for (let i = 0; i < originalLength; ++i){
            let node = q.shift()
            if (node.left){
                q.push(node.left)
            }
            if (node.right){
                q.push(node.right)
            }
            level.push(node.val)
        }
        levels.push(level)
    }
    return levels.map((level) => level[level.length-1])
};