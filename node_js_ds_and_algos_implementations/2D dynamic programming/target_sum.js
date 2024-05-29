/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
/*
Time Complexity: O(N * T), where N is the len of nums and t is the target. 
The recursion with memoization simulates a nested for loop, where you need to start from each i
and iterate through i + 1, i + 2, ... until i = N - 1 because you need to check two possibilities,
whether you add at i or subtract at i, and then each will have their own separate path. 

The memoization prevents redundant paths where you've already calculated whether 
at a given i, how many ways can be generated to reach the target.

Space: O(N * T), for the memoization object

Example:
nums = 1 0 target = 1

i = 0, cur = 0
add 1, or subtract 1
adds 1

i = 1, cur = 1
add 0, or subtract 0
adds 0

target reached, returns 1

backtracks to
i = 1, cur = 1
ways1 = 1
subtracts 0 this time

target reached, returns 1

backtracks to i = 1, cur = 1
ways1 = 1
ways2 = 1
returns 1 + 1 = 2

backtracks to i = 0, cur = 0 
subtract 1

i = 1, cur = -1
here, no matter which way you add or subtract 0, it doesn't reach the target,
so returns 0

i = 0 cur = 0
ways1 = 2
ways2 = 0
returns 2

*/
var findTargetSumWays = function(nums, target) {
    /*
    must use each number in nums
    can either +/- for a given number
    */
    let N = nums.length
    let memo = {}
    let search = function(i, cur){
        // if we were able to decrease to exactly 0 at the end,
        // this is a valid combination, return 1
        if (i >= N){
            return cur === target ? 1 : 0
        }
        if (`${i},${cur}` in memo){
            return memo[`${i},${cur}`] 
        }
        // you can either add the current number, or subtract
        // the current number
        let ways1 = search(i+1, cur - nums[i])
        let ways2 = search(i+1, cur + nums[i])
        memo[`${i},${cur}`] = ways1 + ways2
        return ways1 + ways2
    }
    return search(0, 0)
};