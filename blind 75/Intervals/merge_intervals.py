'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

https://leetcode.com/problems/merge-intervals/
explanation: https://www.youtube.com/watch?v=qKczfGUrFY4&ab_channel=NickWhite

concept: get the first interval and make that the current interval to compare to
iterate through the interval list
if (the current interval's end is greater than or equal to the next interval's start), then its overlapping
if its overlapping, update the end value of the current interval
if its not overlapping with the current interval, add it to the list and update the current interval value 
'''
class Solution:
	# revisited this solution on 7/3/2023
	def altSolution1(self, intervals: [[int]]) -> [[int]]
		if len(intervals) == 1:
            return intervals
        # sort the intervals
        intervals = sorted(intervals, key = lambda x: [x[0], x[1]])
        # keep track of a stack where the top is always the last interval
        # that was merged
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            previousStart, previousEnd = result[-1]
            # at the top of the stack, 
            # if the previous interval's end is greater than or equal to the current interval's start
            # that means it's overlapping
            if previousEnd >= start:
                # when merging the intervals, get the smallest start and the greatest end 
                mergedStart = previousStart if previousStart < start else start
                mergedEnd = previousEnd if previousEnd > end else end
                # update the top of the stack with the merged interval,
                # if the next interval overlaps with this merged interval, this value gets
                # updated again, etc until it no longer overlaps
                result[-1] = [mergedStart, mergedEnd]
            else:
                result.append(intervals[i])
        return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda nums: nums[0])
        output = [intervals[0]]
        current_interval = intervals[0]
        if (len(intervals) == 1):
            return output
        for i in range(1, len(intervals)):
            current_begin = current_interval[0]
            current_end = current_interval[1]
            next_begin = intervals[i][0]
            next_end = intervals[i][1]
            ## if overlapping, update the current interval's ending value to include the
            ## overlapping merge's end value, don't add to the list yet until 
            ## its not overlapping with the next interval value
            if (current_end >= next_begin):
                current_interval[1] = max(current_end, next_end)
            else:
                current_interval = intervals[i]
                output.append(current_interval)
            
        return output
            