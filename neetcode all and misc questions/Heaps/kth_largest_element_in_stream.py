"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
Time: O(NLogN + MLogK), where M is the amount of calls to "add"
NLogN is the time taken to convert the array to a heap
Space: O(N)

Concept: 

Note that when you print a heap out in python, it's in the "heap" represented order (if you were to create a tree out of it),
but not necessarily in the array's sorted order, in a similar way to an array representation of an inorder binary tree traversal.


1) Use Min Heap
kth largest element in the list example:
k = 3
heap = [1, 2, 3, 5, 6]
Because k is 3, the third largest element in this list is 3

2) Because we only need k, we can pop any elements off that are less than k, so 1 and 2 in this case

heap = [3, 5, 6]

3) When adding new elements, we do heap push, and then immediately pop off the smallest element

heap = [3, 5, 4, 6]

After heappop, the 4 gets bubbled up to the root as it's now the min element

heap = [4, 5, 6]

"""
class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        """
        Revisited on 10/1/2024,
        Time Complexity:
        O(NLogN) heapify + O(MLogN), where M is the amount of calls made to self.add()
        put all items of the stream into the min heap so they are sorted, but then
        pop out until only k items are left.
        The idea is that the kth largest element is always the first element of the min heap, 
        kind of like a "sliding window", where the heap only contains the largest k elements
        """
        for i in range(len(nums)-k):
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """ 
        push val to the heap. If the heap is now greater than k, pop out the first value. 
        Return the first value of the heap. 
        This also works if we add a value that is less than the top of the heap,
        since we'd add it the top, and then immediately remove it
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
import heapq
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # use a min heap, and pop out until only k items are left
        # in the heap
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # if we've exceeded k amount, pop
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # the first item in the list will always be the kth largest 
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)