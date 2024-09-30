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
    """
    Revisited on 9/29/2024
    https://neetcode.io/problems/time-based-key-value-store
    """
    def __init__(self):
        import heapq
        """
        dictionary?
        {
            key1: [[value, timestamp1], [value, timestamp2], etc],
            key2: [...]
        }
        """
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        # heapq.heappush(self.table[key], [timestamp, value])
        self.table[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """
        since the calls to set have timestamps in strictly increasing order,
        we can assume the array is already sorted by timestamps ascending.
        this allows us to use binary search to find the timestamp
        """

        def binarySearch(left, right, target, values):
            mid = left + (right-left)//2
            timestamp, value = values[mid]    
            if timestamp == target:
                return value
            """
            if the timestamp is not found and we've exhausted our search, 
            we should be at the next closest timestamp that is either 
            greater or less than what we're looking for.
            The condition is that
            prev timestamp <= timestamp, however, since our recursion "overshoots" by one value,
            that would gives us the next greatest value, so the value that's one "less" is mid - 1.
            However, in the case mid - 1 is out of bounds, we return "".
            If we run into a case where the 
            timestamp we're looking for is greater than all of our existing timestamps,
            then we just return mid, as the midpoint would give us the timestamp which meets the condition
            of prev timestamp < target timestamp, so we wouldn't have overshot in this case.
            for example
            2,3,5
            If target timestamp is 4, we would return the value at timestamp 3, since 4 > 3
            If the timestamp was 6, we would return 5
            If the timestamp was 1 however, we can't return 2, since that would mean
            our currentTimestamp would be greater than the target timestamp
            """
            if left >= right:
                if timestamp > target and mid - 1 >= 0:
                    closestTimestamp, closestValue = values[mid-1]
                    return closestValue
                elif timestamp < target:
                    closestTimestamp, closestValue = values[mid]
                    return closestValue
                return ""

            if timestamp > target:
                return binarySearch(left, mid, target, values)
            else:
                return binarySearch(mid+1,right, target, values)
        if (key in self.table):
            left = 0
            right = len(self.table[key])-1
            return binarySearch(left, right, timestamp, self.table[key])
        return ""

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