/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
// https://leetcode.com/problems/insert-interval/
var insert = function(intervals, newInterval) {
    /*
    insert interval
    * Note the intervals are already in sorted order
    2) figure out where the interval should go based on its start time
    3) insert the interval into this spot
    4) figure out if any intervals after it need to be merged, and then merge them
    */
    if (intervals.length === 0){
        intervals.push(newInterval)
        return intervals
    }
    let k = 0
    // if the current start is less than the new interval's start, keep increasing k
    // until this is no longer true. Once k reaches this point, this is where we should insert the new interval
    while (k < intervals.length && intervals[k][0] < newInterval[0]){ 
        ++k 
    }
    intervals.splice(k, 0, newInterval)
    // perform merge intervals
    let res = [intervals[0]]
    for (let i = 1; i < intervals.length; ++i){
        let [prevStart, prevEnd] = res[res.length-1]
        let [curStart, curEnd] = intervals[i]
        // if the previous endpoint is greater than the current's start, this is overlapping
        if (prevEnd >= curStart){
            // take the min of the two starts
            // take the max of the two ends, combine
            res[res.length-1] = [Math.min(prevStart, curStart), Math.max(prevEnd, curEnd)]

        }
        else {
            res.push(intervals[i])
        }
    }
    return res
};