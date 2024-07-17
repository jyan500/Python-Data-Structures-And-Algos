/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
/* 
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

Approach:
find the counts of all characters in chars
total = 0
for each word in words
    make a copy of the counter
    length = 0 
    for each char in word
        if char in copy counter and count within the counter > 0
            decrease the count
            increase length
        else
            break
    if length equal to word's length
        add to total
return total

Time Complexity: O(N^2)
Space Complexity: O(N)
*/
var countCharacters = function(words, chars) {
    let counter = {}
    for (let c of chars){
        if (c in counter){
            ++counter[c]
        }
        else {
            counter[c] = 1
        }
    }
    
    let totalLength = 0
    for (let word of words){
        let copy = {...counter}
        let length = 0
        for (let c of word){
            if (c in copy && copy[c] > 0){
                ++length
                --copy[c]
            }
            else {
                break
            }
        }
        if (length === word.length){
            totalLength += word.length
        }
    }
    return totalLength
};