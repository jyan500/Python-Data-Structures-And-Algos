class Solution:
    """
    Approach:
    Sliding Window (with left and right pointers)
    1) Similar to max consecutive ones II, we have to track the indices when we find a zero, in this case, storing into a queue
    2) if our queue reaches the max capacity of zeroes that can be flipped, move the left pointer to the index of the "first" zero
    that was found within the queue (q.popleft()), plus one, since we move it one past that index since that also accounts as
    a flipped zero.
    3) Also track the current value of max consecutive ones that we've found

    O(N) time
    O(K) space, where K is the max amount of zeroes we can flip
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        l = 0
        r = 0
        # store the current count of consecutive 1's
        cur = 0
        maxCur = 0
        while r < len(nums):
            if nums[r] == 0:
                # if we reached capacity for zeroes
                if (len(q) == k):
                    if (k > 0):
                        # pop out the left most index which is the 1st zero that was seen
                        firstZeroIndex = q.popleft()
                        # get the distance between the left pointer and the index of the first zero
                        # plus one, since we also include the zero itself that was changed to a 1, which contributes
                        # to the cur value
                        cur -= (firstZeroIndex - l + 1)
                        # since the previous 1's before the first zero that was found no longer count towards the total cur,
                        # we have to decrease the value of cur and set the left pointer to be the "next" value
                        # after the first zero was found
                        l = firstZeroIndex + 1
                        continue
                    else:
                        # if k == 0, we can't flip any zeroes to ones, so whenever
                        # a zero is found, we have to reset cur = 0
                        cur = 0
                else:
                    # save index where the zero was found
                    q.append(r)
                    # this zero has now been "flipped" to a one, increase cur
                    cur += 1
            else:
                # if it's a 1, increase cur
                cur += 1
            maxCur = max(maxCur, cur)
            r += 1
                    
        return maxCur