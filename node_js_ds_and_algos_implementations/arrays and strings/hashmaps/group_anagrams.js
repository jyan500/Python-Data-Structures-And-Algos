/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    /*
    I would first create a key that when sorted, can be used to determine whether two strings are anagrams of each other
    I would then create a hashmap that stores these sorted keys as keys, and values as an array of the strings that are anagrams of each other
    Finally I'd iterate through the values of the hashmap to get all the groups and return
    */
    let groups = {}
    for (let str of strs){
        let key = [...str].sort((a,b) => a.localeCompare(b)).join("")
        if (!(key in groups)){
            groups[key] = [str]
        }
        else {
            groups[key].push(str)
        }
    }
    return Object.values(groups)
};

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