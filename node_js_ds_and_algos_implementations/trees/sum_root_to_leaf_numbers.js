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

/* 
8/16/2026
This solution uses less memory since we're not storing every number built from each path before taking the sum,
instead we build the number in the param, and return the sum of each path as the recursive result 
O(N) Time
O(h) Space
*/
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    sumNumbers(root) {
        // solution without storing the current number as a string
        // alternative is to build from the bottom up, starting from each leaf node
        // we keep the num as a param, but we are returning the current sum in the recursive call
        // of the number paths
        const search = (root, num) => {
            if (!root){
                return 0
            }
            // update accumulated number as we search, multiplying
            // by 10 (i.e if num is 2, and we add digit 3, we do 2 * 10 = 20 + 3 = 23)
            num = (num * 10) + root.val
            // if we reach a leaf node, return accumulated number
            if (!root.left && !root.right){
                return num
            }
            // get the sum between the two different paths
            return search(root.left, num) + search(root.right, num)
        }
        return search(root, 0)
    }
}

/* 
My first solution uses more memory since it stores the numbers of each path, meaning the space used
is the recursive stack + the amount of pathways in the tree
*/
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    sumNumbers(root) {
        let numbers = []
        const search = (root, cur) => {
            if (!root){
                return
            }
            if (!root.left && !root.right){
                // because the problem states the tree depth goes to 10,
                // there can be a max of ten digits in the integer,
                // so we don't need to worry about losing precision
                let last = [...cur, root.val]
                numbers.push(Number(last.join("")))
                return
            }
            search(root.left, [...cur, root.val])
            search(root.right, [...cur, root.val])
        }
        search(root, [])
        return numbers.reduce((acc,num) => acc + num, 0)
    }
}
