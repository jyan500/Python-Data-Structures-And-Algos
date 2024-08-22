/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    /*
    Note for this problem, Neetcode suggests a bit mask solution, but I think this solution is much easier to follow,
    even though it is less efficient:

    https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/discuss/5194916/Python-DP-slow-but-easy-to-understand
    recursive solution:
    
    at each i, we have three choices
    add to the first subsequence
    add to the second subsequence
    skip it
    
    By doing this, we ensure that the two subsequences remain disjoint
    and don't pick the same indices
    
    base case:
    if i has reached the end of the string s,
    you should be left with two disjoint subsequences
    
    if isValidPalindrome(subsequence1) && isValidPalindrome(subsequence2)
       return subsequence1.length * subsequence2.length
      
    You would want to take the max between the three choices and return for each recursive call

    Time Complexity: O(3^N), since there are three different choices we have at each i
    Space: O(N)
    */
    var isValidPalindrome = function(s){
        let i = 0
        let j = s.length-1
        while (i <= j){
            if (s[i] !== s[j]){
                return false
            }
            ++i
            --j
        }
        return true
    }
    var search = function(first, second, i){
        if (i === s.length){
            // if valid palindrome, return the product of the lengths
            if (isValidPalindrome(first) && isValidPalindrome(second)){
                return first.length*second.length    
            }
            // otherwise, return NEGATIVE_INFINITY to show that this recursive path
            // did not generate a valid answer, so if performing Math.max(), it would
            // automatically take any number greater than negative infinity
            return Number.NEGATIVE_INFINITY
        }
        let addToFirst = search(first + s[i], second, i + 1)
        let addToSecond = search(first, second + s[i], i + 1)
        let skip = search(first, second, i + 1)
        return Math.max(addToFirst, addToSecond, skip)
    }
    return search("", "", 0)
};