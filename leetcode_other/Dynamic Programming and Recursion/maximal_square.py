"""
https://www.youtube.com/watch?v=6X7Ha2PrDmM&ab_channel=NeetCode
https://leetcode.com/problems/maximal-square/

Time: O(M*N)
Space: O(M*N)

1) The key idea is that we can continue to check a 2x2 series of squares (the down, right, diag) to see if 
these values are 1, and then within our cache, we store the length of the square if we're able to create the 2x2.
2) Then we can use the cached values to figure out if we can make an even larger square by adding 
1 + min(down, right, diag) directions. 
3) If there are any zeroes, we can't create a square so we'd mark that cell as 0, and any previous calls
that include this cell also cannot form a valid square.

Example:

matrix, where rows = 4 and cols = 5
1 0 1 0 0
1 1 1 1 1
1 1 1 0 0
1 1 1 1 1

1st recursive call, starting from 0, 0
r = 0 c = 0
down = helper(1, 0) <-- goes down this path
..

2nd recursive call
r = 1 c = 0
down = helper(2, 0)
..

3rd recursive call
r = 2 c = 0
down = helper(3, 0)
..

4th recursive call
r = 3 c = 0
down = helper(4, 0)
base case reached r >= rows, returns 0

back to 3rd recursive call
r = 3 c = 0
down = helper(3, 0) (complete)
right = helper(3, 1) <-- goes down this path
..

5th recursive call
r = 3 c = 1
down = helper(4, 1) (this returns 0, I'll skip it in this example)
right = helper(3, 2) <-- goes down this path
..

6th recursive call
r = 3 c = 2
down = helper(4, 2) (this returns 0)
right = helper(3, 3)

7th recursive call
r = 3 c = 3
down = helper(4, 3) (returns 0)
right = helper(3, 4)

8th recursive call
r = 3 c = 4
down = helper(4, 4) (returns 0)
right = helper(3, 5)

9th recursive call
r = 3 c = 5
down = helper(4, 5) returns 0 
base case reached for right

back to 8th recursive call
r = 3 c = 4
down = helper(4,4) (returns 0)
right = helper(3, 5) (returns 0)
diag = helper(4, 5) (should also return 0)

cache[(3, 4)] = 0
Because matrix[3][4] is 1, assign cache[(3, 4)] to 1 
return 1

our cache looks something like this:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

back to 7th recursive call
r = 3 c = 3
down = helper(4, 3) (returns 0)
right = helper(3, 4) (returns 1)
diag = helper(4, 4) (should also return 0)

cache[(3, 3)] = 0
Because matrix[3][3] is 1, we know that we can at least create a square with length 1 here,
so assign cache[(3, 3)] = 1

returns 1

our cache looks something like this:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1

back to 6th recursive call
r = 3 c = 2
down = helper(4, 2) (this returns 0)
right = helper(3, 3) (returns 1)
diag = helper(4, 3) (should also return 0 )

cache[(3, 2)] = 0, matrix[3][2] is 1, so assign cache[(3,2)] as 1 and return 1

our cache looks something like this:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 1 1

back to 5th recursive call
r = 3 c = 1
down = helper(4, 1) returns 0 
right = helper(3, 2) returns 1 
diag = helper(4, 2) (should return 0)

cache[(3, 1)] = 0, matrix[3][1] is 1, so return 0

our cache looks something like this:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 1 1 1 1


back to 4th recursive call
r = 3 c = 0
down = helper(4, 0) (returns 0)
right = helper(3, 1) (returns 1)
diag = helper(4, 2) (returns 0) 

cache[(3, 0)] = 0, matrix[3][0] is 1 however, so assign
cache[(3, 0)] = 1, and returns 1

our cache looks something like this:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1

back to 3rd recursive call
r = 2 c = 0
down = helper(3, 0) (returns 0)
right = helper(2, 1) <-- goes down this path

10th recursive call
r = 2 c = 1
down = helper(3, 1) (returns 1 because we can get it from cache)
right = helper(2, 2) <-- goes down this path

... after a few recursive calls later, the cache ends up looking like this

notice the 3, at this point, we would've taken the min of down, right, diag which is was 
2 at coordinate (1, 0), and added it to become 3

0 0 0 0 0
3 2 1 1 1 
2 2 1 0 0
1 1 1 1 1

after the rest of the recursion finishes,
we find the max of all the cache values and square the final result to get the area
to get an answer of 9

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = dict()
        
        def helper(r, c):
            if r >= rows or c >= cols:
                return 0
            if (r, c) not in cache:
                down = helper(r+1, c)
                right = helper(r, c+1)
                diag = helper(r+1, c+1)
                
                cache[(r, c)] = 0
                
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            return cache[(r, c)]
        helper(0, 0)
        return max(cache.values()) ** 2