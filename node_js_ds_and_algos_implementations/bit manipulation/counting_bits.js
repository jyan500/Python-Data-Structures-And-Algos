// iterating through the bits of a number is actually o(LogN) operation (and not O(N)),
// so the time complexity is O(NLogN)
class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
        let res = []
        for (let i = 0; i <= n; ++i){
            let num = i
            let numOnes = 1
            // algorithm to iterate through the binary representation of a base 10 number
            // extract the rightmost bit (num & 1), then right shift by 1 bit ( num = num >> 1)
            while (num > 0) {
                const bit = num & 1; // Extract the rightmost bit
                console.log(bit);    // 0, then 1, then 0, etc.
                if (bit === 1){
                    ++numOnes
                }
                num >>= 1;           // Shift right by 1 bit
            }
            res.push(numOnes)
        }
        return res
    }
}

/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    /*
    apply the algorithm from "number of one bits" problem
    that counts the number of 1's from i ... n

    using logical AND to see if the last digit of the binary representation is a one,
    and then right shifting the num by one continuously until num === 0
    */
    var countOnes = function(num){
        let res = 0 
        while (num){
            // if we do logical AND 
            // with 1, we determine 
            // whether the last digit is a one
            // or not
            if (num & 1 === 1){
                ++res
            }
            // right shift by one
            // to move onto the next digit
            // so it becomes the "last" digit
            num = num >> 1
        }
        return res
    }
    let res = []
    for (let i = 0; i <= n; ++i){
        res.push(countOnes(i))
    }
    return res
};