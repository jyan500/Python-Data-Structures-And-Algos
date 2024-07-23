/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    /*
    Time: O(N)
    Space: O(N)
    1) create both alternating binary strings (0101..., 1010...) of length S
    2) compare each char of S to each of char of the binary strings, and see 
    how many characters are not matching. This would be the number of flips necessary
    to create that alternating binary string.
    3) Take the min between the number of flips to create 0101 ... and 1010 ... to get
    the min number of flips to make an alternating binary string
    */
    let N = s.length
    let s1 = []
    let s2 = []
    for (let i = 0; i < N; ++i){
        if (i % 2 === 0){
            s1.push(1)
            s2.push(0)
        }
        else {
            s1.push(0)
            s2.push(1)
        }
    }
    let startsWithZero = s2.join("")
    let startsWithOne = s1.join("")
    let requiresFlip1 = 0
    let requiresFlip2 = 0
    for (let i = 0; i < N; ++i){
        if (s[i] !== startsWithZero[i]){
            ++requiresFlip1
        }
        if (s[i] !== startsWithOne[i]){
            ++requiresFlip2
        }
    }
    return Math.min(requiresFlip1, requiresFlip2)
};