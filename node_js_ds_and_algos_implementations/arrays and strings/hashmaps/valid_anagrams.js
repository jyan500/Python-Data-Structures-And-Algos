/* 4/23/2026 cleaner code */
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        /*
        create a hashmap of letters in s
        iterate through the letters of t and decrement
        whenever a letter is found in the hashmap
        if all letters are found, all values in the hashmap should be 0 
        if a letter isn't in the hashmap, return false since that means it can't be anagram
        */
        let sMap = {}
        for (let i = 0; i < s.length; ++i){
            sMap[s[i]] = (sMap[s[i]] || 0) + 1
        }
        for (let i = 0; i < t.length; ++i){
            if (!(t[i] in sMap)){
                return false
            }
            --sMap[t[i]]
        }
        return Object.values(sMap).every((val) => val === 0)
    }
}

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