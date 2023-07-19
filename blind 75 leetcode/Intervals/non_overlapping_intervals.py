"""
https://leetcode.com/problems/non-overlapping-intervals/submissions/
https://www.youtube.com/watch?v=nONCGxWoUfM&ab_channel=NeetCode`

Solved on 7/18/2023

Key Steps:
1) sort the intervals by start and end times
2) Iterate through the list of sorted intervals, while keeping track of the last
non overlapping interval. 

In order for two intervals to be non-overlapping, the previous end must always
be less than or equal to the current interval's start. 
Therefore, we check prevEnd < start to check for an overlap.

Whenever we find an overlapping interval, we increment
the count to show it's been removed. However if two intervals don't overlap, 
update the non overlapping interval since the last interval has ended, we want
to check for future overlaps using this new interval now.

3) when faced with two intervals that are overlapping, we choose to remove
the interval that ends later in order to potentially avoid an overlap with a future interval.

Meaning prevEnd > end

If the previous interval's end is greater than the current intervals end,
we remove the previous interval, incrementing the count to 1, and then the last non overlapping
interval becomes the current.

O(NLogN) time because of the sort, O(N) space to hold the sorted intervals

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:   
        sortedIntervals = sorted(intervals, key = lambda x: [x[0], x[1]])
        lastNonOverlapping = sortedIntervals[0]
        count = 0
        for i in range(1, len(sortedIntervals)):
            start, end = sortedIntervals[i]
            prevStart, prevEnd = lastNonOverlapping
            # if the previous end is greater than the current start,
            # this is overlapping
            if prevEnd > start:
                # we want to remove the interval that ends later in order to potentially
                # avoid an overlap with a future interval, this will help us keep
                # the number of removals to a minimum
                if prevEnd > end:
                    lastNonOverlapping = sortedIntervals[i]   
                count += 1
            else:
                lastNonOverlapping = sortedIntervals[i]
        return count
                
                