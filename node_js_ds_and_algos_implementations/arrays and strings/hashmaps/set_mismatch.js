/**
 * @param {number[]} nums
 * @return {number[]}
 */
/*
https://leetcode.com/problems/set-mismatch/
Time Complexity:
O(N)
Space:
O(N)
*/
var findErrorNums = function(nums) {

    let n = nums.length
    let compare = {}
    // start with a hashmap that contains numbers 1 ... nums.length
    for (let i = 1; i <= n; ++i){
        compare[i] = 1
    }
    let res = []
    // if a number in nums is found in compare, decrement the count
    // if a number is decremented more than once, the value will be 0,
    // so save this number
    for (let i = 0; i < nums.length; ++i){
        if (nums[i] in compare) {
            compare[nums[i]]--
            if (compare[nums[i]] < 0){
                res.push(nums[i])
            }
        }
    }
    // after decrementing the count of each, if there's a still a number
    // in the compare that's equal to 1, that means it was not found within the nums list,
    // so save this number
    for (let key in compare){
        if (compare[key] === 1){
            res.push(key)
            break
        }
    }
    return res
    
};