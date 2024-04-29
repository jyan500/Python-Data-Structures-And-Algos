class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Modified Djikstra's Algorithm (Path with the smallest max height)
        Time Complexity: 
        O(N^2LogN)
        
        Each heappop() takes LogN, and we do this up to N^2 times since it's a 
        2-D grid
        
        Similar to regular Djikstra, we use BFS, but instead of a queue, use a min heap. Also use a visited set
        1) Use a min heap to store the positions we want to visit, but 
        we want to store the max elevation that we've found so far within our path, since the goal is to get to the bottom right square with the least amount of elevation. Therefore, if went to a path that increases our overall elevation that we've visited, we need to factor that in even if later down the path, the elevation decreases.
        2) Along with storing the max elevation, we also store the row and column
        
        """
        import heapq
        def inBounds(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) 
        N = len(grid)
        visited = set()
        # initially, we store the value at grid[0][0] which is the elevation at 0, 0, as well as the coordinates 0, 0
        heap = [(grid[0][0],0,0)]
        # we're able to go in all four directions
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited.add((0,0))
        while (len(heap) > 0):
            elevation, i, j = heapq.heappop(heap)
            # if we reach N-1, N-1, this is our destination, the bottom right hand corner. Because we're using the min heap here, we guarantee that we minimized the elevation up to this point, so we can just return here
            if i == N - 1 and j == N - 1:
                return elevation
            # checking in all four directions, if in bounds and not visited yet,
            # we add the position into the heap, making sure to do 
            # max(current height, height of the next position) so we have an accurate representation of the elevation so far.
            for d in directions:
                x, y = d
                newX = i + x
                newY = j + y
                if inBounds(newX, newY) and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    heapq.heappush(heap, (max(elevation, grid[newX][newY]), newX, newY))

                    
            
        