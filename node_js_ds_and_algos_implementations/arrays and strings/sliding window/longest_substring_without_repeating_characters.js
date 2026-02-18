class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        /*
        Revisited 2/18/2026
        O(N) Time
        O(N) Space
        sliding window
        we expand the window, keeping track of counts of each character in a hashmap until we find a duplicate
        character
        we decrement the left side of the window until there are no duplicate characters left, and then continue
        expanding the right side 
        */
        let counter = {}
        let l = 0
        let res = 0
        for (let r = 0; r < s.length; ++r){
            if (!(s[r] in counter)){
                counter[s[r]] = 1
            }
            else {
                counter[s[r]] += 1
            }
            while (counter[s[r]] > 1){
                counter[s[l]] -= 1
                l += 1
            }
            res = Math.max(res, r - l + 1)
        }
        return res
    }
}


/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let counter = {}
    let i = 0
    let j = 0
    let max = 0
    let cur = 0
    while (j < s.length){
        // we we found a character earlier in the string
        // that has the same value, we need to shift the left pointer
        // all the way to this character, and that add one to avoid
        // having the repeated character
        if (s[j] in counter){
            i = counter[s[j]] + 1
            // go back into the counter and remove any characters
            // with index value less than the index of the previous occurence of the repeated character at j 
            let keys = Object.keys(counter).filter((key) => counter[key] <= counter[s[j]])
            for (let k of keys){
                delete counter[k]
                --cur
            }
            // increment i and cur to the next character after we removed the previous repeating character,
            // and then add the current character back to the counter
            /* 
            for example:
            d v d f g, i = 0, j = 0
            say we're at j = 2, where d is found, and d is already in the counter...
            cur would be 3 at this point, cur would be 2
            we remove the character at index 0 in our counter, which would leave us with {v: 1},
            and a cur of 1, and index i of 1 as well (since we skip 0 as we deleted it)
            we then add the current value at j = 2 back to our counter
            {v: 1, d: 2}, and increment cur to 2
            */ 
            counter[s[j]] = j
            ++cur
        }
        else {
            counter[s[j]] = j
            ++cur
            max = Math.max(max, cur)
        }
        ++j
        
    }
    return max
};