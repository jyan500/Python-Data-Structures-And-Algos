/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    /*
    The trick to solving this problem is recognizing that
    because the houses are arranged in a circle,
    if the first house is robbed, the last house cannot be robbed.
    vice versa, if the last house is robbed, the first house cannot be robbed.

    We can then split into two cases, where we run the original house robber
    algorithm on houses 1 ... N - 1 AND 0 to N - 2
    (i.e 2nd house to last, first house to second to last house) 
    */
    let N = nums.length
    if (N === 1){
        return nums[0]
    }
    let memo = {}
    var robHouse = function(i, end){
        if (i >= end){
            return 0
        }
        else if (i in memo){
            return memo[i]
        }
        memo[i] = Math.max(nums[i] + robHouse(i+2, end), robHouse(i+1, end))
        return memo[i]
    }
    let allExceptFirst = robHouse(1, N)
    memo = {}
    let allExceptLast = robHouse(0, N-1)
    return Math.max(allExceptFirst, allExceptLast)
};