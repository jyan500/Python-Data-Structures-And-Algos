/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    /*
    1) need to sort the intervals by start time
    2) keep track of the top of the merged intervals list (prev),
    and check whether the prev end time >= current interval start time, if so this is overlapping.
    Take the prev start time and max between the prev and current interval end time
    */
    intervals.sort((a, b) => {
        if (a[0] > b[0]){
            return 1
        }
        else if (a[0] < b[0]){
            return -1
        }
        return 0
    })
    let res = [intervals[0]]
    for (let i = 1; i < intervals.length; ++i){
        let [prevStart, prevEnd] = res[res.length-1]
        let [curStart, curEnd] = intervals[i]
        if (prevEnd >= curStart){
            res[res.length-1] = [prevStart, Math.max(prevEnd, curEnd)]
        }
        else {
            res.push(intervals[i])
        }
    }
    return res
};