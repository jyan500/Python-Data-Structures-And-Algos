/*
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Time Complexity:
O(N*M), where M is the size of the needle and N is the size of the haystack

*/
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for (let i = 0; i <= haystack.length - needle.length; ++i){
        let sub = haystack.slice(i, i + needle.length)
        if (sub === needle){
            return i
        }
    }
    return -1
};

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let r = needle.length-1
    for (let l = 0; l < haystack.length; ++l){
        if (needle === (haystack.slice(l,r+1))){
            return l
        }
        ++r
    }
    return -1
};
