/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    /* 
    count the amount of 0's, 1's and 2's
    overwrite the original array nums 
    starting at i = 0 with the amount of 0's, 1's, 2's
    O(N) Time, O(N) Space
    */
    let map = {0: 0, 1:0, 2:0}
    for (let i = 0; i < nums.length; ++i){
        map[nums[i]]++
    }
    let i = 0
    for (let key in map){
        for (let k = 0; k < map[key]; ++k){
            nums[i] = key
            ++i
        }
    }
};