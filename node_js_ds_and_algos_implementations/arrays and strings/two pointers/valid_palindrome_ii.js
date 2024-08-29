/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    /*
    Approach:
    Two pointers, left = 0, right = end of s
    move the two pointers inwards until the values are not equal, break at this point

    Copy the left and right pointers in this state, try incrementing the left once using the copied pointer
    to pass over the left character

    Continue the palindrome check using the new pointers. 
        If the characters are not the same, set a flag to false and break

    This time, copy the original left and right pointers, try decrementing the right once to pass
    over the right character

    continue palindrome check using the new pointers
        if characters not the same, set flag to false and break

    Return flag1 or flag2, if you could delete at least one of the sides and the rest of the string is a palindrome,
    this would return true
    
    Time: O(N)
    Space: O(1)

    */
    let l = 0
    let r = s.length - 1
    while (l <= r){
        if (s[l] !== s[r]){
            break
        }
        l++
        r--
    }
    // pass over the left character, and then try to compare again
    let l1 = l
    let r1 = r
    l1++
    let flag1 = true
    while (l1 <= r1){
        if (s[l1] !== s[r1]){
            flag1 = false
            break
        }
        l1++
        r1--
    }
    // pass over the right character, and then try to compare again
    let l2 = l
    let r2 = r
    r2--
    let flag2 = true
    while (l2 <= r2){
        if (s[l2] !== s[r2]){
            flag2 = false
            break
        }
        l2++
        r2--
    }
    return flag1 || flag2
    
};