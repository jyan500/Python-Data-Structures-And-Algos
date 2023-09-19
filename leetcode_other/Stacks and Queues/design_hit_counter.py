"""
Leetcode Premium
https://www.lintcode.com/problem/3662/

O(N) Time O(N) Space

Key Concept:
1) Use a Queue to store the timestamps
2) In get_hits, we continually pop off the front of the queue if the timestamp is more than 5 minutes ago (300 seconds),
this translates to top of queue <= timestamp - 300. If the timestamp is less than 300, it doesn't enter the while loop, which means
it's still within the 5 minute threshold
"""
class HitCounter:

    def __init__(self):
        from collections import deque
        self.q = deque()

    """
    @param timestamp: the timestamp
    @return: nothing
    """
    def hit(self, timestamp: int):
        self.q.append(timestamp)

    """
    @param timestamp: the timestamp
    @return: the count of hits in recent 300 seconds
    """
    def get_hits(self, timestamp: int) -> int:
        while (self.q and self.q[0] <= timestamp - 300):
            self.q.popleft()
        return len(self.q)