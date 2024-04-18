class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
	/* 
	https://neetcode.io/problems/count-connected-components
	Time Complexity:
	O(V+E), where V is the amount of vertices (nodes) and E is the amount of edges
	Space:
	O(N), where N is the amount of nodes (for the visited set)
	*/
    countComponents(n, edges) {
        /*
        build adjacency for undirected graph 
        */
        let adjacency = {}
        for (let i = 0; i < n; ++i){
            adjacency[i] =  []
        }
        for (let pair of edges){
            let [node, edge] = pair
            adjacency[node].push(edge)
            adjacency[edge].push(node)
        }
        let visited = new Set()
        /* 
        Using a global visited set, keep track of visited nodes. 
        After a run of the DFS has finished, this DFS would have visited all nodes that 
        were reachable from our starting point, so we can increment the count by 1, as this
        means we would've seen at least one connected component.

        In our next run of DFS, we will skip any nodes that we've already visited, and only
        run the DFS on unvisited nodes
        */
        let count = 0
        /*  */
        var dfs = function(node){
            for (let edge of adjacency[node]){
                if (!visited.has(edge)){
                    visited.add(edge)
                    dfs(edge)
                }
            }
        }
        for (let i = 0; i < n; ++i){
            if (!visited.has(i)){
                dfs(i)
                ++count
            }
        }
        return count
    }
}
