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
    minMeetingRooms(intervals) {
        /*

        O(NLogN) time
        O(N) space 

        [(0,40), (5,10), (15,20)]
        sort the intervals by start time, and then by end time
        use a min heap that holds the end time of a meeting
        iterate through the intervals
            [40]
            if the end time on the heap is greater than the current start,
                place the current meeting end time onto the heap
                10 < 40, so places 10 on the min heap
            [10,40]
            20 > 10, so this means that we should pop out the end time
            of 10 from the heap
            however, 20 is still less than 40, so we put 20 on the min heap

        at the end, there are 2 elements left on the min heap,
        so that means 2 rooms were needed in total to schedule all meetings without conflicts

        note that's its important it's:
        if (minHeap.size() > 0 && minHeap.front() <= start){
            minHeap.dequeue()
        }

        and not

        while (minHeap.size() && minHeap.front() <= start){
            minHeap.dequeue()
        }

        Example:
        intervals:  [
            Interval { start: 1, end: 5 },
            Interval { start: 1, end: 20 },
            Interval { start: 2, end: 6 },
            Interval { start: 5, end: 10 },
            Interval { start: 10, end: 15 },
            Interval { start: 15, end: 20 }
        ]

        []
        [ 5 ]
        [ 5, 20 ]
        [ 5, 6, 20 ]
        [ 6, 10, 20 ]
        
        Note at this point in time, we're analyzing {start: 10, end: 15}
        if we were to do the while loop condition, both 6, 10 and would get popped out.
        But in reality, because 6 is already ended, and technically 10 is just ending,
        we still need one room for {start: 10, end: 15}, and the other for {start: 5, end: 10}. 
        The while loop condition states:
        "two rooms freed up, so I'll reuse both"
        but you can only sit in one chair at a time. 
        The new meeting only needs one of those freed rooms. 
        The other freed room still represents a room that was needed historically, 
        and another future meeting could need it.

        [ 10, 15, 20 ]
        */
        intervals.sort((a,b) => {
            if (a.start < b.start){
                return -1
            }
            else if (a.start > b.start){
                return 1
            }
            else {
                if (a.end < b.end){
                    return -1
                }
                else if (a.end > b.end){
                    return 1
                }
                return 0
            }
        })
        let minHeap = new MinPriorityQueue()
        for (let i = 0; i < intervals.length; ++i){
            let { start, end } = intervals[i]
            if (minHeap.size() > 0 && minHeap.front() <= start){
                minHeap.dequeue()
            }
            minHeap.enqueue(end)
        }
        return minHeap.size()
    }
}

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
