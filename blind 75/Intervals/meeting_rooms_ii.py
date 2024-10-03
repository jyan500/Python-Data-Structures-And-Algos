"""
https://www.lintcode.com/problem/919/
https://www.youtube.com/watch?v=FdzJmTCVyJU&ab_channel=NeetCode
1) get all start times and end times for all meetings,
keep track of number of meetings that are currently happening
based on when they start
2) Keep track of two pointers that will track when current meeting
starts and previous meeting ends
3) during iteration, we check whether the start pointer is less than the end pointer's value,

if the start pointer value is less, that means a meeting has started, so we increment
the amount of meetings happening, and also figure out if we've reached our max number of rooms needed so far. 

If the end pointer value is greater, that means a meeting has ended, so we decrement the amount of meetings currently 
happening.

4) Once our start times has reached the end, that means we've figured out all the meetings that 
started, so any remaining meetings will just be ending, so no need to change the meeting count anymore
since the number will just be decrementing at that point, it will never exceed the max we've
already found.

Time complexity: O(NLogN), sorting
Space Complexity: O(N) to hold the start and end times separately

"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        Revisited 10/3/2024
        https://neetcode.io/problems/meeting-schedule-ii
        separate out the starting and ending times into two separate lists
        and sort them
        Use two pointers
        track num rooms
        0 5 15
        10 20 40
        at 0, one meeting starts
        0     5          15
                 10          20         40
        this is less than 10, which is the first ending of a meeting
        at 5, another meeting starts, this is still less than 10
        (at this point, we have 2 rooms needed)
        at time 15, this is greater than the end time, so we keep the start pointer
        the same and increment end pointer. We also decrement the amount of rooms needed by one
        next iteration, compares 15 and 20, 15 is the start of one meeting, so we increment the
        start pointer and count of rooms by one.

        At this point, there are no more meetings that are started, so the remaining rooms
        are ending, which will decrement the count of rooms back to 0.

        At it's maximum value, the amount of rooms needed was 2
        """
        startTimes = [interval.start for interval in intervals]
        endTimes = [interval.end for interval in intervals]
        startTimes.sort()
        endTimes.sort()
        startTimePtr = 0
        endTimePtr = 0
        maxCount = 0
        count = 0
        while (startTimePtr < len(startTimes) and endTimePtr < len(endTimes)):
            startTime = startTimes[startTimePtr]
            endTime = endTimes[endTimePtr]
            if startTime >= endTime:
                count -= 1
                endTimePtr += 1
            else:
                count += 1
                startTimePtr += 1
            maxCount = max(count, maxCount)
        return maxCount

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:

        startTimes = sorted([interval.start for interval in intervals])
        endTimes = sorted([interval.end for interval in intervals])
        amountOfRoomsNeeded = 0
        numMeetings = 0
        startPointer = 0 
        endPointer = 0
        while startPointer < len(startTimes):
            # taking the min here determines whether a meeting started
            # or a meeting just ended
            if startTimes[startPointer] < endTimes[endPointer]:
                numMeetings += 1
                # after incrementing the number of meetings, see if this has exceeded
                # the max we've found so far
                amountOfRoomsNeeded = max(numMeetings, amountOfRoomsNeeded)
                startPointer += 1
            else:
                numMeetings -= 1
                endPointer += 1
        
        return amountOfRoomsNeeded