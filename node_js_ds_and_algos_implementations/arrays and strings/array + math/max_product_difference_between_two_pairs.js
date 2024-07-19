/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    /*
    to get the max product difference,
    we want the first pair to have the biggest product as possible,
    and the second pair to have the smallest product as possible
    
    can sort the numbers first
    and pick the biggest two and the smallest two numbers,
    and then calculate the products and the differences
    */
    var sortKey = (a, b) => {
        if (a < b){
            return -1
        }
        else if (a > b){
            return 1
        }
        return 0
    }
    nums.sort(sortKey)
    return (nums[nums.length-1] * nums[nums.length-2]) - (nums[0] * nums[1])
};