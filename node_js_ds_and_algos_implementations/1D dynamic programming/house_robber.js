/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    /*
    recurrence relation:
    at any given house i, the robber can rob
    i or skip i and rob i + 1
    
    using memoization:
    at each i, we want to store the max that we could've made 
    by robbing either i or skipping i and robbing i + 1
    we can reuse the results of i rather than recalculating the recursion at i
    */
    let N = nums.length
    let memo = {}
    var robHouse = function(i){
        // if at the end of the list, there's nothing to rob, so return 0
        if (i >= N){
            return 0
        }
        if (i in memo){
            return memo[i]
        }
        // if you rob i, you can't rob i + 1, so the next index must be i+2
        // skip i and rob i + 1
        memo[i] = Math.max(nums[i] + robHouse(i+2), robHouse(i+1))
        return memo[i]
        
    }
    return robHouse(0)
};