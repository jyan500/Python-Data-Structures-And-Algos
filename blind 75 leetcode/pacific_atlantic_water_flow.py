'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
More efficient solution: https://www.youtube.com/watch?v=JNKmQffox6A&ab_channel=TimothyHChangTimothyHChang

test case #1: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
test case #2: [[3,3,3],[3,1,3],[0,2,4]]
'''

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
    
        
        
        
        
        

    