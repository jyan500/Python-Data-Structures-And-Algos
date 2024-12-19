class Solution:
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
                    
        
            