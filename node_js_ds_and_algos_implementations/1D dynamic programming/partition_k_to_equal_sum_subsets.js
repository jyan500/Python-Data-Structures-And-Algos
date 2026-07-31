class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    canPartitionKSubsets(nums, k) {
        // Time complexity: O(k*2^N)
        // Space: O(N)

        // if the total sum is not divisible by k, that means there is no possible answer
        let totalSum = nums.reduce((acc,num) => acc + num, 0)
        if (totalSum % k !== 0){
            return false
        }
        let subSum = totalSum / k
        const used = new Array(nums.length).fill(false)
        nums.sort((a,b) => a-b)
        const search = (startIndex, currentSum, countCompleted) => {
            // if the number of subsets with sum === subSum is now equal to k, 
            // this is valid
            if (countCompleted === k){
                return true
            }
            // if currentSum === subSum, start building the next subset by resetting
            // the indices to 0 and current sum to 0
            if (currentSum === subSum){
                return search(0, 0, countCompleted + 1)
            }
            
            // otherwise, try each unused number from startIndex onward,
            // check if adding it would overflow subSum,
            // mark it used, recurse, return true if the recursive result is true,
            // otherwise, unmark so it can be reused by a different recursive path
            for (let i = startIndex; i < nums.length; ++i){
                if (currentSum + nums[i] <= subSum && !used[i]){
                    used[i] = true
                    // if we found a combination, return true
                    if (search(i+1, currentSum + nums[i], countCompleted)){
                        return true
                    }
                    used[i] = false
                }
            }
            return false
        }
        return search(0, 0, 0)
    }
