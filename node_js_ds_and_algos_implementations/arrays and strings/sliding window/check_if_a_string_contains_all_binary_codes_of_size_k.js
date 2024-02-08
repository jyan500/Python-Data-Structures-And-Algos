// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
/**
 * @param {string} s
 * @param {number} k
 * @return {boolean}
 */
var hasAllCodes = function(s, k) {
    const uniqueWays = 2**k
    let uniques = new Set()
    /* rather than brute forcing and finding all 2^k combinations of binary codes and seeing if they exist in string S,
    we can count all unique substrings of length K in our string, and see if 
    the amount of unique substrings === the amount of unique combinations of binary codes of length K
    This cuts the time complexity from exponential time to O(N*K)
    */
	// find all unique slices from i to i + k, i + k <= s.length ensures we will never
	// exceed the length of the string
    for (let i = 0; i+k <= s.length; ++i){
        uniques.add(s.slice(i, i+k))
    }
    return uniques.size === uniqueWays
};