/**
 * @param {number[][]} intervals
 * @param {number[]} queries
 * @return {number[]}
 */
var minInterval = function(intervals, queries) {
    /* 
    Labeling this problem as a heap problem rather than an interval problem 
    since it's different from the other interval problems.

    Revisit this problem at:
    https://www.youtube.com/watch?v=5hQ5WWW5awQ&ab_channel=NeetCode
    */
    let sortKey = (a, b) => {
        if (a[0] > b[0]){
            return 1
        }
        else if (a[0] < b[0]){
            return -1
        }
        return 0 
    }
    intervals.sort(sortKey)
    let sortedQueries = [...queries]
    sortedQueries.sort((a,b)=>{
        if (a > b){
            return 1
        }
        else if (a < b){
            return -1
        }
        return 0
    })
    let minHeap = new MinPriorityQueue({priority: (obj) => obj.intervalLength})
    // we use the hashmap so that we can map the query to the valid answer,
    // so that we can get the proper order based on the order of the original query
    // array before sorting
    let res = {}
    let i = 0
    for (let q of sortedQueries){
        // keep adding intervals until the left side of the interval is no longer <= query
        // or there's no more intervals
        while (i < intervals.length &&
               intervals[i][0] <= q){
            let [l, r] = intervals[i]
            minHeap.enqueue({intervalLength: r-l+1, tieBreaker: r})
            ++i
        }
        // pop all the invalid intervals that are too far to the left where the query does not exist in the range
        while (!minHeap.isEmpty() && minHeap.front().element.tieBreaker < q){
            minHeap.dequeue()
        }
        // get the smallest interval that contains q,
        // if no interval contains q, store a -1
        res[q] = !minHeap.isEmpty() ? minHeap.front().element.intervalLength : -1
    }
    // because we need the original order of the queries, we need to re-iterate
    // over the original queries array 
    return queries.map((q) => res[q])
};