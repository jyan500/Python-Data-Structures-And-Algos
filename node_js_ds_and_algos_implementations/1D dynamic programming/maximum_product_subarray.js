/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    /*
    Prefix and Suffix Multiplication
    1) get the prefix multiplication by taking the cumulative product from front to back. Each cumuluative
    product represents the subarray's product up to that point
    2) get the suffix multiplication by taking the cumulative product from back to front. Each cumulative
    product represents the subarray's product up to that point
    3) Comparing the prefix (starting from front) and suffix (starting from back), take the max between each,
    as this will get the max product that is possible between the two subarrays.

    There's an edge case where the subarray's product becomes 0 (when calculating either prefix or suffix),
    to handle this you need to "reset" the subarray to be equal to just the number itself.

    Time: O(N)
    Space: O(N)

    It's possible to optimize the space by not tracking the prefix and suffix and just storing the products
    directly as a variable. See the python solution (maximum_product_subarrays.py)
    */
    let prefix = [...nums]
    let suffix = [...nums]
    for (let i = 1; i < nums.length; ++i){
        if (prefix[i-1] === 0){
            prefix[i] = nums[i]
        }
        else {
            prefix[i] = nums[i] * prefix[i-1]
        }
    }
    for (let i = nums.length-2; i >= 0; --i){
        if (suffix[i+1] === 0){
            suffix[i] = nums[i]

        }
        else{
            suffix[i] = nums[i] * suffix[i+1]
        }
    }
    let max = Number.NEGATIVE_INFINITY
    for (let i = 0; i < nums.length; ++i){
        j = nums.length - 1 - i
        max = Math.max(max, Math.max(prefix[i], suffix[j]))
    }
    return max
    
};