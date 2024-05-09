/**
 * @param {string} s
 * @return {number}
 */
/* 
Top Down Memoization Approach:
1) Start by creating the encoding dictionary, mapping
the letter's index + 1 to the letter
i.e {1: A, 2: B, ..., 26: Z}
2) The recurrence relation is that at any given i we can either
    a) If s[i] can be encoded, encode s[i] and then move onto i + 1
    b) If s[i] and s[i+1] can be encoded, encode s[i] + s[i+1], and move onto i + 2

   The base case is reached when i >= N, which means we've reached the end of the string
   the only way we could've reached this is IF we've done a valid decoding of all the strings preceding this,
   in that case, we return 1 to indicate that this is a valid way to decode.

3) The memoization aspect is that at a given i:
    save how many ways we could've decoded strings starting from i, and then return memo[i]

Something that can be taken away from this problem is that its only asking for the 
AMOUNT of ways it can be decoded, so no need to use a set to store results. At each i,
we just need to check whether we CAN decode or not, if so, we move on with the recursion.
Since if we can't decode, the amt will be 0 and that will be returned.

Time Complexity: O(N) (with memoization)
Space: O(N) recursive stack and the memoization dict
*/
var numDecodings = function(s) {
    let letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let encodings = {}
    for (let i = 0; i < letters.length; ++i){
        encodings[(i+1).toString()] = letters[i]
    }
    let N = s.length
    let memo = {}
    var decode = function(i){
        if (i >= N){
            return 1
        }
        if (i in memo){
            return memo[i]
        }
        let amt = 0
        if (s[i] in encodings){
            amt += decode(i+1)
        }
        let pair = s.slice(i, i+2)
        if (i+2 <= N && pair in encodings){
            amt += decode(i+2)
        }
        memo[i] = amt
        return memo[i]
    }
    return decode(0)
};