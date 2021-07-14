'''
Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
The demolition robot cannot enter 0 trenches and cannot leave the matrix.

Assumptions made: topleft corner of the grid is always 1, and there is always a 9 within the array somewhere (doesn't necessarily have to be reachable)
Sample Input :
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]]
Sample Output :
3
'''
class Solution:
	def robot(self, grid: [[int]]) -> int:
		return self.dfs(grid, 0,0)

	def dfs(self, grid: [[int]], i: int, j: int) -> int:
		total = 0
		min_total = float('inf')
		if (grid[i][j] == 9):
			return 0
		## down
		temp = grid[i][j]
		grid[i][j] = 0
		if (0 <= i+1 < len(grid) and 0 <= j < len(grid[0]) and grid[i+1][j] != 0):
			print('going down to ', grid[i+1][j])
			total = 1 + self.dfs(grid, i+1, j)
		## up
		if (0 <= i-1 < len(grid) and 0 <= j < len(grid[0]) and grid[i-1][j] != 0):
			print('going up to ', grid[i-1][j])
			total = 1 + self.dfs(grid, i-1, j)
		## left
		if (0 <= i < len(grid) and 0 <= j+1 < len(grid[0]) and grid[i][j+1] != 0):
			print('going left to ', grid[i][j+1])
			total = 1 + self.dfs(grid, i, j+1)
		## right
		if (0 <= i < len(grid) and 0 <= j-1 < len(grid[0]) and grid[i][j-1] != 0):
			print('going right to ', grid[i][j-1])
			total = 1 + self.dfs(grid, i, j-1)
		grid[i][j] = temp
		print('total: ', total)
		return total

if __name__ == '__main__':
	s = Solution()
	grid1 = [[1,0,0],[1,0,0],[1,9,1]]
	grid2 = [[1,0,0,1],[1,1,1,1],[0,1,9,0]]
	grid3 = [[1,0,0],[1,0,0],[1,9,1]]
	print(s.robot(grid1))
	print(s.robot(grid2))
