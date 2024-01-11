''' 
	Given an m x n matrix, return all elements of the matrix in spiral order. 
	https://leetcode.com/problems/spiral-matrix
	Aside: I was able to solve this one without referencing the answer first, but this answer is probably
	not the most efficient solution available.
	concept: iterate through the indicies in a spiral fashion, by keeping within the boundaries of the 
	matrix without hitting a coordinates that we've already visited
'''
"""
Revisited on 8/9/2023 with a similar concept but cleaner solution
O(N^M) time, where M is the number of rows and N is the number of columns
O(N^M) space, where M is the number of rows and N is the number of columns
"""

class Solution:
    def inBounds(self, i, j, matrix):
        return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # go as far to the right as you can
        # go as far down as you can
        # go as far left as you can
        # go as far up as you can
        # all of these, stop before you visit the same node again
        # repeat...
        visited = set()
        visited.add((0,0))
        numCells = len(matrix) * len(matrix[0])
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        res = [matrix[0][0]]
        i = 0
        j = 0
        while len(visited) < numCells:
            for d in directions:
                x, y = d
                while (True):
                    newX, newY = i+x,j+y
                    if self.inBounds(newX, newY, matrix) and (newX, newY) not in visited:
                        visited.add((newX, newY))
                        res.append(matrix[newX][newY])
                        i += x
                        j += y
                    else:
                        break
        return res
            
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res_list = []
        visited = []
        i = 0
        j = 0
        if (rows == 1):
            return matrix[0]
        for n in range(rows - 1):
        	## go to the right until we hit the number of cols or a coordinate that we've already visited
            while (j < cols and (i, j) not in visited):
                res_list.append(matrix[i][j])
                visited.append((i,j))
                j += 1
            ## since we've gone one over the boundary, decrease the value of j and increase the value of i
            ## to get to the next value that we need to add to our result list
            j -= 1
            i += 1

            ## go down until we reach the boundary number of rows, or a coordinate that we've already visited
            while (i < rows and (i, j) not in visited):
                print('second loop: ', (i,j))
                res_list.append(matrix[i][j])
                visited.append((i,j))
                i += 1
            ## since we've gone one over the boundary, decrease the value of i and decrease the value of j
            ## to get to the next value that we need to add to our result list
            i -= 1
            j -= 1
            print('between second and third loop: ', (i,j))
            ## go left until we reach the boundary number of rows, or a coordinate that we've already visited
            while (j >= 0 and (i , j) not in visited):
                print('third loop: ', (i, j))
                res_list.append(matrix[i][j])
                visited.append((i,j))
                j -= 1
            ## since we've gone one over the boundary, decrease the value of i and increase the value of j
            ## to get to the next value that we need to add to our result list
            j += 1
            i -= 1
            print('between third and fourth loop: ', (i, j))
            ## go up until we reach the boundary number of rows, or a coordinate that we've already visited
            while (i >= 0 and (i, j) not in visited):
                res_list.append(matrix[i][j])
                visited.append((i,j))
                i -= 1
            ## since we've gone one over the boundary, increase the value of i and increase the value of j
            ## to get to the next value that we need to add to our result list
            i += 1
            j += 1
            print('end of ' + '#' + str(n+1) + ' loop', (i,j))
           
        return res_list