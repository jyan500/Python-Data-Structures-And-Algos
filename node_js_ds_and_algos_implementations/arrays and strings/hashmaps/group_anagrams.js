/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let c = {}
    for (let s of strs){
        // using the sorted version of the string as the key,
        // any other string that sorts to the same key will be considered an anagram,
        // so we can add the original string to a list as the value
        let sorted = s.split("").sort().join("")
        if (sorted in c){
            c[sorted].push(s)
        }
        else {
            c[sorted] = [s]
        }
    }
    return Object.values(c)
};