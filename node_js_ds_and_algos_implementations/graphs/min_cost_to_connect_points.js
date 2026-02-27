class Solution {
    /**
     * @param {number[][]} points
     * @return {number}
     */
    minCostConnectPoints(points) {
        /*
        Revisited 2/27/2026

        This solution is not as efficient space-wise as the one below it,
        since this uses actual coords as keys in the adjacency list, basically creating an O(N^2) structure
        that stores each point and its weight to every other point in the list.

        points = [[0,0], [2,2], [3,3], [2,4], [4,2]]
        connect all the points such that
        1) there's only one path between each pair of points
        2) you get the minimum cost 

        is this a graph problem?
        Minimum spanning tree, connect all the points
        with the minimum cost, same definition as above

        I don't remember this off the top of my head, but Prim's or Kruskal's algorithm 
        solves for the minimum spanning tree

        in this case, the weight of an edge is the manhattan distance between the two points

        we need to create an adjacency list where one point is connected with all other points
        with the manhattan distance as a weight

        Why do we check visited set twice in Prim's Algorithm (critical difference between djikstra's):

        In Prim’s algorithm, the Min-Priority Queue can contain multiple entries for the same node. 
        
        let [coord, cost] = heap.dequeue()
        if (visited.has(coord)){
            continue
        }
        For example, if node B is connected to node A with weight 10 and node C with weight 5, 
        both [10, B] and [5, B] might end up in the heap.
        The heap pops [5, B] first. You mark B as visited.
        Later, the heap pops [10, B].
        Without this check, you would add the cost of the "worse" edge (10) to your total, 
        even though node B is already part of your Minimum Spanning Tree (MST). 
        This would create a cycle and give you the wrong answer.

        If node nei is already in the visit set, 
        it means it’s already part of your MST. 
        There is no reason to add an edge leading to it back into the heap, because you know for a fact you'll just end up skipping it anyway when it pops (due to the first check we discussed).
        By checking here, you keep the heap smaller, which saves memory and makes the pop() operations faster 
        (since heap operations are O(Log(Heap Size))

        The total time complexity is N^2 LogN
        */

        function manhattanDistance(x1, y1, x2, y2){
            return Math.abs(x1-x2) + Math.abs(y1-y2)
        }
        let adjacency = {}
        /* key: 'x1,y1' value: [['x2,y2', manhattan distance]]*/
        for (let i = 0; i < points.length; ++i){
            let [x1,y1] = points[i]
            let coord1 = `${x1},${y1}`
            adjacency[coord1] = []
            for (let j = 0; j < points.length; ++j){
                if (i === j){
                    continue
                }
                let [x2,y2] = points[j]
                let coord2 = `${x2},${y2}`
                let dist = manhattanDistance(x1,y1,x2,y2)
                adjacency[coord1].push([
                    coord2,
                    dist
                ])
            }
        }
        /* priority should be based on the manhattan distance */
        let heap = new MinPriorityQueue((entry)=>entry[1])
        let visited = new Set()
        // arbitrary point, just select the first one
        heap.enqueue([`${points[0][0]},${points[0][1]}`,0])
        let N = points.length
        let res = 0
        /* very similar to djikstra's, but once
        we've visited all points, we stop
         */
        while (visited.size < N){
            let [coord, cost] = heap.dequeue()
            if (visited.has(coord)){
                continue
            }
            // whenever we pop off min heap, this will automatically be the min cost
            res += cost
            visited.add(coord)
            for (let [neighCoord, neighCost] of adjacency[coord]){
                if (!visited.has(neighCoord)){
                    heap.enqueue([neighCoord, neighCost])
                }
            }
        }
        return res
    }
}

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