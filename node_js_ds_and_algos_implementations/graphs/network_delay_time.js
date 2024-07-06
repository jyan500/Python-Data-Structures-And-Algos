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