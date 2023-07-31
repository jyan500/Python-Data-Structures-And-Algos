'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]

https://leetcode.com/problems/insert-interval/

explanation:
## insert the intervals from the intervals list where the starting value of the current interval is less than the newInterval's starting value
## check to see if the new interval is overlapping with any of the intervals we've added to the output so far, if not then append it
## check to see if the remaining intervals in intervals list are overlapping, if so merge, else append

youtube.com/watch?v=eeTToT5JUUY&list=PLJjp1UcO5B7d7Fm3e45xO74UBf0QiN-wn&index=18&t=339s&ab_channel=TimothyHChang
'''
"""
Revisited again on 7/31/2023,
slightly cleaner solution than the original 
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find out where the interval should be inserted
        i = 0
        while (i < len(intervals) and intervals[i][0] < newInterval[0]):
            i += 1
        # insert the interval and then perform merge intervals on all intervals before this one
        toInsert = intervals[:i]
        toInsert.append(newInterval)
        previousIntervals = [toInsert[0]]
        for j in range(1, len(toInsert)):
            prevStart, prevEnd = previousIntervals[-1]
            curStart, curEnd = toInsert[j]
            if prevEnd >= curStart:
                previousIntervals[-1][1] = max(prevEnd, curEnd)
            else:
                previousIntervals.append(toInsert[j])
        # perform merge interval on the remaining intervals
        restOfIntervals = previousIntervals + intervals[i: ]
        result = [previousIntervals[0]]
        for k in range(1, len(restOfIntervals)):
            prevStart, prevEnd = result[-1]
            curStart, curEnd = restOfIntervals[k]
            if prevEnd >= curStart:
                result[-1][1] = max(prevEnd, curEnd)
            else:
                result.append(restOfIntervals[k])
        return result
"""
Revisited on 7/23/2023
Slightly less efficient but still accepted ONLogN solution
"""
class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        O(NLogN) time complexity, which requires inserting the new interval and then sorting 
        then performing the merge intervals algorithm on the remaining intervals
        """
        # insert the interval and then sort
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: [x[0], x[1]])
        # do merge intervals on the remainder of the intervals
        previousIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            prevStart, prevEnd = previousIntervals[-1]
            start, end = intervals[i]
            if prevEnd >= start:
                mergedStart = prevStart if prevStart < start else start
                mergedEnd = prevEnd if prevEnd > end else end
                previousIntervals[-1] = [mergedStart, mergedEnd]
            else:
                previousIntervals.append(intervals[i])
        return previousIntervals

    """
    O(3N) solution
    1) Get all intervals into the output where the intervals start is less than the new interval's start
    2) Attempt to insert the new interval, fixing any overlaps by updating the end to whichever interval's end is greater
    3) Merge any remaining overlapping intervals
    """
    def insert2(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
    	output = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            newIntervalStart = newInterval[0]
            if start < newIntervalStart:
                output.append(intervals[i])
        merged = False
        for i in range(len(output)):
            prevStart, prevEnd = output[i]
            newStart, newEnd = newInterval
            if prevEnd >= newStart:
                # update only the end
                output[i][1] = max(prevEnd, newEnd)
                # update merged to show that we've merged
                # and fixed an overlap
                merged = True
        # if there were no overlaps, just append the new interval
        if not merged:
            output.append(newInterval)
        
        # merge the remaining intervals to see if any intervals that had 
        # a start time > then the new interval overlaps
        startingIndex = len(output) - 1
        previousInterval = output[startingIndex]
        for i in range(startingIndex, len(intervals)):
            prevStart, prevEnd = previousInterval
            curStart, curEnd = intervals[i]
            if prevEnd >= curStart:
                previousInterval[1] = max(prevEnd, curEnd)
            else:
                previousInterval = intervals[i]
                output.append(intervals[i])
        return output


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ## insert the intervals from the intervals list before reaching new interval
        output = []
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        while (i < len(intervals) and intervals[i][0] < newInterval[0]):
            output.append(intervals[i])
            i += 1
        ## check to see if the new interval is overlapping and insert/merge
        next_start = newInterval[0]
        next_end = newInterval[1]
        has_merged = False
        for j in range(len(output)):
            current_start = output[j][0]
            current_end = output[j][1]
            if (current_end >= next_start):
                output[j][1] = max(current_end, next_end)
                has_merged = True
        if (not has_merged):
            output.append(newInterval)
        ## add/merge the rest of the intervals list that wasn't already added
        i = len(output) - 1
        current_interval = output[i]
        for k in range(i, len(intervals)):
            current_start = current_interval[0]
            current_end = current_interval[1]
            next_start = intervals[k][0]
            next_end = intervals[k][1]
            if (current_end >= next_start):
                current_interval[1] = max(current_end, next_end)       
            else:
                current_interval = intervals[k]
                output.append(intervals[k])
               
        return output
            
            
        
            