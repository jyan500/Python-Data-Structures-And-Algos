/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    /*
    consecutive means either +1 or -1 away
    so at each element we can attempt to find an element +1 or -1 away from our current element,
    can optimize the lookup by storing the nums as a set
    
    If we're at an element, and we try to find an element - 1 away and it doesn't exist,
    that means this is the START of a sequence. We will then use a while loop to continuosly
    find the +1 element until we can't find it. 
    
    Then we record the length of this sequence

    O(N) Time O(N) Space
    */
    if (nums.length === 0){
        return 0
    }
    let lookup = new Set(nums)
    let cur = 1
    let longest = 1
    for (let i = 0; i < nums.length; ++i){
        let oneLess =  nums[i]-1
        // start of a sequence
        if (!lookup.has(oneLess)){
            let oneGreater = nums[i] + 1
            while (lookup.has(oneGreater)){
                ++oneGreater
                ++cur
            }
            longest = Math.max(longest, cur)
            cur = 1
        }
    }
    return longest
};