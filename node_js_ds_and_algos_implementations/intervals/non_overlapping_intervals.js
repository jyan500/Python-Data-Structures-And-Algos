/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    /*
    1) sort the intervals by start time
    2) loop through intervals, keeping track of the last non overlapping interval
    3) Whenever the previous interval's end > current interval's start, this is overlapping. 
        - Trick: greedy approach
            in order to determine which interval to keep and which one to remove, we remove
            the interval that has the greater end time and keep the one that has the smaller end time. 
            This is to prevent this interval from
            potentially overlapping with future intervals.
        increment our count
    */
    intervals.sort((a,b) => {
        if (a[0] > b[0]){
            return 1
        }
        else if (a[0] < b[0]){
            return -1
        }
        return 0
    })
    let lastNonOverlapping = intervals[0]
    let res = 0
    for (let i = 1; i < intervals.length; ++i){
        let [prevStart, prevEnd] = lastNonOverlapping
        let [curStart, curEnd] = intervals[i]
        if (prevEnd > curStart){
            ++res
            lastNonOverlapping = curEnd < prevEnd ? intervals[i] : lastNonOverlapping
        }
        // if the last interval did not overlap, then we set the current interval to be the 
        // new "non-overlapping" interval
        else {
            lastNonOverlapping = intervals[i]
        }
    }
    return res
};