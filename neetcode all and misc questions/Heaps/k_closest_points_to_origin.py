'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

https://leetcode.com/problems/k-closest-points-to-origin/

My approach was to use a heap to store coordinates and their distances to the origin
since we want the closest, we'd want the distance to be approaching zero,
meaning a min-heap, where we're minimizing the distance would be ideal
so the k=1 closest is the root

Some key takeaways from the problem are that if passing in a list of tuples to the heapify function in the heapq library,
heapify will take the first element in the tuple as the comparator to figure out the ordering of the different nodes within the heap

Time complexity: O(N) to call heapify, however for each K, we're calling heappop(), which is an O(LogN) operation
Therefore, the total time is O(N) + O(K * LogN), roughly O(NLogN)
Space complexity: O(N) to store the heap

'''
class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       
        
        ## create a list of tuples, where each tuple will contain the coordinate and distance of the coordinate sto the origin (0,0)
        to_heap = []
        for i in range(len(points)):
            x,y = points[i]
            distance = self.calculateDistance(x,y,0,0)
            to_heap.append((distance, points[i]))        

        ## heapify this list of tuples using the distance (tuple[0]) as the comparator
        ## note that in python documentation, if passing in a list of tuples, the heapq.heapify function 
        ## will use the first element of the tuple as a comparator assuming that the first element in the tuple
        ## is a built-in datatype or has a comparator already implemented
        heapq.heapify(to_heap)
       
        
        ## for the amount of k times, pop off the root and store the points as a list to return
        to_return = []
        for i in range(k):
            distance,points = heapq.heappop(to_heap)
            to_return.append(points)
        return to_return
        
    def calculateDistance(self, x1: int,y1: int,x2: int, y2: int) -> float:
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        