/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let counter = {}
    for (let i = 0; i < nums.length; ++i){
        let diff = target - nums[i]
        // if the target - nums[i] is in counter, that means 
        // that target - nums[i] + nums[i] would be the target, so this would be a valid pair
        // return the indices of those two numbers 
        // note that you have to check this case before you store nums[i], otherwise you might end up in an edge case like
        // [3, 2, 4], target = 6, if you store 3 with index 0 in the counter, and THEN check if target - 3 is present,
        // 6- 3 = 3, which IS present, so you end up with [0, 0] which is incorrect
        if (diff in counter){
            return [i, counter[diff]]
        }
        else{
            counter[nums[i]] = i
        }
    }
};