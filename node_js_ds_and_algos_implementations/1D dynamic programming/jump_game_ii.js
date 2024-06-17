/**
 * @param {number[]} nums
 * @return {number}
 */
/*
Greedy BFS/sliding window-like solution
https://www.youtube.com/watch?time_continue=217&v=dJ7sWiOoK7g&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MzY4NDIsMjM4NTE&feature=emb_title
Approach:

Based on each nums[i], we want to determine the possible places we can
reach 

for example:
2 3 1 1 4

if we start at i = 0 (2), we 
can reach either i = 1, or i = 2
which are 3 or 1

we'd then denote these choices as one "jump",
as in one jump, you can reach either 3 or 1 in this case.

From here, you'd check either i = 1 or i = 2, and then repeat the process

In this case, i = 1, you can jump either to i = 2, i = 3 or i = 4
(We don't count i = 2 here since this is part of our original jump),
we'd denote these choices as the second "jump"

because i = 4 (the goal) is in here, this would be the min amount
of jumps we can reach

*/
var jump = function(nums){
    let res = 0
    // the left and right pointers indicate the choices that can be reached by our "jump"
    // for example, at i = 0, the left and right pointers would be i = 1 and i = 2 respectively
    // this will be called the "jump" area
    let l = 0
    let r = 0
    while (r < nums.length-1){
        let farthest = 0
        // find the farthest point that we can reach based on the choices available
        // to us in the current "jump" area
        for (let i = l; i < r + 1; ++i){
            farthest = Math.max(farthest, nums[i] + i) 
        }
        // shift the sliding window to the next "jump" area which covers
        // the choices that could be made after making the furthest possible jump
        // in our current "jump" area
        l = r + 1
        r = farthest
        ++res
    }
    return res
}
/* 
Top Down Solution:
Time: O(N^2)
Space: O(N)

Similar concept to the first version of jump game,
the recurrence relation checks whether we can reach the end
of the array starting from i by looping through
j ... nums[i], and performing search(i+j+1)

The difference this time is that when we reach i === N - 1,
we return 0 to indicate that we've already reached the end of the array.

And then during backtracking, we would add 1 to the recursive call that we've finished to
indicate that it took "1" step to reach from this i to the end.

Within the loop, we also want to take the Math.min between the recursive call and the minimum
amount of jumps that we've found so far starting from i, and then return the minimum in the recursive call

Note that we initialize the minimum amount of jumps to positive infinity. This is okay because
the problem states that there will always be a way to reach the end according to the test cases,
so we don't need to make a check for it.

Memoization:
at each i, we memoize the minimum amount of steps it'd take to reach the end
*/
var jump = function(nums) {
    let N = nums.length
    let memo = {}
    var search = function(i){
        if (i === N - 1){
            return 0
        }
        if (i in memo){
            return memo[i]
        }
        let jumps = Number.POSITIVE_INFINITY
        for (let j = 0; j < nums[i]; ++j){
            jumps = Math.min(jumps, 1+search(i+j+1))
        }
        memo[i] = jumps
        return jumps
    }
    return search(0)
};