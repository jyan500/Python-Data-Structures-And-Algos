/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
 /*
 1) Keep char count obj of s1
 2) Iterate through string s2 in slices of j ... n 
 3) Iterate through the slice, make a copy of the char count obj of s1, and then decrement it
 each time a character within the slice is found in char count
 4) If the copy of the char count obj has values of all 0 , that means this is a permutation of the string,
 as all the same characters, as well as the count of characters of each is the same.

 Time Complexity:
 O(N*k), where N is the length of s2 and k is the length of s1, k is a fixed number
 in this problem though

 Space:
 O(N)
 */
var checkInclusion = function(s1, s2) {
    let counter = {}
    for (let i = 0; i < s1.length; ++i){
        if (s1[i] in counter){
            ++counter[s1[i]]
        }
        else {
            counter[s1[i]] = 1
        }
    }
    let n = s1.length
    let j = 0
    while (j + n - 1 < s2.length){
        let counterCopy = {...counter}
        let slice = s2.slice(j, j+n)
        for (let k = 0; k < slice.length; ++k){
            if (slice[k] in counterCopy){
                --counterCopy[slice[k]]
            }
        }
        if (Object.values(counterCopy).every(x => x === 0)){
            return true
        }
        ++j
    }
    return false
};