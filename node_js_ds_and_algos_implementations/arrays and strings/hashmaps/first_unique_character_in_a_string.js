/**
 * @param {string} s
 * @return {number}
 */
/*
O(N) time O(N) Space
Two pass solution:
1) iterating from i ... s.length - 1, get the counts of each character
2) iterating through the string a second time, check to see if the character
at i has a count of 1, if so return the index
*/
var firstUniqChar = function(s) {
    let counter = {}
    for (let i = 0; i < s.length; ++i){
        if ((s[i] in counter)){
            counter[s[i]]++
        }
        else {
            counter[s[i]] = 1
        }
    }
    for (let i = 0; i < s.length; ++i){
        if (counter[s[i]] === 1){
            return i
        }
    }
    return -1
};