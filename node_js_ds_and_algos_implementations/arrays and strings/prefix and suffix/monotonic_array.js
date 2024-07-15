/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function(nums) {
    /*
    two pass solution
    1st pass, check to see if the previous element in the array <= than the current element
    2nd pass, check to see if the previous element in the array >= than the current element
    */
    let increasing = true
    for (let i = 1; i < nums.length; ++i){
        if (nums[i-1] <= nums[i]){
            increasing = true
        }
        else {
            increasing = false
            break
        }
    }
    let decreasing = true
    for (let i = 1; i < nums.length; ++i){
        if (nums[i-1] >= nums[i]){
            decreasing = true
        }
        else {
            decreasing = false
            break
        }
    }
    return increasing || decreasing
};