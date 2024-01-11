"""
https://www.lintcode.com/problem/663/
"""
from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        from collections import deque
        # write your code here
        """
        Brute Force:
        1) Starting from INF, use BFS, track the current coords
        and the distance in a tuple within the queue
        2) Keep track of a dict to get the minimum distances for each (i, j), ensuring
        that we don't overwrite an INF which would disrupt the path finding for a future coordinate

        The issue with this solution is that we visit the same cells multiple times, see the solution
        below which is more efficient.
        """
        # m = len(rooms)
        # n = len(rooms[0])
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # minDistances = dict()
        # def inBounds(i, j, m, n):
        #     return 0 <= i < m and 0 <= j < n
        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == 2147483647:
        #             minDistances[(i, j)] = 2147483647
        #             q = deque()
        #             q.append((i, j, 0))
        #             visited = set((i, j))
        #             while (q):
        #                 x, y, distance = q.popleft()
        #                 if rooms[x][y] == 0:
        #                     minDistances[(i, j)] = min(distance, minDistances[(i, j)])
        #                     break
        #                 for d in directions:
        #                     x2, y2 = d
        #                     newX, newY = x2 + x, y2 + y
        #                     if inBounds(newX, newY, m, n) and (newX, newY) not in visited and (rooms[newX][newY] == 0 or rooms[newX][newY] == 2147483647):
        #                         visited.add((newX, newY))
        #                         q.append((newX, newY, distance + 1))

        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) in minDistances:
        #             rooms[i][j] = minDistances[(i, j)]

        """
        NeetCode (Optimized Solution)
        https://www.youtube.com/watch?v=e69C6xhiSQE&ab_channel=NeetCode
        1) You can run BFS starting from each gate where rooms[i][j] == 0
        2) From there, just increment the distance out for each room, where rooms[i][j] = INF, level by level, and keep a visited
        set to prevent overwriting the same room with a different value. Increment the dist after going through the level

        When adding the for loop within the queue BFS, it'll add all the neighbors for a starting point,
        and then go to the next starting point. For example, gate (0, 2), adds all the neighbors for (0, 2), and then
        adds all the neighbors for (3, 0). In the next iteration, it'll pop out all neighbors for (0, 2) first, and then
        all for (3, 0)

        Time Complexity: O(N * M)
        """
        m = len(rooms)
        n = len(rooms[0])
        visited = set()
        q = deque()
        dist = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inBounds(i, j, m, n):
            return 0 <= i < m and 0 <= j < n

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j))
        
        while (q):
            for i in range(len(q)):
                x, y = q.popleft()
                if rooms[x][y] == 2147483647:
                    rooms[x][y] = dist
                for d in directions:
                    x2, y2 = d
                    newX, newY = x+x2, y+y2
                    if inBounds(newX, newY, m, n) and (newX, newY) not in visited and rooms[newX][newY] == 2147483647:
                        visited.add((newX, newY))
                        q.append((newX, newY))
            dist += 1

                        
