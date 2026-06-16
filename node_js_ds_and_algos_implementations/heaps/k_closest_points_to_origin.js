class Solution {
    /**
     * @param {number[][]} points
     * @param {number} k
     * @return {number[][]}
     */
    kClosest(points, k) {
        /*
        min heap problem
        store the coordinates as well as their euclidean distance in an object
        push onto the min heap
        then pop off k times 

        Time: O(NLogN + KLogN) -> kLogN when dequeing k times, NLogN when enqueing each element
        Space: O(N)
        */
        let minHeap = new MinPriorityQueue((x) => x.distance)
        let distances = []
        for (let [x,y] of points){
            // technically, you don't need the sqrt since we're only comparing relative distances, 
            // and don't care what the actual distance value is
            // let dist = Math.sqrt(x**2 + y**2)
            let dist = x**2 + y**2
            minHeap.enqueue({
                distance: dist, x, y
            })
        }
        let res = []
        for (let i = 0; i < k; ++i){
            let {distance,x,y} = minHeap.dequeue()
            res.push([x,y])
        }
        return res
    }
}
