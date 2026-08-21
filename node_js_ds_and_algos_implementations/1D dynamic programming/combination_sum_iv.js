class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    combinationSum4(nums, target) {
        /* 
        you can use a number as many times as needed, and needs to use previous indices,
        needs a for loop 

        3,1,2 target = 4

        finds 3,1 (3 doesn't work, 3,2 doesn't work)
        finds 1,3 
        finds 1,1,1,1 (1,1,1,3 doesn't work, 1,1,1,2 doesn't work)
        
        */
        const N = nums.length
        // memoize on current, where if the current sum is a certain amount, we already
        // know the amount of ways to reach the target
        let memo = {}
        const search = (current) => {
            if (current === target){
                return 1
            }
            if (current > target){
                return 0
            }
            if (current in memo){
                return memo[current]
            }
            let res = 0
            // continue using the same element
            // note that this loop alone would find repeated subcases over and over,
            // which is why memoizing the current sum is important
            for (let i = 0; i < nums.length; ++i){
                res += search(current + nums[i])
            }
            memo[current] = res
            return res
        }
        return search(0)
    }
}
