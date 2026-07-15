class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canPartition(nums) {
        /* 
            Backtracking:
            If the sum of the array elements is not an even number,
            can immediately return false, because it's not possible to split
            into two subsets
            for example:
            [1,2], we cannot split [1], [2], or [1,2]

            Framing the problem as:
            try to build a subset with half of the sum, so that the remaining subset is possible,
            we don't necessarily care about what the values of the remaining subset are, just that
            it's possible.

            The entire array can be considered as one subset, with the other as empty

            knapsack:
            include the current element in the subset or not? Keep track of the subset sum
            rather than the actual elements themselves
        */
        let totalSum = nums.reduce((acc,obj) => acc + obj, 0)
        let isDivisible = totalSum % 2
        if (isDivisible !== 0){
            return false
        }
        // if we can find a subset that sums to the total sum / 2,
        // that means that the other subset is possible
        let total = totalSum / 2
        const search = (i, curSum) => {
            if (i === nums.length){
                return false
            }
            if (curSum === total){
                return true
            }
            let include = false
            if (curSum + nums[i] <= total){
                include = search(i+1, curSum + nums[i])
            }
            // if either path results in finding the target, return true
            return include || search(i+1, curSum)
        }
        return search(0,0)
    }
}
