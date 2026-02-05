/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    /* 
    Revisited 2/5/2026 (JS solution)
    Kadane's Algorithm 
    (similar to best time to buy or sell stock question)
    1) track the current sum, and the max sum as two variables
    2) Iterate through nums, adding nums[i] to current sum
    However, if we notice that the current nums[i] is greater than the cumulative sum, it would be better
    to just start the cumulative sum AT nums[i], since
    that would result in a greater cumulative sum overall.
    
    For example:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    If we added nums[0], nums[1], nums[2], nums[3],
    we'd get 0
    however nums[3] (which is 4), is greater than 0,
    so it'd be better for the cumulative sum to be value of nums[3] (4), since the previous numbers are bringing the value of the cumulative sum down.
    
    3) At each point iteration i, we also check to see
    if the current sum is greater than the max sum
    */
    let sum = 0;
    let maxSum = Number.NEGATIVE_INFINITY
    for (let i = 0; i < nums.length; ++i){
        sum += nums[i]
        if (nums[i] > sum){
            sum = nums[i]
        }
        maxSum = Math.max(sum, maxSum)
    }
    return maxSum
};