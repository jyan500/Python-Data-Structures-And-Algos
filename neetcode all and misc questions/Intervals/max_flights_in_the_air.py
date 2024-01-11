'''
Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

If landing and taking off of different planes happen at the same time, we consider landing should happen at first.

Example
Example 1:

Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second airplane takes off at 2 and lands at 3.
The third airplane takes off at 5 and lands at 8.
The forth airplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.
Example 2:

Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
Explanation: Landing happen before taking off.

https://www.lintcode.com/problem/391/
(Leetcode Premium)
'''
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        ## concept
        ## sort the intervals by start time O(NLogN)
        ## use a stack to keep track of flights in the air so far
        ## if a flight is no longer overlapping with our current interval, we need to pop off the previous elements in our stack
        ## to check if they're still overlapping with our current interval
        ## else if it is overlapping, we continue to append to our stack
        ## at the end, the flights that are still in the air are the ones left in our stack, so just return the length
        ## Time complexity: O(NLogN + (O(N) * O(len of stack))
        ## Space Complexity: O(N) (if all the flights were overlapping, they'd all be in our stack)

        airplanes = sorted(airplanes, key = lambda x: x[0])
        stack = []
        for i in range(len(airplanes)):
            if (len(stack)>0):
                previous = stack[-1]
                start, end = airplanes[i]
                previous_start,previous_end = previous
                if (previous_end > start):
                    stack.append(airplanes[i])
                else:
                    ## if our current interval is not overlapping
                    ## we need to check all previous intervals in our stack to see if they're still overlapping with our current
                    ## if not, we need to pop those intervals off of the stack 
                    while (stack):
                        previous = stack[-1]
                        previous_start,previous_end = previous
                        if (previous_end > start):
                            break
                        else:
                            stack.pop()
                    stack.append(airplanes[i])
            else:
                stack.append(airplanes[i])
        return len(stack)


if __name__ == '__main__':
    s = Solution()
    airplanes = [[1,10], [4,7], [2,3], [5,8]]
    assert s.countOfAirplanes(airplanes) == 3
    airplanes2 = [[4,8], [2,5], [17,20], [10,21], [9,18]]    
    assert s.countOfAirplanes(airplanes2) == 3
    airplanes3 = [[1,2],[3,4],[5,6]]
    assert s.countOfAirplanes(airplanes3) == 1

