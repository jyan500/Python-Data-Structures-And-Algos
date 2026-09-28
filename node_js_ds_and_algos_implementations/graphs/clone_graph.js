/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        /* 
        Revisited 9/26/2026
        DFS
        hashmap to map the old to new node
        */
        if (!node){
            return node
        }
        const hashmap = {}
        const clone = (node) => {
            let cur;
            // if we've already seen this node,
            // return its copy
            if (node.val in hashmap){
                return hashmap[node.val]
            }
            // map the old to the copy
            else {
                cur = new Node(node.val)
                hashmap[node.val] = cur
            }
            for (let neighbor of node.neighbors){
                // push the result of the DFS, which should
                // be the "copy" node version of the neighbor
                cur.neighbors.push(clone(neighbor))
            }
            return cur
        }

        return clone(node)
    }
}

/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
	// keep a hashmap where it maps the old node to the new copy
    let oldToNew = {}
    var dfs = function(n){
        let node
        // if the value of the node is already found in the map,
        // we want to re-use the new node, otherwise,
        // we create a new node copy with the same value.
        if (n.val in oldToNew){
            return oldToNew[n.val]
        }
        else {
            node = new Node(n.val)
            oldToNew[node.val] = node
        }
        // for each of the old node's neighbors,
        // we want to push each neighbor into the new node's neighbor list
        for (let neighbor of n.neighbors){
            node.neighbors.push(dfs(neighbor))
        }
        // we return the copy of the new node, this way the recursion
        // builds from the bottom up, and by the end, we would've had the root node, with all
        // new nodes attached
        return node
    }
    if (node){
        return dfs(node)
    }
};