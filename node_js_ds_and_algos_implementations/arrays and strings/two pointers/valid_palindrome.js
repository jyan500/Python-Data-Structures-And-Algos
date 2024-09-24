class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    /*
    Revisited 9/24/2024
    https://neetcode.io/problems/is-palindrome
    O(N) Time O(1) Space solution
    This variation of the problem on neetcode indicates that 
    the string can include non-alphanumeric characters such as special chars and spaces,
    and that a palindrome is not case sensitive.
    this creates an extra challenge to the original problem as non-alphanumeric characters need
    to be tested for and ignored, and case must also be ignored. The goal is that you're only comparing
    alphanumeric characters with each other, so if one character is alphanumeric but the other is not, you only shift
    the side that's not alphanumeric. but if both characters are Non-alphanumeric, you also shift both
    pointers

    The approach is similar, two pointers, one from the left and one from the right.
    while left <= right, (in the case the total length is odd)

    However, now we have t check to see if left and right side characters
    are actually alphanumeric or not using regex, using (/[a-zA-Z0-9]/).test(your string)
    if both sides are alphanumeric:
        if both sides when converted to lower case are NOT equal:
            this is not a palindrome
        else
            increment left
            decrement right
    else if left side is alphanumeric and the right side is not:
        decrement only the right side
    else if left side is not alphanumeric and the right side is:
        increment only the left side 
    else (if neither side is alphanumeric):
        increment left
        decrement right
    */
    isPalindrome(s) {
        let l = 0 
        let r = s.length - 1
        while (l <= r){
            let isLeftSideChar = (/[a-zA-Z0-9]/).test(s[l])
            let isRightSideChar = (/[a-zA-Z0-9]/).test(s[r])
            if (isLeftSideChar && isRightSideChar){
                if (s[l].toLowerCase() !== s[r].toLowerCase()){
                    return false
                }
                l++
                r--
            }
            else if (isLeftSideChar && !isRightSideChar){
                r--
            }
            else if (!isLeftSideChar && isRightSideChar){
                ++l
            }
            else {
                l++
                r--
            }
        }
        return true
    }
}

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
	/* O(N) Time O(N) Space */
    let parsed = []
    // uses some extra memory to simplify the pointer logic
    // remove any non alpha numeric characters,
    // and make sure that alpha numeric characters are lowercase
    for (let i = 0; i < s.length; ++i){
        if ((/[0-9a-zA-Z]/).test(s[i])){
            parsed.push(s[i].toLowerCase())
        }
    }
    let i = 0
    let j = parsed.length-1
    while(i < j){
        if (parsed[i] !== parsed[j]){
            return false
        }
        i++
        j--
    }
    return true
};