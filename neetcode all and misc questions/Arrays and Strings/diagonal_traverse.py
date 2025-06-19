class Solution:
    class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Revisited on 6/17/2025
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2

        0,0 0,1 0,2 0,3
        1,0 1,1 1,2 1,3
        2,0 2,1 2,2 2,3
        3,0 3,1 3,2 3,3

        Approach:
        we can start by iterating starting from the top row
        0,0 -> 0, 1 -> 0,2 -> 0,3
        and then going down this row
        1,3 -> 2,3 -> 3,3

        the reasoning is that in this direction, we're always reaching the 
        top of each diagonal, so it ensures we cover every diagonal

        for example 0,0 is the only element in the first diagonal
        0,1, we do (x+1, y-1) to get the next element in the diagonal, which is 1,0
        0,2 we do (x+1, y-1) to get the next element in the diagonal, which is 1,1,
        and then 2,0
        and so on...

        we'll also store each element in a separate list.
        Once we have each diagonal in nested lists, we reverse every other nested list 
        to represent the proper direction that's mentioned in the problem,
        and then merge all the lists together.

        Time: O(N*M)
        Space: O(N*M)
        """
        def inBounds(x, y, rows, cols):
            return x >= 0 and x < rows and y >= 0 and y < cols
        rows = len(mat)
        cols = len(mat[0])
        elements = []
        for i in range(0, cols):
            x = 0
            y = i
            diagonal = []
            while inBounds(x, y, rows, cols):
                diagonal.append(mat[x][y])
                x += 1
                y -= 1
            elements.append(diagonal)
        # we already have the diagonal starting from (0, cols-1), so we can
        # start at (1, cols-1) instead
        for j in range(1, rows):
            x = j
            # last column
            y = cols - 1
            diagonal = []
            while inBounds(x, y, rows, cols):
                diagonal.append(mat[x][y])
                x += 1
                y -= 1
            elements.append(diagonal)
        # reverse every other list and merge
        result = []
        for i in range(len(elements)):
            if i % 2 == 0:
                elements[i].reverse()
            result.extend(elements[i])
        return result

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        1st diag starts from bottom left to top right
        2nd diag starts from top right to bottom left and alternates
        
        in example 1:
        1 2 3
        4 5 6 
        7 8 9
        
        the indices that are being iterated are like so:
        0,0 to 0,0
        1,0 to 0,1
        2,0 to 1,1 to 0,2
        2,1 to 1,2
        2,2 to 2,2
        
        when moving between diagonal indices, you're adding to (x, y),
        +1, -1 or -1, +1
        
        ** keep two tuples l = (0, 0), r = (0,0)
        they will represent the range at which you begin performing (+1, -1) OR (-1, +1) on the coordinates.
        You then add the values at each coordinate into the list, alternating based on whether you start from the top right
        or bottom left. Once you've hit the corner where l[0] == N - 1 and r[1] == N - 1, you only increment the y value
        on the l tuple, and x value for the r tuple to stay in bounds.
        
        
        It's also possible the rows and cols of the matrix are different
        1 2 3 4
        5 6 7 8
        9 1 2 3
        
        this would make the algorithm a bit different, however...
        
        If you have an M X N, you can pad the M X N with 0's to get an N x N,
        so the algorithm stays consistent. In this particular problem, you can 
        pad it with a sentinel value, and then remove the sentinel value in the final result
        
        so in this example:
        1 2 3 4
        5 6 7 8 
        9 1 2 3
        
        padded to
        
        1 2 3 4
        5 6 7 8 
        9 1 2 3
        * * * *
        
        in this example a (2 x 3)
        1 2
        5 6
        9 1
        
        can be padded to
        1 2 *
        5 6 *
        9 1 *
        
        a 1 x 3 would get padded to a 3 x 3
        1
        5 
        9
        
        to 
        1 * *
        5 * *
        9 * *
        
        ****
        This solution works but get's a memory limit exceeded on Leetcode
        
        Rather than padding the input array, we can treat the indices **as if** the array were that size,
        and if we're out of bounds of the actual array, we don't index into it.
        
        Making this edit gets a Time Limit exceed on Leetcode still, I think it's because we're doing too many un-necessary iterations
        due to treating the array like a N x N instead of M x N
        
        **************
        2nd Approach:
        To avoid the need for treating an M x N like an N x N, we can simplify the approach by always starting in the top right corner and going bottom left. Then, we can simply just perform (+1, -1) on the indices until we go out of bounds. This allows us to keep the algorithm of determining the diagonals consistent, because the first index we start with is either
        1) first row and moving towards the last column
        2) once the last column is reached, we stay on the last column moving towards the last row
        
        The pictorial under "Approach 1" explains this: https://leetcode.com/problems/diagonal-traverse/solution/
        
        Then, in the result, if we store our result in nested lists, we can just alternate and reverse every other nested list,
        and extend to a final list and return
        
        1 2 3
        4 5 6
        7 8 9
        """
        M = len(mat)
        N = len(mat[0])
        diagonalLeft = (1, -1)
        cur = (0, 0)
        def inBounds(i, j, M, N):
            return 0 <= i < M and 0 <= j < N
        res = [] 
        while (cur[0] < M):
            x, y = cur
            inner = []
            # iterate diagonal from top right to bottom left, which is adding (+1, -1) to the current until you're out of bounds
            while (inBounds(x, y, M, N)):
                inner.append(mat[x][y])
                x += 1
                y -= 1
            # at first, we stay on the first row, and move only the y pointer until we reach the end of the columns
            if cur[1] < N - 1:
                cur = (cur[0], cur[1] + 1)
            # then, we stay on the last column and only change the row
            else:
                cur = (cur[0]+1, cur[1])
            res.append(inner)
        final = []
        for i in range(len(res)):
            if i % 2 == 0:
                res[i].reverse()
            final.extend(res[i])
        return final
                    
        
            