class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Revisited 9/26/2024
        https://neetcode.io/problems/sliding-window-maximum
        optimized solution uses a queue where each element is in decreasing order 
        (so smallest element is at the end)
        instead of storing the element, store the index of that element instead
        to make it easier to tell when that element is no longer in the window
        """
        from collections import deque
        q = deque()
        res = []
        l = 0
        r = 0
        while (r < len(nums)):
            """
            when adding a new element onto the window, if the last element in the queue (right side)
            is less than the current, pop the last element 
            """
            while (len(q) > 0 and nums[q[-1]] < nums[r]):
                q.pop()
            q.append(r)
            """
            if the left pointer is greater than the index that represents our current max,
            pop the current max
            """
            if q[0] < l:
                q.popleft()
            
            """
            if we've reached the window size, take the current max and append to our res
            to represent the current max of this window, increment left pointer
            """
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Brute Force:
        Iterate through nums via windows of K, and then find the max at each window
        O(N*(N-K+1)), where N - K is the amount of windows you can make
        
        Optimized:
        https://www.youtube.com/watch?v=DfljaUwZsOk&ab_channel=NeetCode
        O(N) Time
        O(N) Space
        Using Deque
        all items in the queue should be strictly decreasing, that way 
        we can always retrieve the max element on the window, which is the leftmost element
        
        1) Create queue and store the indices (as opposed to the elements of the array themselves),
        as it's easier to check whether the leftmost element is out of bounds with the window
        2) keep two pointers i, j and start them at 0. 
        3) while looping through nums, we need to continually check the queue and pop out any elements that are less
        than the current number at index j that we're trying to add. This is because the leftmost element on the queue
        must be the max.
        4) After that, add the current number to the queue.
        5) Check to see if the left most element is still in bounds of this window, otherwise pop left
        6) If we're still within our window, we then add the left most element to the output, which is the max
        of this particular window, and we also increment i.
        7) Increment j
        
        Example:
        nums = [
        3, -1, -2, 0, 4, -5, 8
        ]
        k = 3
        
        1st iteration
        q = []
        i = 0 
        j = 0
        
        j = 0, nums[0] = 3, so we add j to the queue first
        
        q = [0]
    
        2nd iteration
        q = [0]
        i = 0
        j = 1
        
        j = 1, nums[1] = -1
        
        note that -1 is smaller than 3, so we don't need to pop
        we're still in our window, so we don't need to popleft either
        
        3rd iteration
        q = [0, 1]
        i = 0
        j = 2
        
        j = 2, nums[2] = -2
        
        note that -2 is smaller than -1, so we don't need to pop
        we're still in our window, so we don't need to popleft either
        
        We do however hit this condition: j + 1 >= k,
        so we need to increment i and append the left most element to output:
        
        q[0] = 0, output.append(nums[0]) = output.append(3)
        
        output = [3]
        
        4th iteration
        q = [0, 1, 2]
        i = 1
        j = 3
        output = [3]
        
        nums[3] = 0
        
        Now the top of the queue, q[-1] = 2, which is nums[2] = -2
        
        0 > -2, so this goes into the inner while loop...
        
        we need to pop the index 2 off the stack
        q = [0, 1]
        
        now the top of the stack, q[-1] = 1, which is nums[1] = -1
        
        0 > -1, so we need to pop the index 1 off the stack
        q = [0]
        
        now the top of the stack is q[-1] = 0, which is nums[0] = 3
        
        0 < 3, so we don't need to pop off the stack anymore
        
        We now append index 3, 
        q = [0, 3]
        
        Note that i = 1, which is greater than q[0],
        so nums[0] = 3, is no longer in the window...
        
        q.popleft()
        q = [3]
        
        j + 1 >= k, 3 + 1 >= 3, so we need to append nums[q[0]] 
        to the output, which evaluates to 0, and then increment i 
        
        output = [3, 0]
        
        5th iteration:
        i = 2
        j = 4
        output = [3, 0]
        q = [3]
        
        now the top of the stack q[-1] is 3,
        nums[3] = 0, 
        
        0 < nums[4], 0 < 4,
        this gets into the inner while loop...
        
        q.pop(), so q is now empty, q = [] 
        
        append j = 4 to the queue
        q = [4]
        
        i = 2 < q[0] = 4, so no need to popleft()
        
        j + 1 >= k, 4 + 1 >= 3, so we need to append
        nums[q[0]] to the output, and append i 
        
        output = [3, 0, 4]
        
        6th iteration:
        i = 3
        j = 5
        output = [3, 0, 4]
        q = [4]
        
        nums[j] < nums[q[-1]], -5 < 4
        
        no need to go into the inner while loop and pop,
        q = [4, 5]
        
        3 < 4, so no need to popleft()
        
        append nums[q[0]] to the output again, this is still our max.
        increment i 
        
        output = [3, 0, 4, 4]
        
        7th iteration:
        i = 4
        j = 6
        output = [3, 0, 4, 4,]
        q = [4, 5]
        
        nums[j] > nums[q[-1]], 8 > -5
        
        we need to enter in the inner while loop and pop the queue
        q.pop()
        
        q = [4]
        
        nums[j] > nums[q[-1]], 8 > nums[4], 8 > 4,
        
        so we need to pop again
        
        q = []
        
        Append j to the queue
        q = [6]
        
        4 < 6, so no need to popleft
        
        append nums[q[0]], nums[6] = 8, to the output
        
        output = [3, 0, 4, 4, 8]
        
        We can no longer iterate since 
        j is now 7, which is equal to the length of nums
        
        ************ final result is [3, 0, 4, 4, 8] *************
        """
        from collections import deque
        q = deque() # contains indices, because we can index into the array to find the actual value in O(1)
        output = []
        i = 0
        j = 0 
        while (j < len(nums)):
            # Before adding a new number onto the queue, we need to make sure it's strictly decreasing
            # by removing any numbers on the queue that are less than the number we're trying to add
            while (q and nums[q[-1]] < nums[j]):
                q.pop()
            # add the index
            q.append(j)
            # if the left most element on the queue is out of the window, meaning i is now greater than
            # the index in our left most spot on the queue, we also need to pop this out
            if i > q[0]:
                q.popleft()
            # if we've exceeded the window size (since we start i and j at 0, once j + 1 >= k, which indicates the first window has exceeded,
            # we can now start incrementing both i and j). We also need to append the left most element of our queue, as this indicates
            # the "max" of that window
            if j + 1 >= k:
                output.append(nums[q[0]])
                i += 1
            j += 1
        return output
