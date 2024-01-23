"""
Why a greedy approach doesn't work:
https://leetcode.com/problems/grid-game/discuss/1486399/Can-anyone-explain-one-of-the-LC-Test-cases/1096023

I first attempted a DFS approach where I'd attempt to take a path that'd maximize robot 1's points, 
with the thought that by doing this, it'd automatically mean robot 2 would have less points.

However: 

The first robot's aim is to MINIMIZE the amount of points the second robot can gain, and not necessarily to maximize it's own points.

1 2 3 4
5 6 7 8

In this example, a greedy approach would have robot 1 taking the following path:
1 
5 6 7 8

This would create a total sum of 27, leaving robot 2 with the following path

0 2 3 4
0 0 0 0

Which would allow robot 2 with a total of 9

However, you can actually minimize robot 2's sum even further by taking this path with robot 1:
1 2
  6 7 8

This would leave robot 2 with the following:

0 0 3 4
5 0 0 0

As shown, robot 2's actual maximum sum should be 7 and not 9
------------------------------------------------------------

Therefore, it's more optimal to use a prefix sums concept to solve this problem,
since you need to track the remaining amount of points for robot 2 when considering
the path for robot 1

See the explanations below on the prefix sums

"""
class Solution:
	"""
	Time complexity: 
	O(N), where N is the number of columns
	Space complexity:
	O(N), where N is the number of columns
	"""
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pre1 = [grid[0][i] for i in range(n)]
        pre2 = [grid[1][i] for i in range(n)]
        """ 
        get the prefix sums for both the top and bottom of the grid.
        Remember for prefix sums, you always start at index 1, since at index 0,
        there's no previous element.
        """
        for i in range(1, n):
            pre1[i] = pre1[i] + pre1[i-1]
            pre2[i] = pre2[i] + pre2[i-1]
        """
        to find the path needed for robot 1 to minimize robot 2's score:
        1) we can iterate through the columns of the grid, because we know at some point
        robot 1 needs to go downwards. we can take advantage of this fact because
        we'll automatically know the path that robot 2 needs to take based on the remaining squares
        left in that row, thus knowing the scores via the prefix sums.
        
        1 2 3 4
        5 6 7 8
        
        if robot 1 takes 1 -> 5, then ...
        robot 2 automatically takes 2 3 4, because robot 1 would've needed to take 6 7 8 as a part of it's path
        
        if robot 1 takes 2 -> 6, then robot 2 takes either
        5 or
        2 3 4,
        
        because robot 1 would've taken 7 and 8, causing those values to become 0, so we only need to count 5 or 2 3 4
        
        2) Between the two options that robot 2 can take,
        the top one can be calulated using the total sum of the top row - the prefix sum at the point
        that robot 1 goes down (let's call this i)
        
        the bottom one is simply the prefix sum at i - 1, if i == 0 though, then it will just be 0 since
        there's no previous element
        
        3) After calculating the the two scores that robot 2 could have given robot 1's path when going down at i,
            we need to pick the maximum between these two since robot 2 wants to maximize it's score.
           
           max(top, bottom)
           
        4) However, we also want to minimize the overall score that robot 2 could have as our final answer,
            we would then take the min between the maximal score that robot 2 could have in this path,
            and our overall min
        
        In the example above, if robot 1 take 1 -> 5
        robot 2 takes 2 3 4
        
        Since 2 3 4 is a bigger sum, we'd choose this path (for a total of 9)
        
        However, in the next iteration
        if robot 1 takes 2 -> 6,
        robot 2 would get either 5 or 3 4
        
        3 4 is the maximum here (with a total of 7), so we'd choose that.
        However, 7 < 9, so we'd set the new answer to 7 instead.
        
        In the next iteration
        robot 1 takes 3 -> 7,
        robot 2 takes either 4 or 5,6
        
        Here 5 + 6 > 4, so the maximum is 11.
        However, 11 > 9, so 9 is still our minimum. Therefore, this path for robot 1
        of going down 3 -> 7 is not as optimal as going down 2 -> 6
        
        """
        total = sum(grid[0])
        res = float("inf")
        for i in range(n):
            top = total - pre1[i]
            bottom = pre2[i-1] if i > 0 else 0
            res = min(res, max(top, bottom))
        return res
            