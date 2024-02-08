/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let prefix = nums.map(x=>x)
    let suffix = nums.map(x=>x)
    let res = nums.map(x=>x)
    /*
    prefix = [1, 2, 6, 24]
    suffix = [24,24,12, 4]
    because the prefix and suffix contain the cumulative products up to index i,
    the product of everything except i is one element to the left of i in prefix,
    and one element to the right of i within suffix
    
    i = 0
    1 * suffix[1]
    
    i = 1
    prefix[0] * suffix[2]
    1 * 12 = 12
    
    i = 2
    prefix[1] * suffix[3]
    2 * 4 = 8
    */
    for (let i = 1; i < nums.length; ++i){
        prefix[i] = prefix[i-1] * prefix[i]
    }
    for (let i = nums.length - 2; i >= 0; --i){
        suffix[i] = suffix[i+1] * suffix[i]
    }
    for (let i = 0; i < res.length; ++i){
        if (i === 0){
            res[i] = suffix[i+1]
        }
        else if (i === res.length - 1){
            res[i] = prefix[i-1]
        }
        else {
            res[i] = prefix[i-1] * suffix[i+1]
        }
    }
    return res
    
};