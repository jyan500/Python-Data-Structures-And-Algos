class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/solutions/451787/python-o-m-n-k-bfs-solution-with-explanation/
        
        Time Complexity: O(N*M*K), where K is the amount of removals allowed. The additional K is because
        its possible to visit the same cell depending on the amount of removals that were taken in the BFS path.
        Space: O(N*M*K), because we can visit the same cell in the grid multiple times due to the amount of
        removals that are allowed

        perform BFS on (x, y, r, steps), where x, y is the coordinates, and r is
        the remaining amount of obstacles that can be removed, and steps is the amount
        of steps that have been taken so far.

        One aspect of this problem that's tricky and different from similar BFS problems is the visited set.
        Normally, we just track the (x, y), but in this problem, we track the remaining amount of removals we have as well.
        This is to prevent cases where multiple different paths are trying to visit the same coordinate, but one path
        has a different amount of removals taken than the others. In order to allow the same coordinate to be visited multiple times,
        we'd have to differentiate between these cases by tracking the amount of removals left as well.

        You have to account for this difference in the logic:
        1) When a proposed coordinate is an obstacle, and we have removals remaining AND we have not visited
        this cell already with the proposed amount of removals ((newX, newY, numRemovals - 1) not in visited):
            add to the queue and visited set
        2) When a proposed coordinate is NOT an obstacle, AND we have not visited this cell already given
        the amount of removals we have ((newX, newY, numRemovals) not in visited)
            add to queue and visited set

        """
        def inBounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        from collections import deque
        q = deque()

        q.append((0,0,k,0))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dest = (len(grid)-1, len(grid[0])-1)
        visited = set()
        visited.add((0,0,k))
        minSteps = float("inf")
        while (q):
            i, j, numRemovalsAllowed, steps = q.popleft()
            if (i, j) == dest:
                return steps
            for x, y in directions:
                newX = i + x
                newY = j + y
                if inBounds(newX, newY):
                    # if obstacle, decrement from the amount of removals allowed, also check to see if 
                    # another path with the same amount of removals has already visited this coordinate.
                    if grid[newX][newY] == 1 and numRemovalsAllowed > 0 and (newX,newY, numRemovalsAllowed-1) not in visited:
                        q.append((newX, newY, numRemovalsAllowed - 1, steps+1))
                        visited.add((newX, newY, numRemovalsAllowed-1))
                    # also check for an alternative path where you don't use the removal right away, check to make 
                    # sure the cell is not already visited by another path with the same amount of removals taken.
                    if grid[newX][newY] == 0 and (newX,newY, numRemovalsAllowed) not in visited:
                        q.append((newX, newY, numRemovalsAllowed, steps+1))
                        visited.add((newX, newY, numRemovalsAllowed))

        # if minSteps is still infinity, it means we couldn't reach the destination given
        # the amount of obstacle removals we were given,
        # return -1 in that case
        return minSteps if minSteps != float("inf") else -1