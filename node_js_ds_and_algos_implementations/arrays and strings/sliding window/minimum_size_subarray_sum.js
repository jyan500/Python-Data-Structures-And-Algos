class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target, nums) {
        /* 
        sliding window
        if the sum of the window exceeds the target, shrink the window from the left
        side until the sum is under the target
        */
        let l = 0
        let currentSum = 0 
        let minLength = Number.POSITIVE_INFINITY
        for (let r = 0; r < nums.length; ++r){
            currentSum += nums[r]
            while (currentSum >= target){
                minLength = Math.min(r - l + 1, minLength)
                currentSum -= nums[l]
                ++l
            }
  
        }
        return minLength !== Number.POSITIVE_INFINITY ? minLength : 0
    }
}
