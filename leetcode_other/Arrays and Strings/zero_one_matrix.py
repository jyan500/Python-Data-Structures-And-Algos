"""
https://leetcode.com/problems/01-matrix/
https://www.youtube.com/watch?v=Ezj3VDOfd5I&ab_channel=HappyCoding

7/31/2023
Key Concepts:
BFS to find the nearest distance

1) We think of the problem in reverse, where instead of starting from a non-zero element 
and finding a zero element, we flip the logic so that 
we visit all zeroes first, and then find the distance to a non-zero element.

2) By finding all zeroes, appending to our queue and visited set first,
we then do BFS on the zero element, and only adding elements to our queue that haven't been visited,
which are basically all non-zero elements. Once we visit our non-zero element, that will be the nearest distance
to a zero. 


"""
class Solution:
    def inBounds(self, x, y, mat):
        return 0 <= x < len(mat) and 0 <= y < len(mat[0])
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m = len(mat)
        n = len(mat[0])
        res = [[0] * n for _ in range(m)]
        visited = set()
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j, 0))
                    visited.add((i,j))
        while (q):          
            x1, y1, curLength = q.popleft()
            if mat[x1][y1] != 0:
                res[x1][y1] = curLength
            for d in directions:
                x2, y2 = d
                newX = x1 + x2
                newY = y1 + y2
                if self.inBounds(newX, newY, mat) and (newX, newY) not in visited:
                    q.append((newX, newY, curLength + 1))
                    visited.add((newX, newY))
        return res
        
            

            
            

            