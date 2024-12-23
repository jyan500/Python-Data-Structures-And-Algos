class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/
        (this is close to the 2 heaps solution suggested in the editorial)
        Approach:
        Sliding window + Heap
        Also keep track of the currentMin and currentMax of the sliding window,
        so that we can do absolute value of (currentMax - currentMin) to get the limit value,
        and check whether the value <= limit parameter.
        
        If abs(currentMax - currentMin) > limit, we have to keep moving the left pointer until that condition becomes false
        We also use two heaps to keep track of the min values and max values
        in order to make sure the values are in the window, we also keep track of the indices along with the
        value in a tuple before appending to the heap. 
        After moving the left pointer, it's also important to pop out any values with indices that are outside of
        the window.

        Time: O(NLogN), because we're pushing N elements to the heap, each heappush takes O(LogN) time
        Space: O(N)
        
        nums = [10,1,2,4,7,2]
        limit = 5
        
        minHeap = []
        maxHeap = []
        
        1st iteration
        minHeap = [(10, 0)]
        maxHeap = [(10, 0)]
        
        2nd iteration
        minHeap = [(1,1), (10,0)]
        maxHeap = [(10,0), (1,1)]
        
        abs(max-min) = 10-1= 9, 9 > the limit of 5, enters the while loop
        l += 1 , so l = 1
        any elements in min and max heap with values less than 1 are popped
        
        minHeap = [(1,1)]
        maxHeap = [(1,1)]
        
        3rd iteration
        minHeap = [(1,1),(2,2)]
        maxHeap = [(2,2),(1,1)]
        
        2 - 1 = 1, which is under the limit 5
        
        4th iteration
        minHeap = [(1,1),(2,2),(4,3)]
        maxHeap = [(4,3),(2,2),(1,1)]
        
        4 - 1 = 3, which is under the limit 5
        
        5th iteration
        minHeap = [(1,1),(2,2),(4,3),(7,4)]
        maxHeap = [(7,4),(4,3),(2,2),(1,1)]
        
        7-1 = 6, which is above the limit of 6
        increment left by one, to 2, remove any elements less than 2
        
            minHeap is now [(2,2),(4,3),(7,4)]
            maxHeap is now [(7,4),(4,3),(2,2)]
        
        new calculation in the inner while loop, 7 - 2 = 5, so this is in bounds of the limit now, so the inner while loop ends
        
        6th iteration
        minHeap = [(2,5),(2,2),(4,3),(7,4)]
        maxHeap = [(7,4),(4,3),(2,5),(2,2)]
        
        7 - 2 = 5, so this in bounds
        
        outer while loop breaks out because r > len(nums)
        
        final answer is 5 - 2 + 1 = 4
        """
        import heapq
        l = 0
        r = 0
        N = len(nums)
        minHeap = []
        maxHeap = []

        curMaxLength = 0
        while (l < N and r < N):
            heapq.heappush(maxHeap, (-nums[r], r))
            heapq.heappush(minHeap, (nums[r], r))
            # because the smallest value of limit can be 0, we can safely assume
            # that we continue this loop until the left and right pointers overlap,
            # which would mean the min and max would be the same value, so abs(min-max) == 0,
            # so the loop will end.
            while l < r and abs(-maxHeap[0][0]-minHeap[0][0]) > limit: 
                l += 1
                # remove any elements from the heap that are no longer in the window
                while (maxHeap[0][1] < l):
                    heapq.heappop(maxHeap)
                while (minHeap[0][1] < l):
                    heapq.heappop(minHeap)
            curMaxLength = max(curMaxLength, r - l + 1)    
            r += 1  
        return curMaxLength
            
                