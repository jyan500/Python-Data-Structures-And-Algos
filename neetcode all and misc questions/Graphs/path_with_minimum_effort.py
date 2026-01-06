class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Optimal Solution uses Djikstra's Algorithm
        BFS with min heap, where we store the absolute difference in heights
        found so far as the weight. 

        That way, in the min heap, it'll constantly be picking the smallest absolute different in
        heights found so far and going down that path. 
        So once we've reached the bottom right hand corner, that will be the smallest absolute
        difference found and we can return that
        """
        def inBounds(i,j):
            return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        import heapq
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        minHeap = []
        heapq.heappush(minHeap, (0,0,0))
        while (minHeap):
            curDifference,i,j = heapq.heappop(minHeap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                # by using the min heap, we would've travelled
                # the path that results in the smallest possible absolute
                # height difference, so we can just return that here
                return curDifference
            for x,y in directions:
                newX = i + x
                newY = j + y
                if inBounds(newX, newY):
                    heightDiff = abs(heights[i][j] - heights[newX][newY])
                    # push the max between the absolute height difference
                    # and the current absolute height difference to the heap
                    heapq.heappush(minHeap, (max(heightDiff, curDifference), newX, newY))

        # in the case of an empty array, or only one element, return 0     
        return 0

        """
        DFS Brute Force solution checks all paths
        """
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # visited = set()
        # M = len(heights)
        # N = len(heights[0])
        # def inBounds(i, j):
        #     return 0 <= i < M and 0 <= j < N

        # self.res = float("inf")
        # def dfs(i, j, curDifference):
        #     if i == M - 1 and j == N - 1:
        #         self.res = min(self.res, curDifference)
        #         return
        #     if (i,j) in visited:
        #         return 
        #     visited.add((i,j))
        #     for x, y in directions:
        #         newX = i + x
        #         newY = j + y
        #         if (inBounds(newX, newY)):
        #             difference = heights[newX][newY] - heights[i][j]
        #             dfs(newX, newY, max(difference, curDifference))
        #     # to allow other paths to traverse down this cell, we have to remove
        #     # this from the visited set after the recursive path has finished
        #     visited.remove((i, j))
        # dfs(0, 0, 0)
        # return self.res if self.res != float("inf") else 0

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
        
            
            