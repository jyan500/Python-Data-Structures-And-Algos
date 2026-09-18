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
 * @param {number} startValue
 * @param {number} destValue
 * @return {string}
 */
var getDirections = function(root, startValue, destValue) {
    /* 
    BFS to find the shortest path
    you would need to traverse the tree and build an adjacency list for an undirected graph
    and then start BFS from there

    The adjacency list needs to include the relationship (whether its parent, left, or right)
    and also from the child back to its parent since its undirected

    O(N) Time
    O(N) Space
    */
    const adjacency = {}
    const buildList = (root) => {
        if (!root){
            return
        }
        // save left
        if (root.left){
            if (root.val in adjacency){
                adjacency[root.val].push([root.left.val, "L"])
            }
            else {
                adjacency[root.val] = [[root.left.val, "L"]]
            }
            if (root.left.val in adjacency){
                adjacency[root.left.val].push([root.val, "U"])
            }
            else {
                adjacency[root.left.val] = [[root.val, "U"]]
            }
            buildList(root.left)
        }
        if (root.right){
            // save right
            if (root.val in adjacency){
                adjacency[root.val].push([root.right.val, "R"])
            }
            else {
                adjacency[root.val] = [[root.right.val, "R"]]
            }
            if (root.right.val in adjacency){
                adjacency[root.right.val].push([root.val, "U"])
            }
            else {
                adjacency[root.right.val] = [[root.val, "U"]]
            }
            buildList(root.right)
        }
    }
    buildList(root)

    q = []
    // [currentNode, currentPath]
    q.push([startValue, ""])
    visited = new Set()
    while (q){
        let [cur, path] = q.shift()
        if (visited.has(cur)){
            continue
        }
        visited.add(cur)
        if (cur === destValue){
            return path
        }
        for (let [node, direction] of adjacency[cur]){
            q.push([node, path + direction])
        }
    }
    return ""
};