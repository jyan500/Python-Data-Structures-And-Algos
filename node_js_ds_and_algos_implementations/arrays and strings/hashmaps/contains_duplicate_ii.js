class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums, k) {
        /* 
        3/2/2026
        https://neetcode.io/problems/contains-duplicate-ii/history?list=neetcode250&submissionIndex=2
        O(N) Time
        O(N) Space
        */
        let counter = {}
        for (let i = 0; i < nums.length; ++i){
            // if we've seen the number already, subtract the indices together and
            // check whether the absolute difference <= k
            if (nums[i] in counter && Math.abs(i-counter[nums[i]]) <= k){
                return true
            }
            // if not, clear out the previous value and reset it to the current,
            // since we want two values with
            // the indices as close as possible together
            counter[nums[i]] = i
        }
        return false
    }
}
