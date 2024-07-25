/**
 * @param {string[]} words
 * @return {boolean}
 */
var makeEqual = function(words) {
    /*
    O(N) Time O(N) Space
    1) get the count of each individual character for all words in the words list
    2) the character counts for each character must be divisible amongst the amount 
    of total words in the words list
    
    example:
    ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]
    
    the counter would look like this {c: 45, a: 15, b: 15}
    
    there are 15 words in total
    
    each of the character counts is divisible by 15. Therefore, there exists a way to shift characters around such 
    that every word has the same characters. Although the problem states the ordering must be the same, that doesn't really matter,
    since we can just assume that we can shift the ordering anyway we want as long as the characters that exist in both words
    are the same.
    */
    let counter = {}
    for (let i = 0; i < words.length; ++i){
        for (let c of words[i]){
            if (c in counter){
                counter[c]++
            }
            else {
                counter[c] = 1
            }
        }
    }
    for (let v of Object.values(counter)){
        if (v % words.length !== 0){
            return false
        }
    }
    return true
    
};