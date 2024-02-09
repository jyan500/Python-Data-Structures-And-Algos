/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
	/* O(N) Time O(N) Space */
    let parsed = []
    // remove any non alpha numeric characters,
    // and make sure that alpha numeric characters are lowercase
    for (let i = 0; i < s.length; ++i){
        if ((/[0-9a-zA-Z]/).test(s[i])){
            parsed.push(s[i].toLowerCase())
        }
    }
    let i = 0
    let j = parsed.length-1
    while(i < j){
        if (parsed[i] !== parsed[j]){
            return false
        }
        i++
        j--
    }
    return true
};