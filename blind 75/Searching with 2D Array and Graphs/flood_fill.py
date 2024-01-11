"""
https://leetcode.com/problems/flood-fill/
Very similar concept to the number of islands problem,
using DFS to traverse the matrix, 
and only visit matrix[i][j] if it's the same as the starting color

We can do a small optimization saying that if the startingColor == color,
we won't need to flood fill any remaining pixels

Time complexity: O(N * M), number of rows * number of columns
Space complexity: O(N * M), number of rows * number of columns
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [
            (0, -1), # left
            (0, 1), # right
            (-1, 0), # up
            (1, 0) # down
        ] 
        startingColor = image[sr][sc]
        if startingColor == color:
            return image
        def inBounds(image, i, j):
            return i >= 0 and i < len(image) and j >= 0 and j < len(image[i])
        def dfs(image, i, j, startingColor, color):
            if image[i][j] == startingColor:
                image[i][j] = color
                visited.add((i,j))
            for direction in directions:
                x, y = direction
                newX = i + x
                newY = j + y
                if inBounds(image, newX, newY) and (newX, newY) not in visited and image[newX][newY] == startingColor:
                    dfs(image, newX, newY, startingColor, color)
                
        dfs(image, sr, sc, startingColor, color)
        return image