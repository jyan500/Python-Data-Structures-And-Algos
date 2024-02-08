/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let c = {}
    for (let i = 0; i < nums.length; ++i){
        if (nums[i] in c){
            ++c[nums[i]]
        } else {
            c[nums[i]] = 1
        }
    }
    const sortKey = (a, b) => {
        if (c[a] < c[b]){
            return 1
        }
        else if (c[a] > c[b]){
            return -1
        }
        else {
            return 0
        }
    }
    // sort the keys array based on the frequencies found in our counter object
    let sortedKeys = Object.keys(c).sort(sortKey)
    return sortedKeys.slice(0, k)
    
};