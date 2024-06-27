/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    /*
    O(N^2) solution is to 
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