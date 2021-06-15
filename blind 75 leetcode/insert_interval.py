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
            
            
        
            