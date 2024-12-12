""" 
https://www.lintcode.com/problem/642/
"""
class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        from collections import deque
        self.q = deque()
        self.curSum = 0
        self.limit = size

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self.q) == self.limit and len(self.q) > 0:
            v = self.q.popleft()
            self.curSum -= v
        self.q.append(val)
        self.curSum += val
        return self.curSum if len(self.q) == 1 else self.curSum/len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)