class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        you can go left, right, up, down and all diagonals (8 total directions)
        The goal is to go from the top left cell (0,0) to the bottom right cell (n-1, n-1),
            - only visiting cells that have value of 0
        
        BFS, starting from the top left corner
        since we want the shortest path, we'll put all the different 0 value cells
        that we can visit into a queue. and then at each level, evaluate if there any
        neighbors with value 0. By definition, once we reach the bottom right, the amount of levels
        that we took will show the length of the path needed. We can continue the BFS to see if there
        were any shorter paths

        This is a similar problem to rotting oranges and other shortest path style BFS problems.

        Time Complexity: O(N*M)
        Space: O(N*M)
        """
        from collections import deque
        def inBounds(i, j):
            return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])
        # if the starting point is a 1, we return -1, as there's no way for the path to only be 
        # 0's if the starting point is a 1.
        if grid[0][0] == 1:
            return -1

        q = deque()
        directions = [(0,1), (0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
        visited = set()
        # initialize at (0,0)
        q.append((0,0))
        distance = 1
        while (q):
            N = len(q)
            # since we're potentially adding elements to the queue, we only want to iterate
            # by "level", which indicates all the elements we added at a specific distance away
            # and nothing further
            for k in range(N):
                i, j = q.popleft()
                if (i,j) in visited:
                    continue
                # if we've reached the bottom right element 
                if i == len(grid)-1 and j == len(grid[0])-1:
                    return distance
                visited.add((i,j))
                for x, y in directions:
                    newX = x + i
                    newY = y + j
                    if inBounds(newX, newY) and grid[newX][newY] == 0:
                        q.append((newX, newY))    
            distance += 1
        return -1
