"""
Leetcode Premium
https://www.lintcode.com/problem/920/description
1) Similar to other interval problems, like merge interval
sort by the start time
iterate through the sorted list of intervals, 
if the previous end is greater than the current start, this is overlapping, return False
"""
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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals = sorted(intervals, key = lambda interval: [interval.start, interval.end])
        for i in range(1, len(intervals)):
            prevStart, prevEnd = intervals[i-1]
            curStart, curEnd = intervals[i]
            if prevEnd > curStart:
                return False
        return True