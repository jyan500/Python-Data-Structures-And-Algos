class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, newInterval) {
        /*
        Revisited 6/3/2026
        sort the intervals
        first, find the insertion point where the interval should go based on its starting time
        then, perform the merge intervals algorithm in the case the interval is overlapping
        with previous intervals in the list 
        */
        if (!intervals.length){
            return [newInterval]
        }

        intervals.sort((a,b) => {
            if (a[0] < b[0]) {
                return -1
            }
            else if (a[0] > b[0]){
                return 1
            }
            return 0
        })
        let k = 0
        let newIntervals = [...intervals]
        let inserted = false
        while (k < intervals.length){
            // if the new interval is less than the current start,
            // insert the new interval here
            if (newInterval[0] < newIntervals[k][0]){
                newIntervals.splice(k, 0, newInterval)
                inserted = true
                break
            }
            ++k
        }
        // if the new interval was not inserted, that means it should've been inserted in the final
        // spot since it has a start time that's greater than the latest start time in the lsit
        if (!inserted){
            newIntervals.push(newInterval)
        }
        let merged = [newIntervals[0]]
        for (let i = 1; i < newIntervals.length; ++i){
            let [curStart, curEnd] = newIntervals[i]
            let [prevStart, prevEnd] = merged[merged.length-1]
            // if the prevEnd > currentStart, this is overlapping
            if (prevEnd >= curStart){
                // merge
                merged[merged.length-1] = [Math.min(prevStart, curStart), Math.max(prevEnd, curEnd)]
            }
            else {
                merged.push(newIntervals[i])
            }
        }
        return merged
    }
}

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