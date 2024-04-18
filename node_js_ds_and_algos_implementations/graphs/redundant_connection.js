/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function(edges) {
    /*
    https://leetcode.com/problems/redundant-connection/solution/
    https://leetcode.com/problems/redundant-connection/discuss/323625/JavaScript-DFS-Solution
    
    given a [node, edge], find another node that goes to the same edge
    
    time complexity: O(N^2), where N is the amount of nodes. The worst case is that
    for every edge, we have to search every previously occuring edge of the graph
    
    space: O(N), for the map() that represents the graph
    */
    var findRedundantConnection = function(edges) {
    let graph = new Map();
    let curr;
    
    for(const [v, e] of edges){
        if(dfs(v, e, new Set())){
            curr = [v, e];
        }
        if(!graph.has(v)) graph.set(v, new Set());
        if(!graph.has(e)) graph.set(e, new Set());
        
        graph.get(v).add(e);
        graph.get(e).add(v);
    }
    
    function dfs(v, e, visited){
        visited.add(v);
        
        if(graph.has(v)){
            let edges = graph.get(v);

            // 
            if(edges.has(e)) return true; // cycle detected
            
            for(const edge of edges){
                if(!visited.has(edge)){
                    // if we find another vertex that points to the original edge we passed in,
                    // this is a cycle
                    if(dfs(edge, e, visited)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
    return curr;
};