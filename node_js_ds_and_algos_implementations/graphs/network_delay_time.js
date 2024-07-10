/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    /*
    BFS using min heap (Dijkstra's Algorithm)
    The only difference is the check for visited nodes,
    we allow ourselves to add multiple neighbors that we've already added,
    so that we will dequeue those neighbors, but we won't process the time taken if
    we've already visited it. Therefore, we add the following condition outside of the loop
    that normally retrieves all neighbors to the node.

    if (visited.has(dst)){ 
        continue 
    }
    visited.add(dst)

    Time Complexity:
     O(ELogV), where E is the number of edges and V is the number of vertices
    E = V^2, this is true because an a given graph, there could be bidirectional
    edges between each vertex. In Djikstra's Algorithm, we use a min heap to store
    all possible vertices. Therefore, it's possible we could have the same vertex on the min heap multiple times. So when we pop out of the min heap, it'll be 
    at worst LogV^2, and we repeat this operation for the amount of edges,
    E*LogV^2,
    
    This can be simplified to
    2*E*LogV, and since 2 becomes constant, this further simplifies to
    ELogV, O(ELogV)
    
    */
    let adjacency = {}
    for (let i = 1; i <= n; ++i){
        adjacency[i] = []
    }
    for (let i = 0; i < times.length; ++i){
        let [source, target, time] = times[i]
        adjacency[source].push([target, time])
    }
    let queue = new MinPriorityQueue({priority: (points) => points[1]})
    let res = 0
    let visited = new Set()
    queue.enqueue([k, 0])
    while (!queue.isEmpty()){
        let [dst, time] = queue.dequeue().element
        if (visited.has(dst)){
            continue
        }
        visited.add(dst)
        res = time
        for (let [neighbor, neighborTime] of adjacency[dst]){
            if (!(visited.has(neighbor))){
                queue.enqueue([neighbor, time + neighborTime])
            }
        }
    }
    return visited.size === n ? res : -1
    
};