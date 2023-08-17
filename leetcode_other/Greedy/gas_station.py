"""
https://www.youtube.com/watch?v=lJwbPZGo05A&ab_channel=NeetCode
https://leetcode.com/problems/gas-station/discuss/3011271/Python-3-oror-2-6-lines-w-explanation-and-example-oror-TM%3A-99-98
https://leetcode.com/problems/gas-station/discuss/1706142/JavaC%2B%2BPython-An-explanation-that-ever-EXISTS-till-now!!!!

Time: O(N)
Space: O(1)

Key Concepts (Greedy Approach):
1) It's only possible to complete the circuit if the total amount of gas on the circuit is sufficient
enough to drive the circuit (i.e sum(gas) >= sum(cost))
2) The starting position can be determined by starting at some station A, and noting whether
a station B on the circuit is unreachable due to lack of gas. If all are reachable,
then A is our answer. If not, our answer is not A, nor any station between between A and B
    -Say if A can't make it, A+1 ... A+2 ... to B cannot make it either, because for A+1, A+2...,
    they all had to go through A first, so if A can't make it, these can't either

3) Reset the tank to zero and repeat on the remainder of gas 
4) The last station that is unreachable in this process (i.e station Z) is our answer

Example:
Gas = [1,2,3,4,5]
Cost= [3,4,5,1,2]

sum(gas) = 15
sum(cost) = 15

There must be at least one answer because 15 >= 15

total = 0
res = 0

1st iteration
total += gas[0] - cost[0] = 1 - 3 = -2
total < 0

reset total = 0, res = 0 + 1

total = 0
res = 1

2nd iteration
total += gas[1] - cost[1] = 2 - 4 = -2
total < 0

reset total = 0, res = 1 + 1 = 2

total = 0
res = 2

3rd iteration
total += gas[2] - cost[2] = 3 - 5 = -2
total < 0

reset total, res = 2 + 1 = 3

4th iteration
total += gas[3] - cost[3] = 3
total > 0,

total = 3

5th iteration

total += gas[4] - cost[4] = 3 += 3 = 6

total = 6

Therefore, res is still equal to 3 which is the answer

Another example:
Gas = [1,2,3,4,5,4,1,1,1]
Cost= [3,4,5,1,2,1,2,10,8]

if running through this similar example above,
the total becomes non zero at i = 3, however,
the total dips back down below zero at i = 7, where the cost was 10

This is why we can't just return the 1st instance of the total
becoming non-zero, we need to run through the rest of the array, 
because at i = 8, the total becomes non-zero again,
making i = 8 our answer

"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res
        