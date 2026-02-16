class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
	/*
	https://neetcode.io/problems/valid-tree

    Revisited 2/16/2026 with the same solution

	Approach:
	1) A graph is a valid tree if:
		- from the root (0), all other nodes are reachable
		- no cycles
	Using DFS and keeping a global visited set, check to see if there are any cycles. Because
	the graph is undirected, we have to track the "prev" node to make sure we don't
	accidentally revisit the node that we came from

	If DFS passes, AND the amount of nodes === the length of our global visited set, this is a valid tree

	*/
    validTree(n, edges) {
        // build adjacency
        let adjacency = {}
        for (let i = 0; i < n; ++i){
            adjacency[i] = []
        }
        for (let pair of edges){
            let [node, edge] = pair
            adjacency[node].push(edge)
            adjacency[edge].push(node)
        }
        var globalVisited = new Set()
        var dfs = function(node, prev){
            if (globalVisited.has(node)){
                return false
            }
            globalVisited.add(node)
            for (let edge of adjacency[node]){
                if (edge !== prev){
                    if (!dfs(edge, node)){
                        return false
                    }
                }
            }
            return true
        }
        return dfs(0, -1) && globalVisited.size === n
    }
}
