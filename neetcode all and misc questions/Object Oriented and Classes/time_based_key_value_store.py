"""
https://leetcode.com/problems/time-based-key-value-store/
Key concepts:
1) 
Storing key, values, and timestamps in a structure like so, where the key is the key,
and the value is a list of tuples w/ timestamp and value
{key: [(timestamp, value), (timestamp, value)]
2) 
The problem states that we'll always be inserting timestamps in increasing order, 
so the timestamps are added in sorted ascending order.
That means that to find timestamps more efficiently, we can apply binary search
3) 
If the timestamp doesn't exist in our list of timestamps, our binary search should've found
the next biggest value. So we can get the element directly to the left to be our "next smallest" value
For example if we had:

{"foo": [(1, "bar"), (4, "bar2"), (6, "bar3")]}

If input timestamp = 3, we'd expect to receive 1, so the value "bar" as the answer
If input timestamp = 5, we'd expect to reveive 4, so the value "bar2" as the answer

In binary search, if we couldn't find 3, our left and right pointers would be at index 0,
but because we can't go any further back, we just return left 

In binary search, if we couldn't find 5, our left and right pointers would be at index 2,
which is 6, "bar3", therefore the answer is left - 1

"""
class TimeMap:

    def __init__(self):
        # timestamps are always increasing, meaning it'll be in sorted order
        self.timeMap = dict()
        # {key: [(timestamp, value), (timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp, value)]
    
    # use binary search to find the index of the timestamp,
    # or the next smallest timestamp if the exact timestamp 
    # couldn't be found
    def getPrevTimestampIndex(self, keys, timestamp: int):
        left = 0 
        right = len(keys) - 1
        def helper(keys, timestamp, left, right):
            mid = left + (right-left)//2
            ts, val = keys[mid]
            if timestamp == ts:
                return mid
            # if the timestamp couldn't be found and the search has ended,
            # left will give us the timestamp that is closest in value
            # to the timestamp we were trying to find
            # so we just need to subtract one to find the previous value since this is
            # in sorted order, or just return left if we're at the beginning of the list
            if left >= right:
                return left if left == 0 else left - 1
            
            # if the timestamp is greater than the mid
            # we actually search the left side since we always want to find
            # the next smallest value
            if timestamp < ts:
                return helper(keys, timestamp, left, mid)
            # if the timestamp is less than mid, we want to search the right side
            elif timestamp > ts:
                return helper(keys, timestamp, mid+1, right)
        return helper(keys, timestamp, left, right)
    
    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            keys = self.timeMap[key]
            # edge cases:
            smallestTs, valOfSmallest = keys[0]
            largestTs, valOfLargest = keys[-1]
            # if the timestamp is less than the smallest timestamp
            # that we've seen, just return ""
            if timestamp < smallestTs:
                return ""
            # if the timestamp is greater than the biggest timestamp we've seen
            # just return the biggest so far
            if timestamp > largestTs:
                return valOfLargest
            index = self.getPrevTimestampIndex(keys, timestamp) 
            closest = keys[index]
            ts, val = self.timeMap[key][index]
            return val
        return ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)