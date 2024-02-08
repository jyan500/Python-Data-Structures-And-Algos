/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let d1 = {}
    for (let i = 0; i < s.length; ++i){
        if (s[i] in d1){
            ++d1[s[i]]
        }
        else {
            d1[s[i]] = 1
        }
    }
    // after counting all characters in string S, use the same dictionary
    // if the character in T is not in S, we can automatically return false
    // in string T, but decrement the counts of each character
    for (let i = 0; i < t.length; ++i){
        if (t[i] in d1){
            --d1[t[i]]       
        } else {
            return false
        }
    }
    // if all characters in d1 are set to 0, that means that both strings had the same
    // amount of each character, making them anagrams of each other
    let values = Object.values(d1)
    for (let i = 0; i < values.length; ++i){
        if (values[i] > 0){
            return false
        }
    }
    return true
};