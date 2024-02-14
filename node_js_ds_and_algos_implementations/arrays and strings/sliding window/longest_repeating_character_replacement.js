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