class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Neetcode: https://youtu.be/XQlxCCx2vI4
        
        The only difference between my solution and Neetcode is that instead of removing (i,j) from visited when
        reaching the bottom right hand cell, Neetcode just makes an exception where if newX == len(heights)-1 and newY == len(heights[0])-1,
        you can still visit it.

        BFS but using a min heap to always travel on the smallest weights first (Djikstra's), in this case the weight is defined as the minimum of the max absolute difference between two consecutive cells. The min heap helps to pick the path that has the smallest absolute difference
        Djikstra's Time Complexity: O(V + ELogV)
        """
                
        def inBounds(x, y):
            return 0 <= x < len(heights) and 0 <= y < len(heights[0])
        import heapq
        minHeap = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        heapq.heappush(minHeap, (0, 0, 0))
        minAbsDistance = float("inf")
        visited = set()
        while (minHeap):
            absDistance, i, j = heapq.heappop(minHeap)

            if ((i,j) in visited):
                continue
            visited.add((i,j))
            # if reached bottom right hand corner, return
            # the absolute distance between this cell and second to last cell
            # you have to make sure to "unvisit" this cell by removing it,
            # otherwise you would not find a separate path
            if i == len(heights)-1 and j == len(heights[0])-1:
                minAbsDistance = min(minAbsDistance, absDistance)
                visited.remove((i,j))
                continue
                
            for x, y in directions:
                newX = i + x
                newY = j + y
                if (inBounds(newX, newY)):
                    # find the absolute difference between the current cell
                    # and the proposed cell
                    newAbsDistance = abs(heights[i][j] - heights[newX][newY])
                    # if we found a new max absolute difference, we have to account for this on this path
                    # then push onto the minheap
                    heapq.heappush(minHeap, (max(absDistance,newAbsDistance), newX, newY))
            
        return minAbsDistance
        
            
            