/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let unique = new Set()
    for (let i = 0; i < nums.length; ++i){
        unique.add(nums[i])
    }
    return unique.size !== nums.length
};