class Solution {
    /**
     * @param {number[][]} tasks
     * @return {number[]}
     */
    getOrder(tasks) {
        /* 
        sort the tasks by enqueue time
        min heap of processing time
        as we loop through enqueue time,
        pop them from the tasks list using shift so it pops out the front, and push into the min heap for processing time

        note that instead of popping from the tasks list,
        you can actually just increment a pointer to avoid
        having to mutate the original array

        Time Complexity: O(NLogN)
        Space: O(N)
        */

        // include index since we need to return the order
        let toSort = tasks.map((x, i) => [x[0],x[1],i])
        toSort.sort((a,b) => {
            if (a[0] < b[0]){
                return -1
            }
            else if (a[0] > b[0]){
                return 1
            }
            return 0
        })

        let minHeap = new MinPriorityQueue((x) => x[1])

        // set i to the first enqueued task to start
        let currentTime = toSort[0][0]
        let res = []
        let k = 0
        while (k < toSort.length || minHeap.size() > 0){
            while (k < toSort.length && toSort[k][0] <= currentTime){
                minHeap.enqueue(toSort[k])
                k++
            }
            // process shortest processing time
            if (minHeap.size() > 0){
                const [_, processingTime, index] = minHeap.dequeue()
                // add the processing time to the current time
                // so that in the next iteration, we can pop out 
                // any tasks where enqueueTime < current time
                currentTime += processingTime
                res.push(index)
            }
            // note that if the heap is empty but there are still tasks,
            // jump the current time to the next task
            else {
                currentTime = toSort[k][0]
            }
        }
        return res
    }
}
