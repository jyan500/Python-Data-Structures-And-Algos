"""
https://leetcode.com/problems/combinations/
Key Concepts:
1) The goal in the recursion is to pass in a smaller chunk of the list each time,
where we "pick" the first item in our list, and then in a for loop, we make a recursive call
to pass in a version of the list that's everything after the item we picked, and then 
append the "picked" item to our current result. 
2) Once the current result has reached the length K, we then append it to our global result

Example:
n = 4, k = 2
[1, 2, 3, 4]

1st recursive call
loop variable i = 0
Picks 1
Passes in build([2, 3, 4], [1])

2nd recursive call
loop variable i = 0
Picks 2
Passes in build([3, 4], [1, 2])

3rd recursive call
This time, cur is now length of 2, so we can append 
[1, 2] to our global result and return

Back to 2nd recursive call
loop variable is now at i = 1
Picks 3
Passes in build([4], [1, 3])

4th call
cur is now length 2, 
appends [1, 3] to global result and returns

Back to 2nd recursive call
loop variable is now at i = 2
Picks 4
Passes in build([], [1, 4])

5th call
cur is now length 2,
appends [1, 4] to global result and returns

Back to 2nd recursive call, the loop is now finished

Back to 1st recursive call (when we picked 1), 
now i = 1
Picks 2
Passes in build([3, 4], [2])

... we now build the list with 2 as the starting number,
and then the process repeats with 3 as the starting number and so on 

the final result is [1,2], [1,3], [1,4], [2,3], [2,4], [3,4]

Time Complexity: O(k*N^k), the upper bound of the first "pick" which technically has the most combinations,
K is the amount of combinations that we end up with
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        def build(l, cur):
            if len(cur) == k:
                self.result.append(cur)
                return
            for i in range(len(l)):
                build(l[i+1:], cur + [l[i]])
                
    
        build([i+1 for i in range(n)], [])
            
        return self.result