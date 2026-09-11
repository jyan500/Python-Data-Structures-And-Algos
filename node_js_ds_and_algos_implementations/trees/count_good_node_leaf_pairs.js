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
 * @param {number} distance
 * @return {number}
 */
var countPairs = function(root, distance) {
    /* 
    https://neetcode.io/solutions/number-of-good-leaf-nodes-pairs
    Time: O(N * D^2), where D is the distance param and N is the number of nodes
    Space: O(N)

    Example run through:
    root = [1,2,3,4,5,6,7] distance = 3
         1
       2    3
     4  5  6  7
    
    assuming we recur all the way down the left first...
    you'd return [1] and [1] for the leaf nodes
    performs the loop with [1], [1], 1 + 1 creates a distance of 2, which is <= 3,
    so this.pairs increments to 1

    this combines to [1,1], and then returns [2,2] since we'd be going back to the root

    you'd also return [1] and [1] for the leaf nodes,
    performs the nested for loop for [1], [1], 1+1 creates a distance of 2, which is <= 3
    so this.pairs increments now to 2
    
    this combines to [1,1], and then returns [2,2] since we'd be going back to the root

    Now doing the loop on [2,2] and [2,2], the distances are now too great, so we know that 
    these aren't good pairs
    */
    this.pairs = 0 
    const dfs = (node) => {
        if (!node){
            return []
        }
        // if we're at a leaf node, the distance between the
        // parent and this node is 1
        if (!node.left && !node.right){
            return [1]
        }

        const leftDist = dfs(node.left)
        const rightDist = dfs(node.right)

        // when we have the distances between each of the left children and their respective parents
        // and same for the right,
        // we do a nested for loop to find each pair of distances, and then add them together
        // to get the total distance between them. If that total distance <= our param's distance,
        // this is considered a "good leaf node pair", so we increment
        for (let d1 of leftDist){
            for (let d2 of rightDist){
                if (d1 + d2 <= distance){
                    ++this.pairs
                }
            }
        }

        // combine the distances between the parent and its nodes on both the left and right subtrees
        const combined = [...leftDist, ...rightDist]
        // return the combined array where each of the distances is incremented by 1
        // to represent that the distance between the next parent and the leaf node has increased by 1
        return combined.map((dist) => dist+1)
    }

    dfs(root)
    return this.pairs
};