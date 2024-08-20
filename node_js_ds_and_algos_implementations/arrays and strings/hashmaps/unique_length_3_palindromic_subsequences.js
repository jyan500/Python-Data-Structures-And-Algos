/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    /*
    Most efficient solution
    O(26 * N) time
    O(N) space
    Similar to the better solution below,
    but rather than repeatedly iterating through left and right, we can track characters that we've already seen
    using a hashmap
    Use a hashmap that represents the counts of all characters on the right of the current index
    Use a set that represents all characters that were formerly on the right, but are now on the "left", indicating
    that we've seen it
    Use another set to check for duplicate palindromes
    Neetcode: https://youtu.be/3THUt0vAFLU
    
    Example:
    s = "bbcbaba", answer should be 4
    
    set = {}
    left = {}
    right = {b: 4, a:2, c:1}
    
    1st iteration i = 0
    -----------------------
    s[0] is b
    right[b]-- (right[b] is now 3)
    
    because we're still at i = 0, we can't find a character to the left that matches a character on the right,
    since left is still empty
    
    add b to left 
    
    set = {}
    left = {b}
    right = {b: 3, a:2, c:1}
    
    2nd iteration i = 1
    -----------------------
    s[1] = b
    right[b]-- (right[b] is now 2)
    
    searching on both the left and right for the same letter, you can see that b exists
    on both the left and right, forming "bbb". Add "bbb" to the set. No other characters exists on both sides
    
    add b to left (b already exists in the set so it's not added)
    
    set = {bbb}
    left = {b}
    right = {b: 2, a:2, c:1}
    
    3rd iteration i = 2
    -----------------------
    s[2] = c
    right[c]-- (right[c] is now 0, so remove c as a key)
    
    searching on both the left and right for the same letter, you can see that b exists on both sides
    forming the palindrome "bcb", add to set. No other character exists on both sides
    
    add c to left
    
    set = {bbb, bcb}
    left = {b, c}
    right = {b: 2, a:2}
    
    4th iteration i = 3
    -----------------------
    s[3] = b
    right[b]-- (right[b] is now 1)
    
    we can see that b exists on the left and right, but we've already added bbb to our set so ignore it
    no other character exists on both sides
    
    add b to left (b is already added so ignore)
    
    set = {bbb, bcb}
    left = {b, c}
    right = {b: 1, a: 2}
    
    5th iteration i = 4
    ----------------------------
    s[4] = a
    right[a]-- (right[a] is now 1)
    
    we can see that b exists on the left and right, forming the palindrome bab, add to our set
    
    add a to left 
    
    set = {bbb, bcb, bab}
    left = {b, c, a}
    right = {b: 1, a: 1}
    
    6th iteration i = 5
    --------------------------------
    s[5] = b
    right[b]-- (right[b] is now 0, remove this key)
    
    we can see that b exists on the left and right, a exists on the left and right.
    we've added bab but not aba, so add aba
    
    add b to left (already been added, so ignore)
    
    set = {bbb, bcb, bab, aba}
    left = {b, c, a}
    right = {a: 1}
    
    7th iteration i = 6
    --------------------------
    s[6] = a
    right[a]-- (right[a] is now 0, remove this key)
    there's nothing on the right side that exists on the left since the right side is now empty
    
    adds a to the left (already been added, so ignore)
    
    ------------------------------------
    At the end, there's four unique palindromes in the set, so return 4
    
    */
    let set = new Set()
    let left = new Set()
    let right = {}
    for (let char of s){
        if (char in right){
            ++right[char]
        }
        else {
            right[char] = 1
        }
    }
    let letters = "abcdefghijklmnopqrstuvwxyz"
    for (let i = 0; i < s.length; ++i){
        --right[s[i]]
        if (right[s[i]] === 0){
            delete right[s[i]]
        }
        for (let letter of letters){
            if (left.has(letter) && letter in right){
                set.add(letter + s[i] + letter)
            }
        }
        left.add(s[i])
    }
    return set.size
    /*
    Better solution:
    O(26 * N^2) solution
    Key observation:
    For length 3 palindromes, the middle character can be any character from a to z, while the two surrounding 
    characters always have to be the same.
    
        We still keep a set to check for duplicate palindromes
        z a a b c a b z
        
        at each index, this would be the "middle" of the palindrome
        then we can slice everything from 0 to i (left side) and i + 1 to s.length (right side),
        then loop through all letters a to z to check if the letter exists in both the left and right side.
        Also check if the palindrome (letter + s[i] + letter) already exists in our set
    */
    /*
    if (s.length < 3){
        return 0
    }
    let counter = 0
    let set = new Set()
    let letters = "abcdefghijklmnopqrstuvwxyz"
    for (let i = 1; i < s.length-1; ++i){
        let left = s.slice(0, i)
        let right = s.slice(i+1, s.length)
        for (let letter of letters){
            let palindrome = letter + s[i] + letter
            if (left.includes(letter) && right.includes(letter) && !set.has(palindrome)){
                set.add(palindrome)
                ++counter
            }
        }
    }
    return counter
    */
    
    /*
    O(N^3) brute force solution
    1) generate every unique 3 length subsequence in the string
    2) check if each subsequence is a palindrome
    */
    /*
    var isPalindrome = function(s){
        let l = 0
        let r = s.length-1
        while (l <= r){
            if (s[l] !== s[r]){
                return false
            }
            l++
            r--
        }
        return true
    }
    if (s.length >= 3){
        let set = new Set()
        for (let i = 0; i < s.length; ++i){
            for (let j = i+1; j < s.length; ++j){
                for (let k = j+1; k < s.length; ++k){
                    let subsequence = s[i] + s[j] + s[k]
                    set.add(subsequence)
                }
            }
        }
        let counter = 0
        for (let word of set){
            if (isPalindrome(word)){
                ++counter
            }
        }
        return counter
    }
    return 0
    */
};