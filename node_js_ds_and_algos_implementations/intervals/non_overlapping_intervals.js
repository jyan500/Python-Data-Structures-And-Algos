class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    eraseOverlapIntervals(intervals) {
        /*
        Alternate solution 6/30/2026
        Greedy approach simplifies things here
        Instead of sorting by start time (like in most interval problems),
        sort by end time

        The reasoning is because any interval that comes earlier in the list
        is less likely to collide with future intervals, since it's an earlier
        end time. So by default, we would be removing less intervals this way (resulting 
        in the minimum)

        The overlapping check would instead be if prev.end > cur.start since it's sorted
        by end time

        Loop through intervals starting from 1 ... n
            If prevEnd > curStart
                update remove count, but keep prev the same, since
                it's a smaller end time, so we decrease the chances of conflicts
            else
                update prev to be the current interval

        Time: O(NLogN)
        Space: O(1)
        */

        // sort by end time
        intervals.sort((a,b) => {
            if (a[1] < b[1]){
                return -1
            }
            else if (a[1] > b[1]){
                return 1
            }
            return 0
        })
        let res = 0
        let prev = intervals[0]
        for (let i = 1; i < intervals.length; ++i){
            let [prevStart, prevEnd] = prev
            let [curStart, curEnd] = intervals[i]
            // overlapping
            if (prevEnd > curStart){
                res++
            }
            else {
                prev = intervals[i]
            }
        }
        return res
    }
}

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