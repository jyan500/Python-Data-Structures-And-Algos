/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// because JS doesn't have built-in integer division operator, use Math.floor() instead
var search = function(nums, target) {
    const helper = (l, r, target) => {
        let mid = l + Math.floor((r-l)/2)
        if (nums[mid] === target){
            return mid
        }
        else if (l > r){
            return -1
        }
        else if (nums[mid] < target){
            return helper(mid+1, r, target)
        }
        else if (nums[mid] > target){
            return helper(l, mid-1, target)
        }
        
    }
    return helper(0, nums.length-1,target)
};