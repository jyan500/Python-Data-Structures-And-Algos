class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        /*
        find a substring within s2 that contains all the same letters and counts of each letter
        in s1

        since it's a contiguous substring, considering sliding window of length s1
        whenever the window shifts, decrement the letter count of l and increment on r
        within a hashmap

        we have to compare the hashmaps counts. Because we only store lower case letters in 
        the hashmap, this is at max an O(26) operation per loop

        Time: O(N*26)
        Space: O(26)
        */
        const compareMaps = (map1, map2) => {
            for (let k of Object.keys(map1)){
                if (!(k in map2) || map1[k] !== map2[k]){
                    return false
                }
            }
            return true
        }
        let s1Count = {}
        let s2Count = {}
        let l = 0
        for (let i = 0; i < s1.length; ++i){
            s1Count[s1[i]] = s1[i] in s1Count ? s1Count[s1[i]] + 1 : 1
        }
        for (let r = 0; r < s2.length; ++r){
            if (s2[r] in s2Count){
                ++s2Count[s2[r]]
            }
            else {
                s2Count[s2[r]] = 1
            }
            if (r - l + 1 === s1.length){
                if (compareMaps(s1Count, s2Count)){
                    return true
                }
                if (r > 0 && s2[l] in s2Count){
                    --s2Count[s2[l]]
                    if (s2Count[s2[l]] === 0){
                        delete s2Count[s2[l]]
                    }
                }
                ++l
            }
        }
        return false
    }
}

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