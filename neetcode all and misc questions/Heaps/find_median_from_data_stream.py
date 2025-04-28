import heapq
import math

# revisited on 4/28/2025 with the same solution as below (without the comments)
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, num * -1)
        if (len(self.maxHeap) > 0 and len(self.minHeap) > 0):
            topMax = self.maxHeap[0] * -1
            topMin = self.minHeap[0] 
            if topMax > topMin:
                topMax = heapq.heappop(self.maxHeap) * -1
                heapq.heappush(self.minHeap, topMax)
                
        if abs(len(self.minHeap)-len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                top = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -1 * top)
            else:
                top = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, -1 * top)

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            topMax = self.maxHeap[0] * -1
            topMin = self.minHeap[0]
            return (topMax+topMin)/2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0] * -1

class MedianFinder:
    """
    TLE solution:
    Use a heap, adding a number to the heap via heappush is O(Logn),
    but getting n largest and n smallest is ONLogN,
    if we get the last element in largest, and last element in smallest,
    this would get us the median for even numbered heaps, or taking the last element in either smallest/largest for odd numbered heaps, but because it's ONLogN, it doesn't pass.
    """
#     def __init__(self):
#         self.heap = []

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.heap, num)
        

#     def findMedian(self) -> float:
#         n = len(self.heap)
#         largest = heapq.nlargest(math.ceil(n/2), self.heap)
#         smallest = heapq.nsmallest(math.ceil(n/2), self.heap)
#         if n % 2 == 0:
#             return (largest[-1] + smallest[-1])/2
#         else:
#             return smallest[-1]
    """
    Optimized Solution (Neetcode)
    1) Use two heaps, one max heap (A) and one min heap (B)
    the min heap contains all elements that are larger than elements than A
    the max heap contains all elements that are smaller than B

    2) By default, we will always add an element to the max heap (A)
    However, once we have a length difference greater than 1, we need to
    balance the heaps by popping out the max of max heap (A) and then adding 
    it to min heap (B). Vice versa, if there's too many elements in min heap (B), you'd need to pop the min from min heap B and add it to max heap (A)

    There can also be a case where an element exists in A that is greater than elements in B, so you'd need to pop out the element from A

    The benefit of this solution is that popping a min from min heap or max from max heap is O(LogN), and adding to a heap is O(LogN). 

    That way, the findMedian can also be O(LogN) since popping min from min heap, popping max from max heap, and then adding together and dividing by 2 is also O(1) (or if there's a length difference of 1, we can just take the max from the max heap if len(maxHeap) > len(minheap) OR we take the min of min heap if len(minHeap) > len(maxHeap)
    """
    def __init__(self):
        self.maxHeapA = []
        self.minHeapB = []

    def addNum(self, num: int) -> None:
        # in order to to convert a min heap to a max heap in python,
        # we have to convert the numbers to negative when inserting
        heapq.heappush(self.maxHeapA, -1 * num)
        # to access the max without popping, use heap[0],
        # but since the numbers inside max heap are negative,
        # we have to convert back by doing * -1
        topMaxHeapA = -1 * self.maxHeapA[0]
        topMinHeapB = None
        if (len(self.minHeapB) > 0):
            # if the max of A is greater than the min of B,
            # this is incorrect because every element in A must be less than 
            # every element in B, need to pop out
            topMinHeapB = self.minHeapB[0]
            if topMaxHeapA > topMinHeapB:
                topMaxHeapA = -1 * heapq.heappop(self.maxHeapA)
                heapq.heappush(self.minHeapB, topMaxHeapA)
        # if the length difference between the two heaps is greater than one,
        # either because we added too many elements to A OR 
        # because of the operation above when we moved the max of A to B ...
        if (abs(len(self.maxHeapA) - len(self.minHeapB)) > 1):
        	# if len(A) > len(B), that means we need to pop from A and add the
        	# popped element to B
        	# note that we need to convert the popped element by multiplying by -1
            if (len(self.maxHeapA) > len(self.minHeapB)):
                topMaxHeapA = -1 * heapq.heappop(self.maxHeapA)
                heapq.heappush(self.minHeapB, topMaxHeapA)
            # otherwise, we need to pop from B and add to A,
            # noting that since we're adding to A, we need to multiply by -1 first
            else:
                topMinHeapB = heapq.heappop(self.minHeapB)
                heapq.heappush(self.maxHeapA, -1 * topMinHeapB)

    def findMedian(self) -> float:
        topMaxHeapA = -1 * self.maxHeapA[0]
        if (len(self.minHeapB) > 0):
            topMinHeapB = self.minHeapB[0]
            if (len(self.maxHeapA) == len(self.minHeapB)):
                return (topMaxHeapA + topMinHeapB)/2
            # in the case of odd numbered amounts, if the length of max heap A is greater than min Heap B,
            # the top will be the median, i.e A = [-3, -2, -1], B = [3, 4]
            # here, the max is 3 (-3 * -1) from the maxHeap and min is 3 from minHeap,
            # because len(A) > len(B), we just take the max A as the median
            # vice versa, if it was A = [-2, -1] and B = [3,3,4], then we'd take the min of B as the median
            elif (len(self.maxHeapA) > len(self.minHeapB)):
                return topMaxHeapA
            else:
                return topMinHeapB
        return topMaxHeapA

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()