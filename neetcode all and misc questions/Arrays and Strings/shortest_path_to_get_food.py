"""
https://leetcode.ca/2021-03-13-1730-Shortest-Path-to-Get-Food/
(Premium Problem)

Key Concepts:
Use standard BFS, where you store the coordinates as well as the distance traveled
in a tuple within your queue

Time Complexity: O(N*M) + O(N+M) to find the * position, and then an additional O(N+M) to perform the search
Space Complexity: O(N*M) for the visited set, which could potentially hold all 
"""
def inBounds(i, j, grid):
	return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def shortestPath(grid):
	from collections import deque
	# find the * starting point
	m = len(grid)
	n = len(grid[0])
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	minDistance = float("inf")
	for i in range(m):
		for j in range(n):
			if grid[i][j] == "*":
				q = deque()
				q.append((i,j,0))
				visited = set()
				visited.add((i,j))
				while (q):
					coord1, coord2, distance = q.popleft()
					# if food is found, record the min distance
					# go to the next iteration since we don't need to continue traversing after we've
					# found food 
					if grid[coord1][coord2] == "#":
						minDistance = min(distance, minDistance)
						continue
					for d in directions:
						x, y = d	
						newX, newY = coord1 + x, coord2 + y
						if inBounds(newX, newY, grid) and grid[newX][newY] != "X" and (newX, newY) not in visited:
							q.append((newX, newY, distance + 1))
							visited.add((newX, newY))
				break
	return minDistance if minDistance != float("inf") else -1

grid1 = [
	["X", "X", "X", "X", "X", "X"],
	["X", "*", "O", "O", "O", "X"],
	["X", "O", "O", "#", "O", "X"],
	["X", "X", "X", "X", "X", "X"],
]
assert shortestPath(grid1) == 3
print(shortestPath(grid1))

grid2 = [
	["X", "X", "X", "X", "X"],
	["X", "*", "X", "O", "X"],
	["X", "O", "X", "#", "X"],
	["X", "X", "X", "X", "X"],
]

assert shortestPath(grid2) == -1
print(shortestPath(grid2))


grid3 = [
	["X","X","X","X","X","X","X","X"],
	["X","*","O","X","O","#","O","X"],
	["X","O","O","X","O","O","X","X"],
	["X","O","O","O","O","#","O","X"],
	["X","X","X","X","X","X","X","X"]
]

assert shortestPath(grid3) == 6
print(shortestPath(grid3))


grid4 = [["O","*"],["#","O"]]

assert shortestPath(grid4) == 2
print(shortestPath(grid4))


grid5 = [["X","*"],["#","X"]]

assert shortestPath(grid5) == -1
print(shortestPath(grid5))

