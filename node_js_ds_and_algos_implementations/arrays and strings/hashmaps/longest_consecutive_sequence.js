class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        /*
        Revisited 9/24/2024
        the trick is realizing that in a consecutive sequence,
        the numbers must be increased or decreased by 1 only
        so given a particular number, we can check if it's value + 1 
        is present, if so this is a consecutive sequence. The start of a consecutive
        sequence would indicate that the value - 1 is not present, so it's not in the middle
        of any consecutive sequence.
        to decrease lookup times, convert nums to a set
        loop through nums,
        check to see if nums[i] - 1 exists, if so this is a start of a consecutive sequence
            use a while loop to continue checking if the next value in the sequence exists
            once this loop stops, we track the length of the sequence that we found
            also check to see if this length is greater than a max length that we've found so far

        */
        /*
        edge case where the nums array is empty, we can't assume that the smallest consecutive sequence is 1,
        so we must return 0
        */
        if (nums.length === 0){
            return 0
        }
        let lookup = new Set([...nums])
        // assumes that a single number is a consecutive sequence of length 1
        let res = 1
        for (let i = 0; i < nums.length; ++i){
            let start = nums[i] - 1
            if (lookup.has(start)){
                let total = 1
                while (lookup.has(start + 1)){
                    start++
                    total++
                }
                res = Math.max(total, res)
            }
        }
        return res
    }
}

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