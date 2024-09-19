/**
 * @param {string} s
 * @return {string}
 */
/* 
https://leetcode.com/problems/reverse-words-in-a-string-iii/
O(N) Time
O(N) Space (space needed to store the current word)

In one pass, store an array where each character is added to the front. 
This creates the reversed word until a whitespace is found,
then add the reversed word to the final result and clear out the array and continue iterating

*/
var reverseWords = function(s) {
    let str = ""
    let currentWord = []
    for (let i = 0; i < s.length; ++i){
        if (s[i] === " "){
            str += currentWord.join("") + " "
            currentWord = []
        }
        else {
            currentWord.unshift(s[i])
        }
    }
    if (currentWord.length > 0){
        str += currentWord.join("")
    }
    return str
};