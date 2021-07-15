'''
Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
The demolition robot cannot enter 0 trenches and cannot leave the matrix.

Assumptions made: there is always a 9 within the array somewhere (doesn't necessarily have to be reachable)
Sample Input :
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]]
Sample Output :
3
'''
from collections import deque

class Solution:
	def robot(self, grid: [[int]]) -> int:
		## Unknown time solution for dfs? O(M*N) seems unlikely, theres a lot of repeated work
		## return self.dfs(grid, 0,0)
		## BFS will be O(M*N) time, where M is the amount of rows and N is the amount of columns
		## O(min(M,N)) space, where M or N is depending on how many nodes are in the queue
		return self.bfs(grid)

	def to_add(self, i, j, row, col, grid, visited):
		return 0 <= i < row and 0 <= j < col and grid[i][j] != 0 and (i,j) not in visited

	def bfs(self, grid: [[int]]) -> int:
		frontier = deque()
		## start at the top left corner
		frontier.append((0,0,0))
		visited = [(0,0)]

		directions = [(1,0),(-1,0),(0,1),(0,-1)]
		while (frontier):
			## the key is that we store the distance that we've currently traveled along with the current index within our tuple
			i, j, dist = frontier.popleft()
			if (grid[i][j] == 9):
				return dist
			## get the neighbors of this (i,j), which are the nodes immediately to the left,right,up,down
			## if the grid's value is not 0 or grid value not in visited, add to the frontier
			else:
				for x,y in directions:
					if (self.to_add(i+x,j+y, len(grid), len(grid[0]), grid, visited)):
						neighbor = (i+x,j+y)
						neighbor_with_dist = (i+x,j+y, dist+1)
						frontier.append(neighbor_with_dist)
						visited.append(neighbor)
		return -1

	def dfs(self, grid: [[int]], i: int, j: int) -> int:
		total = float('inf') 
		min_total = float('inf')
		if (grid[i][j] == 9):
			return 0
		## down
		temp = grid[i][j]
		grid[i][j] = 0
		print('current index: ', i, j)
		if (0 <= i+1 < len(grid) and 0 <= j < len(grid[0]) and grid[i+1][j] != 0):
			print('going down to ', grid[i+1][j])
			total = min(total, 1 + self.dfs(grid, i+1, j))
		## up
		if (0 <= i-1 < len(grid) and 0 <= j < len(grid[0]) and grid[i-1][j] != 0):
			print('going up to ', grid[i-1][j])
			total = min(total, 1 + self.dfs(grid, i-1, j))
		## left
		if (0 <= i < len(grid) and 0 <= j+1 < len(grid[0]) and grid[i][j+1] != 0):
			print('going right to ', grid[i][j+1])
			total = min(total, 1 + self.dfs(grid, i, j+1))
		## right
		if (0 <= i < len(grid) and 0 <= j-1 < len(grid[0]) and grid[i][j-1] != 0):
			print('going left to ', grid[i][j-1])
			total = min(total, 1 + self.dfs(grid, i, j-1))
		grid[i][j] = temp
		print('total: ', total)
		return total

if __name__ == '__main__':
	s = Solution()
	## 3x3
	grid1 = [[1,0,0],[1,0,0],[1,9,1]]
	## 4x4
	grid2 = [[1,0,0,1],[1,1,1,1],[0,1,9,0]]
	## 5x5
	grid3 = [[1,1,1,9,0],[1,1,0,1,0],[1,1,1,1,0],[1,0,0,1,0],[1,1,1,1,0]]
	## no obstacle
	grid4 = [[1,0,0],[1,0,0],[1,0,1]]
	print('---------------grid1-------------\n')
	print(s.robot(grid1))
	print('---------------grid2-------------\n')
	print(s.robot(grid2))
	print('---------------grid3-------------\n')
	print(s.robot(grid3))
	print('---------------grid4-------------\n')
	print(s.robot(grid4))
