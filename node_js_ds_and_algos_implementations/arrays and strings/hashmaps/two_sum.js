/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let counter = {}
    for (let i = 0; i < nums.length; ++i){
        let diff = target - nums[i]
        if (diff in counter){
            return [i, counter[diff]]
        }
        else{
            counter[nums[i]] = i
        }
    }
};