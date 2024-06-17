/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    /*
        Greedy Solution: O(N) time O(1) Space
        starting from the back of the array, we check if the current
        value at each i + current i >= goalPost, as this indicates
        that we can reach the goalPost from this position at i
        
        if we can reach the goalPost, we can shift it closer by setting it equal to i
    */
    let goalPost = nums.length-1
    for (let i = nums.length-1; i >= 0; --i){
        if (i + nums[i] >= goalPost){
            goalPost = i
        }
    }
    return goalPost === 0
};

/*
top down solution
Recurrence relation:
at each i, we want to check whether we can 
reach the end based on the value of nums[i], which is the amount
of steps we can jump

Therefore, we can loop from j ... nums[i], and perform
recursive call search(i+j+1), to indicate that we're jumping to the next index
Within the loop, if search(i+j+1) returns true, we can return true

Otherwise, we return false

Base Case:
if i === N - 1, that means that we have reached the end, so we can return true

Memoization:
At each i, we want to memoize whether we can reach the end

*/
// Time: O(N^2)
// Space: O(N) 
var canJump = function(nums) {
    let N = nums.length
    if (N <= 1){
        return true
    }
    let memo = {}
    var search = function(i){
        if (i === N-1){
            return true
        }
        if (i in memo){
            return memo[i]
        }
        for (let j = 0; j < nums[i]; j++){
            if (search(i+j+1)){
                memo[i] = true
                return true
            }
        }   
        memo[i] = false
        return memo[i]
    }
    return search(0)
}