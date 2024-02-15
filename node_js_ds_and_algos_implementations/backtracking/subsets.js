/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    /*
    https://leetcode.com/problems/subsets/submissions/
    knapsack relation
    1) increment i and include nums[i]
    2) increment i but don't include nums[i]
    */
    let res = []
    const search = (i, cur) => {
        // base case
        // if i has reached the end, there's no more subsets that can be returned,
        // so just return empty array
        if (i >= nums.length){
            res.push(cur)
            return
        }
        search(i+1, cur.concat(nums[i]))
        search(i+1, cur)
    }
    search(0, [])
    return res
};