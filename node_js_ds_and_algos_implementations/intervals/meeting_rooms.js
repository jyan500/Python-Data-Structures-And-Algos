/*
https://neetcode.io/problems/meeting-schedule
Similar to logic for the other interval problems, except the intervals
are defined within a class.

Revisited 2/25/2026

*/
/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {boolean}
     */
    canAttendMeetings(intervals) {
        intervals.sort((a, b) => {
            if (a.start > b.start){
                return 1
            }
            else if (a.start < b.start){
                return -1
            }
            return 0
        })
        let nonOverlapping = intervals[0]
        for (let i = 1; i < intervals.length; ++i){
            let {start: prevStart, end: prevEnd} = nonOverlapping
            let {start: curStart, end: curEnd} = intervals[i]
            if (prevEnd > curStart){
                return false
            }
            nonOverlapping = intervals[i]
        }
        return true
    }
}
