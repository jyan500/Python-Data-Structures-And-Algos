'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
More efficient solution: https://www.youtube.com/watch?v=JNKmQffox6A&ab_channel=TimothyHChangTimothyHChang

test case #1: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
test case #2: [[3,3,3],[3,1,3],[0,2,4]]
'''

"""
Revisited 10/2/2024 with a similar solution, except
the placement of when to add the cell to visited is moved into the if () statement,
and the DFS call doesn't return anything. It just sets a res array which contains two flags
[isPacific, isAtlantic]. When starting from an (i, j) and running DFS until it reaches both the pacific
and atlantic, this would set both flag values to true within the array. Immediately after if both
flags are True, we can just return nothing to stop the recursion.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isPacific(i, j):
            return i == 0 or j == 0
        def isAtlantic(i, j):
            return i == len(heights)-1 or j == len(heights[0])-1
        def inBounds(i, j):
            return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        def dfs(i, j, visited, res):
            if isPacific(i, j):
                res[0] = True
            if isAtlantic(i, j):
                res[1] = True
            if res[0] and res[1]:
                return 
            for x, y in directions:
                newX = i + x
                newY = j + y

                # important that the height of the next grid cell must be less than or equal to the current cell in order for the water to flow
                if inBounds(newX, newY) and (newX, newY) not in visited and heights[newX][newY] <= heights[i][j]:
                    visited.add((newX, newY))
                    dfs(newX, newY, visited, res)

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                pacificAtlantic = [False, False]
                dfs(i, j, set(), pacificAtlantic)
                pacific, atlantic = pacificAtlantic
                if (pacific and atlantic):
                    res.append([i,j])
        return res
"""
8-18-2023
Condensed Solution
"""
class Solution:
    def inBounds(self, x, y, heights):
        return 0 <= x < len(heights) and 0 <= y < len(heights[0])
    
    def isPacific(self, x, y):
        return x == 0 or y == 0

    def isAtlantic(self, x, y, heights):
        return x == len(heights)-1 or y == len(heights[0])-1
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j, heights, visited, temp):
            if temp[0] and temp[1]:
                return True
            if self.isPacific(i, j):
                temp[0] = True
            if self.isAtlantic(i, j, heights):
                temp[1] = True
            visited.add((i, j))
            for d in self.directions:
                x, y = d
                newX, newY = i+x, y+j
                if self.inBounds(newX, newY, heights) and (newX, newY) not in visited:
                    if heights[newX][newY] <= heights[i][j]:
                        dfs(newX, newY, heights, visited, temp)
            return temp[0] and temp[1]
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if dfs(i, j, heights, set(), [False, False]):
                    self.res.append([i,j])
        return self.res

# revisited on 7-14-2023, brute force solution that's O(N^2 * (N + M)),
# where M is the amount of nodes traversed starting from N within the DFS
class Solution2:
    def isPacific(self, heights: [[int]], i:int, j:int) -> bool:
        return i < 0 or j < 0
    
    def isAtlantic(self, heights: [[int]], i:int, j:int) -> bool:
        return i > len(heights) - 1 or j > len(heights[0]) - 1
    
    def inBounds(self, heights: [[int]], i:int, j:int) -> bool:
        return i >= 0 and j >= 0 and i <= len(heights) - 1 and j <= len(heights[0]) - 1
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                # if we're able to reach pacific and atlantic from these coordinates
                # save the result
                if self.dfs(heights, i, j, set(), [False, False]):
                    result.append((i, j))
        return result
    
    def dfs(self, heights: List[List[int]], i:int, j:int, visited: set, reached: list):
        left = (i-1, j)
        right = (i+1, j)
        up = (i, j-1)
        down = (i, j+1)
        
        leftX, leftY = left
        rightX, rightY = right
        upX, upY = up
        downX, downY = down
        
        visited.add((i, j))
        # no need to continue traversing if we've already found valid paths to 
        # pacific and atlantic
        if reached[0] and reached[1]:
            return True
        if self.isPacific(heights, leftX, leftY) or self.isPacific(heights, upX, upY):
            # mark this cell as reaching pacific for future recursive calls
            # if we're still traversing the matrix
            reached[0] = True
        if self.isAtlantic(heights, rightX, rightY) or self.isAtlantic(heights, downX, downY):
            # mark this cell as reaching atlantic for future recursive calls
            # if we're still traversing the matrix
            reached[1] = True
        # check to make sure the value at the index is less than the current,
        # as we're only allowed to move in the direction of decreasing or equal value
        if self.inBounds(heights, leftX, leftY) and heights[leftX][leftY] <= heights[i][j] and left not in visited:
            self.dfs(heights, leftX, leftY, visited, reached)
        if self.inBounds(heights, rightX, rightY) and heights[rightX][rightY] <= heights[i][j] and right not in visited:
            self.dfs(heights, rightX, rightY, visited, reached)
        if self.inBounds(heights, upX, upY) and heights[upX][upY] <= heights[i][j] and up not in visited:
            self.dfs(heights, upX, upY, visited, reached)
        if self.inBounds(heights, downX, downY) and heights[downX][downY] <= heights[i][j] and down not in visited:
            self.dfs(heights, downX, downY, visited, reached)
        
        return reached[0] and reached[1]
        
## My original brute force solution (how to optimize?)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## flow to both the atlantic and pacific?
        ## it means that there is path from (i, j) to the pacific AND a path to atlantic
        ## where the pacific is cells on row 0 or column (top and left)
        ## and the atlantic is cells on row i = len(heights) - 1 and column j = len(heights) - 1
        result = []
 
        ## unmark current cell as visited
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                # print('for ', (i,j))
                # print('-------------------')
                if (self.dfs(heights, i, j, [False, False])):
                    result.append([i,j])
        return result

    def dfs(self, heights, i, j, reached):
        ## if we know we can reach the pacific and atlantic, than we don't need to continue onto the rest of the code 
        ## to cut down on unnecessary search and just
        ## keep returning true (there's probably a better way of doing this though) 
        if (reached[0] and reached[1]):
            return True
        ## at the current cell that we're at, are we at the boundaries?
        # print('current node: ', (i,j))
        # print('value of reached: ', reached)
        ## top and left sides of the matrix
        reached_pacific = (i <= len(heights) - 1 and j == 0) or (i == 0 and j <= len(heights[0]) - 1)
        ## bottom and right sides of the matrix
        reached_atlantic = (i == len(heights) - 1 and j <= len(heights[0]) - 1) or (i <= len(heights) - 1 and j == len(heights[0])-1)
        if (i >= 0 or i <= len(heights) - 1 and j >= 0 or j <= len(heights[0]) - 1):
            
            if (reached_pacific):
                # print('Reached Pacific')
                ## reached pacific
                reached[0] = True

            if (reached_atlantic):
                # print('Reached atlantic')
                reached[1] = True

        temp = heights[i][j]

        ## mark the current cell as visited
        heights[i][j] = '#'
        
        # print('current value of the cell: ', temp)
        ## dfs in 4 directions to check for possible paths
        ## if the current cell's value is greater than or equal to the cell to the right

        
        if (j+1 <= len(heights[0]) - 1 and heights[i][j+1] != '#' and temp >= heights[i][j+1]):
            # print('going right')
            self.dfs(heights, i, j + 1, reached)
        ## if the current cell's value is greater than or equal to the cell to the left
        if (j-1 >= 0 and heights[i][j-1] != '#' and temp >= heights[i][j-1]):
            # print('going left')
            self.dfs(heights, i, j - 1, reached)
        ## if the current cell's value is greater than or equal to the cell below
        if (i+1 <= len(heights) - 1 and heights[i+1][j] != '#' and temp >= heights[i+1][j]):
            # print('going down')
            self.dfs(heights, i + 1, j, reached)
        ## if the current cell's value is greater than or equal to the cell above
        if (i-1 >= 0 and heights[i-1][j] != '#' and temp >= heights[i-1][j]):
            ## print('going up')
            self.dfs(heights, i - 1, j, reached)
        
        heights[i][j] = temp
        # print('backtracking, current node is ', (i, j))
        return reached[0] and reached[1]


## Timothy Chang's more optimal solution in O(M*N) time and O(M*N) space
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])
        pacific = []
        atlantic = []
        visited_pacific = set()
        visited_atlantic = set()
        
        ## the approach is that we perform a depth first search only on the boundaries of the 
        ## grid, and we move to a cell where the value is greater than before, since
        ## we know that if the next cell is greater, than the cell with the higher value can
        ## have water flow to the cell that is lower (which is the current cell)
        ## if we can no longer traverse in a direction, then we stop the recursion
        ## we will do this twice (once for the pacific boundaries and once for the atlantic)
        ## once we've found the cells in our visited pacific and visited atlantic,
        ## then we will perform an intersection to get the cells that can reach both
        ## pacific and atlantic
        
        ## store the values for the left boundary of the grid (pacific) and the right boundary of the grid (atlantic)
        for i in range(M):
            pacific.append([i, 0])
            atlantic.append([i, N-1])
        ## store the values for the top boundary of the grid (pacific) and the bottom boundary of the grid (atlantic)
        for i in range(N):
            pacific.append([0, i])
            atlantic.append([M-1, i])
        
        for i,j in pacific:
            self.dfs(heights, i, j, M, N, visited_pacific)
        for i,j in atlantic:
            self.dfs(heights, i, j, M, N, visited_atlantic)
        
        return visited_pacific.intersection(visited_atlantic)
        
    def dfs(self, island, i, j, M, N, visited):
        ## right, left, down, up
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        ## add to visited
        visited.add((i,j))
        
        ## for each direction
        for x, y in directions:
            ## if we're in the boundaries
            next_x = i + x
            next_y = j + y
            if (0 <= next_x <= M-1 and 0 <= next_y <= N-1):
                ## if the next value is greater than our current, and the next value is not in visited
                ## continue to recur
               
                if (island[i][j] <= island[next_x][next_y] and (next_x, next_y) not in visited):
                    self.dfs(island, next_x, next_y, M, N, visited)
    
        
        
        
        
        

    