class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @returns {number[][]}
     */
    combinationSum(nums, target) {
        /* 
        Revisited 9/30/2026
        Time complexity is roughly 2^N
        can actually save both time and memory by pushing and popping off the "cur" array once
        we're doing exploring, so that we undo the previous recursive state and can explore another path without that side effect
        of the array push from the previous state
        and then when copying into the combinations, we just slice the "cur" to create a copy of it
        */
        let combinations = []
        let N = nums.length
        const search = (i, cur, curSum) => {
            if (curSum === target || i === N){
                if (curSum === target){
                    combinations.push([...cur])
                }
                return
            }
            if (curSum + nums[i] <= target){
                cur.push(nums[i])
                search(i, cur, curSum + nums[i])
                cur.pop()
            }
            search(i+1, cur, curSum)
        }
        search(0, [], 0)
        return combinations
    }
}

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let res = []
    var search = function(candidates, target, index, cur){
        if (target <= 0){
            if (target === 0){
                res.push(cur)
            }
            // if the target is below 0, we cannot add any more numbers
            return 
        }
        if (index < candidates.length){
            // knapsack relation, we include the element at the current index
            // and do target - current element, until target === 0 || target <= 0, then
            // we pick the next index.
            // at each point, we can only include the element at index, or potentially elements after it,
            // so we only get unique combinations this way, since we don't backtrack and use previous elements
            // we also spread a new array with the element in it to avoid side effects between each recursive call,
            // so once the recursion backtracks, it will be the original array without the current element added
            search(candidates, target - candidates[index], index, [...cur, candidates[index]])
            search(candidates, target, index + 1, cur)
        }
    }
    search(candidates, target, 0, [])
    return res
};