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
     * @returns {number}
     */
    /*
    Approach:
    1) In the intervals list, separate it into two separate lists, one for start times only
    and another for end times only, and sort both of these lists in ascending order.
    2) The idea is that we keep track of two pointers, one that tracks the start times of meetings,
    and the other tracks the end times.

        while (there are meetings that can start)
            if the current meeting has started
                increment num meetings
                increment start pointer
            else 
                decrement num meetings
                increment end pointer
            cur max amt of meetings = max(num meetings, cur max amt of meetings)
    
    Time Complexity:
    O(NLogN), sorting required

    Space:
    O(N)

    Example:
    [(0,40),(5,10),(15,20)]
    
    start times = [0, 5, 15]
    end times = [10, 20, 40]
    start, end = 0
    num meetings = 0
    max num of meetings = 0

    1st iteration
    0 < 10 True
    this means that one meeting has started (0 - 40 meeting)
    num meetings = 1
    max num of meetings = 1
    start = 1
    end = 0

    2nd iteration
    5 < 10 True
    this means that another meeting has started (5 - 10 meeting)
    num meetings = 2
    max num of meetings = 2
    start = 2
    end = 0

    3rd iteration
    15 < 10 False
    this means that one meeting has ended (the 5 - 10 meeting ended)
    num meetings = 1
    max num of meetings = 2
    start = 2
    end = 1

    4th iteration
    15 < 20 True
    this means another meeting has started (15 - 20 meeting)
    num meetings = 2
    max num of meetings = 2
    start = 3
    end = 1

    start === length of start times, this means that there 
    are no more meetings to start, so we can break the loop

    return max num of meetings, which is 2 



    */
    minMeetingRooms(intervals) {
        let startTimes = intervals.map((interval) => interval.start)
        let endTimes = intervals.map((interval)=> interval.end)

        startTimes.sort((a, b) => {
            if (a > b){
                return 1
            }
            else if (a < b){
                return -1
            }
            return 0
        })
        endTimes.sort((a, b) => {
            if (a > b){
                return 1
            }
            else if (a < b){
                return -1
            }
            return 0
        })
        let roomsNeeded = 0
        let numMeetings = 0
        let startPointer = 0
        let endPointer = 0
        while (startPointer < startTimes.length){
            if (startTimes[startPointer] < endTimes[endPointer]){
                ++numMeetings 
                ++startPointer
            }
            else {
                --numMeetings
                ++endPointer
            }
            roomsNeeded = Math.max(roomsNeeded, numMeetings)
        }
        return roomsNeeded

    }
}
