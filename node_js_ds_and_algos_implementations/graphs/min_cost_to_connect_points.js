/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    /*
    Prim's Algorithm
    https://www.youtube.com/watch?v=f7JOBJIC-NA
    
    Time Complexity:
    O(N^2LogN), LogN comes from popping the min heap, N^2 to create the adjacency relationship, 
    since each point could connect to every other point (and there are N points)

    Space:
    O(N)


    Approach:
    1) Constructing the adjacency list for this problem is different from other graph problems
    
        the format is key mapped to an array of nested arrays, where the nested array
        is [distance to another point from current point, the index of this other point]

        adjacency[index] = [ [distance to another point on the graph, the index of this point], ... ]

        adjacency = {}
        for i ... points.length
            x1, y1 = points[i]
            for j = i + 1 ... points.length
                x2, y2 = points[j]
                manhattan distance = abs(x1-x2) + abs(y1-y2)
                adjacency[i].push([manhattan distance, j])
                adjacency[j].push([manhattan distance, i])

        since this is undirected, you also create the reverse relationship
    
    2) This is essentially a BFS, but using a min heap instead of a queue
        use a visited set
        initially, we start at point 0, 0 and put it onto the min heap

        from there, it's an implementation of BFS, where at each iteration,
        we dequeue from the min heap, and then we deconstruct the element as [distance, i],
        and then add the distance to the element.

        from there, i is used to key into the adjacency list to get the neighbors

    */
    // priority is based on the manhattan distance
    let queue = new MinPriorityQueue({priority: (points) => points[0]})
    let adjacency = {}
    for (let i = 0; i < points.length; ++i){
        adjacency[i] = []
    }
    for (let i = 0; i < points.length; ++i){
        let [x1, y1] = points[i]
        for (let j = i + 1; j < points.length; ++j){
            let [x2, y2] = points[j]
            let dist = Math.abs(x1-x2) + Math.abs(y1-y2)
            // from point i, get the distance to all other points besides itself
            adjacency[i].push([dist, j])
            // since this is undirected, we add the reverse relationship
            adjacency[j].push([dist, i])
        }
    }
    let res = 0
    let visited = new Set()
    queue.enqueue([0,0])
    while (visited.size < points.length){
        let [cost, i] = queue.dequeue().element
        if (visited.has(i)){
            continue
        }
        res += cost
        visited.add(i)
        for (let [neighborCost, neighbor] of adjacency[i]){
            if (!visited.has(neighbor)){
                queue.enqueue([neighborCost, neighbor])
            }
        }
    }
    return res
};