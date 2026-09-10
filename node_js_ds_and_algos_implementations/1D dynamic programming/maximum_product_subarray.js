class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        /* 
        9/10/2026
        Samuel Yu's solution:
        https://neetcode.io/problems/maximum-product-subarray/discuss/qrPlODVjWMumaBKFkVIf

        Two pass by getting the running product from left to right and finding the max
        so far, resetting whenever we get nums[i] = 0 to avoid making the rest of the 
        product 0
        and then comparing it to the running product from right to left

        Reason for comparing both:
        If there are an odd count of negative numbers, this ensures that we handle the case
        when we multiply two negatives and it becomes positive
        for example:
        [1,-2,-3,-4]
        1 * -2 = -2, -2 * -3 = 6, 6 * -4 = -24
        whereas
        -4 * -3 = 12, 12 * -2 = -24, -24 * 1 = -24

        You can see from left to right, the max product is 6
        but from right to left, the max product is actually 12

        Example edge case with 0
        [1,2,0,4] 
        1 * 2 = 2
        2 * 0 = 0, but instead of resetting to 0, we reset to 1,
        otherwise, every remaining product will also be 0
        1 * 4 = 4, so we get a max product of 4
        */

        let res = nums[0]
        let prod = 1
        for (let i = 0; i < nums.length; ++i){
            prod = prod * nums[i]
            // catch edge case in JS where if you multiply a negative number with 0,
            // you get -0, so you need to turn it back to 0
            if (prod === -0){
                prod = 0 
            }
            res = Math.max(res, prod)
            if (nums[i] === 0){
                prod = 1   
            }
        }
        prod = 1
        for (let i = nums.length - 1; i >= 0; --i){
            prod = prod * nums[i]
            if (prod === -0){
                prod = 0 
            }
            res = Math.max(res, prod)
            if (nums[i] === 0){
                prod = 1
            }
        }
        return res
    }
}

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