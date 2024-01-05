"""
https://leetcode.com/problems/count-sub-islands/
Approach:
1) Find all the islands of grid1 using DFS:
	a) within the DFS, we keep track of a visited set,
	and whenever visiting a "1", we set it to "0" in the graph so we don't revisit it later on
	b) the visited set tells us the cells that we visited, and since we only visit "1"s within our 
	DFS, this comprises of a complete 4 directionally connected island
	c) we then save these cells into the "islands" set
2) Find all the islands of grid2
	a) Run the same DFS function, but this time, we use the "issubset" method to see if the island
	visited in grid2 is a subset of the complete set of islands that we created from searching grid1 above. 
	b) If so, we increment the count
3) Return the count, this will tell us all the islands in grid2 that were a subset of the islands in grid1

Time Complexity:
O(M*N* length of each island in grid2 * num islands in grid2), since the issubset() method would depend
on the length of the subset that we're comparing

Space Complexity:
O(M*N)
"""
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.islands = set()
        directions = [(0, 1), (0,-1), (1, 0), (-1, 0)]
        def inBounds(i, j, grid):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def dfs(i, j, g1, visited):
            g1[i][j] = 0
            for d in directions:
                x, y = d
                newX, newY = i + x, y + j
                if inBounds(newX, newY, g1) and (newX, newY) not in visited and g1[newX][newY] == 1:
                    visited.add((newX, newY))
                    dfs(newX, newY, g1, visited)
            return visited
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1:
                    v1 = set()
                    v1.add((i,j))
                    visited = dfs(i, j, grid1, v1)
                    self.islands.update(visited)
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    v2 = set()
                    v2.add((i,j))
                    visited = dfs(i,j,grid2,v2)
                    if visited.issubset(self.islands):
                        count += 1
        return count
        
