/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
/*
Approach:
1) Use a min heap since you want the smallest distances to be at the front of the heap
for javascript, you want to specify that you want to take in an object,
and that the priority should be based on a certain attribute of the object (in this case distance)
2) Calculate the distance of each point to (0, 0) using Math.sqrt(x1**2 + y1**2)
3) Enqueue an object into the min priority queue using { distance, point }
4) Pop k times and save to array to get the k closest points to the origin based on the smallest distance
*/
var kClosest = function(points, k) {
    let minHeap = new MinPriorityQueue({priority: (points) => points.distance})
    for (let [x1, y1] of points){
        let distance = Math.sqrt(Math.abs(x1**2 + y1**2))
        minHeap.enqueue({distance: distance, point: [x1,y1]})
    }
    let res = []
    for (let i = 0; i < k; ++i){
        let {point} = minHeap.dequeue().element      
        res.push(point)
    }
    return res
    
};