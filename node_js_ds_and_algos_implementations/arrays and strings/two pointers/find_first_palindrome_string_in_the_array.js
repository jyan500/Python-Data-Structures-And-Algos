/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
    var isPalindrome = function(word){
        let l = 0
        let r = word.length-1
        while (l <= r){
            if (word[l] !== word[r]){
                return false
            }
            ++l
            --r
        }
        return true
    }
    for (let word of words){
        if (isPalindrome(word)){
            return word
        }
    }
    return ""
};