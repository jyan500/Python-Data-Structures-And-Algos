'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
https://leetcode.com/problems/climbing-stairs/
'''
class Solution:
	## iterative fibonacci solves this problem, since the number of ways to get 
	## to the current step is the previous two numbers added together, which is modeled by the fibonacci sequence
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            prev_1 = 2
            prev_2 = 3
            val = 0
            for i in range(3, n):
                val = prev_1 + prev_2
                prev_1 = prev_2
                prev_2 = val
        return val
                    