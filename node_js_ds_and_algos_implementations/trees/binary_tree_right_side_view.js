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