"""
https://leetcode.com/problems/rotting-oranges/

Concept:
1) Find all the rotting oranges in the grid and append to the queue,
at the same time, find all the fresh oranges in the queue to check
if we're able to visit all the fresh oranges and turn them into rotten ones.

2) Perform BFS by initially popping off the coordinates of the rotten oranges,
this will append the neighbors to the rotten oranges if they're fresh. At the next iteration,
this should count as one "minute" once we. We start at -1 for this reason, as the first iteration
where we begin our BFS doesn't count.

3) When the queue is empty, we should've visited all the fresh oranges that we could visit and see if 
it equals the amount of fresh oranges we started with. If so, return our minute count. If we couldn't visit
all fresh oranges, that means they were "fenced" off by zeroes, so return -1 since it's not possible.

some edge cases:
if there's only fresh oranges but no rotting oranges, it's not possible to make the fresh oranges rot,
so return -1

if there's no rotting oranges, but there's no oranges (all zeroes in the matrix), return 0. Same
case if there are only rotting oranges (return 0)

Time:
O(number of rotting oranges + number of fresh oranges)
Space:
O(number of fresh oranges) for the visited set
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS
        Revisited 12/23/2025
        find all the rotten oranges first and place them into
        the queue
        for each queue item, track both the cell and also the 
        current time, so when the BFS ends, you'll automatically
        have the smallest number of minutes
        """
        from collections import deque
        q = deque()
        M = len(grid)
        N = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inBounds(i, j):
            return 0 <= i < M and 0 <= j < N

        visited = set()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited.add((i,j))
        res = 0
        while (q):
            # continue to run BFS on each of the rotten oranges, and as we see fresh oranges,
            # turn these into rotten oranges, and increment the time
            # by the time the BFS finishes, we should have the minimum time
            for _ in range(len(q)):
                i, j, time = q.popleft()
                res = time
                for x, y in directions:
                    newX = x + i
                    newY = y + j
                    if inBounds(newX, newY) and grid[newX][newY] == 1 and (newX, newY) not in visited:
                        grid[newX][newY] = 2
                        visited.add((newX,newY))
                        q.append((newX, newY, time + 1))
        
        # check to see if no fresh oranges left first
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1
        
        # if no more fresh oranges, return the result 
        return res

class Solution:
    def inBounds(self, i, j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        m = len(grid[0])
        # visit all the ones first
        visitedOnes = set()
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    visitedOnes.add((i,j))
                if grid[i][j] == 2:
                    q.append((i,j))

        # Edge cases
        if len(q) == 0:
            if len(visitedOnes) > 0:
                return -1
            else:
                return 0
        else:
            if len(visitedOnes) == 0:
                return 0

        visited = set()
        minuteCount = -1
        while q:   
            for i in range(len(q)):
                xCoord, yCoord = q.popleft()
                if grid[xCoord][yCoord] == 1:
                    grid[xCoord][yCoord] = 2
                for d in directions:
                    x, y = d
                    newX, newY = x+xCoord, y+yCoord
                    if self.inBounds(newX, newY, grid) and (newX, newY) not in visited and grid[newX][newY] == 1:
                        q.append((newX, newY))
                        visited.add((newX, newY))
            minuteCount += 1
        if len(visited) == len(visitedOnes):
            return minuteCount
        else:
            return -1
                
                        
                        