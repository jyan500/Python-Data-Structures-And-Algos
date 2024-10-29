class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Time: O(N**2) (chance to iterate through every cell in the grid at worst)
        Space: O(N**2) (chance to visit all cells)

        01
        10
        flipping one "zero" will turn two islands into one island
        11    01
        10 or 11
        
        010
        000
        001
        
        flipping two zeroes will turn two islands into one island
        
        010    011
        010    001
        011 or 001 
        
        1 1 1 1 1
        1 0 0 0 1
        1 0 1 0 1
        1 0 0 0 1
        1 1 1 1 1
        
        flipping one "zero" will turn two islands into one island
        
        1 1 1 1 1
        1 0 0 0 1
        1 0 1 0 1 , or any of the other four directional sides
        1 0 1 0 1
        1 1 1 1 1
        
        at a given point, how do I know whether I crossed onto a different island,
        or if i'm on the same island?
        
        seems like the only way would be to get all indices of one island. Then, any remaining 1's will by default
        be part of the 2nd island.
        
        Since there can only be two islands total, if I start at a given "one",
        and then run DFS, visiting all "ones" until i've visited all that are connected four-directionally from the starting point, I would've visited all the cells for one island. Therefore, all other "ones" should be a part of the 2nd island. If I start from a cell in the visited set, and attempt to flip a "0" to a "1", and then
        reach another "1", I would've crossed into the 2nd island, so the amount of "0"s that were flipped to "1"s would be the final answer. 
        To find the shortest amount of 0's, I would use BFS, initializing a queue
        containing tuples of all (i, j) pairs in the visited set, as well as the number of flips so far. 
        Any time I see a "0" during the BFS, I would increment numFlipped by one and put this onto the queue with the new coordinates

        If I reach a "1", this would mean I've reached the 2nd island, since all other "1"s belonging to the island I started at
        would've already been in visited set, so any new "1"s must be a part of the 2nd island. Take the min between the number of flips
        and the current min.
        
        """
        from collections import deque
        N = len(grid)
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inBounds(i, j):
            return 0 <= i < N and 0 <= j < N
        
        def dfs(i, j):
            visited.add((i,j))
            for x, y in directions:
                newX = i + x
                newY = j + y
                if inBounds(newX, newY) and grid[newX][newY] == 1 and (newX, newY) not in visited:
                    dfs(newX, newY)
        found = None
        for i in range(N):
            if found:
                break
            for j in range(N):
                if not found and grid[i][j] == 1:
                    found = (i,j)
                    break

        # run DFS to identify all cells of the first island
        dfs(found[0], found[1])
        
        # for each cell of the first island, begin a BFS, attempting to reach another "1" value,
        # which indicates the 2nd island is reached 
        q = deque([(pair, 0) for pair in visited]) # ((i, j), num of zeroes flipped)
        minFlipped = float("inf")
        while (q):
            pair, numFlipped = q.popleft()
            i, j = pair
            for x, y in directions:
                newX = x + i
                newY = y + j
                if inBounds(newX, newY) and (newX, newY) not in visited:
                    if (grid[newX][newY] == 0):
                        q.append(((newX, newY), numFlipped + 1))
                        visited.add((newX, newY))
                    else:
                        minFlipped = min(numFlipped, minFlipped)
        return minFlipped
                
            
        
                
        
        
            
        