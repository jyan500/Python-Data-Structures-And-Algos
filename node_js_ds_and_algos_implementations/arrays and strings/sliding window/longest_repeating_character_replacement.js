class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        /*
        6/12/2026
        sliding window
        we keep a hashmap of the current counts of each character in the window
        we check what the max count character is, meaning as long as we have enough k
        replacements to equal the sum of all other characters (besides the max count character),
        this is still a valid window


        AABACCAAC k = 2
        you can replace index 2 and index 4 with A since at index 4, max(character count) is 3 which
        belongs to A

        what happens when the amount of characters you want to replace exceeds k?
        use a while loop that iterates the left pointer until the amount of character is less than k

        note that if we know the max character count, all we need to do to find out all the other
        characters we need to replace is to do our current window length - max character count,
        since that would yield the total amount of replacements we need (rather than iterating
        our hashmap and summing the other numbers together)

        Time: O(N*26)
        Space: O(26)

        since there are only 26 possible uppercase letters, the input is bound by this number
        */

        let counter = new Map()
        let l = 0
        let res = 0
        for (let r = 0; r < s.length; ++r){
            counter[s[r]] = (s[r] in counter ? counter[s[r]]+1: 1)
            // find the max count
            let curMax = Math.max(...Object.values(counter))
            // we need to replace the other characters that aren't the max count
            let numReplacements = (r - l + 1) - curMax
            if (numReplacements > k){
                while (true){
                    if (r-l+1 - curMax <= k){
                        break
                    }
                    curMax = Math.max(...Object.values(counter))
                    counter[s[l]]--
                    if (counter[s[l]] === 0){
                        delete counter[s[l]]
                    }
                    ++l
                }
            }
            // after the replacements, save the window size
            res = Math.max(res, (r-l+1))
        }
        return res
    }
}

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    /*
    Sliding Window
    https://youtu.be/gqXU1UyA8pk
    Rather than keeping track of the actual string itself,
    we can store a counter where we see if we have k characters that are
    different from the rest of the characters currently, this is still "okay"
    But if we have more than that, then we don't have enough characters to do a 
    full replacement, so we need to make a decision about our sliding window.
    */
    let i = 0
    let j = 0
    let counter = {}
    let longest = 0
    for (j = 0; j < s.length; j++){
    	// store each character in the counter
        if (s[j] in counter){
            ++counter[s[j]]
        }
        else {
            counter[s[j]] = 1
        }
        /*
	        the window size is equal to the right - left + 1
	        subtracted from the amount of the most frequently occurring character
	        in our string
	        if this is > k, we need to start decreasing our sliding window
	        by shifting the left pointer, and also decreasing the count of the character
	        at the left position,
	        otherwise we can break
	    */
        while (true){
        	// note to find the max value of an array, you can use Math.max, but spread the values
        	// of the array as parameters, so [1,2,3], Math.max(...[1,2,3]) = Math.max(1,2,3)
            let frequent = Math.max(...Object.values(counter))
            let windowSize = j - i + 1 - frequent
            if (windowSize > k){
                --counter[s[i]]
                ++i
            }
            else {
                break
            }
        }
        // we do the calculation down here in case
        // we needed to do any adjustments to the window size above in the while loop, 
        longest = Math.max(longest, j - i + 1)
    }
    return longest
};