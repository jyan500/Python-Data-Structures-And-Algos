/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
/*
Time Complexity:
using the mathemetical trick of the even numbered powers,
this is reduced to O(LogN), since the number of recursive calls at each even number
is getting cut in half, in a similar way to binary search
*/
var myPow = function(x, n) {
    var search = function(x, n){
        if (n === 0){
            return 1
        }
        // the mathematical trick to this problem
        // is realizing that any even number power is the
        // product of the power/2, for example:
        // 2^4 = 2^2 * 2^2 = 16
        // 2^6 = 2^3 * 2^3 = 8 * 8 = 64
        // 2^7 = 2 * 2^6 = 2 * (2^3 * 2^3)
        // this calls the total recursive calls in half
        if (n % 2 === 0){
            let temp = search(x, n/2)
            return temp * temp
        }
        return x * myPow(x, n-1)
    }
    // if n is a negative number, we're going to convert this to its positive counterpart
    // by treating it as continuous division
    // i.e 2^-3 is the same as (1/2)^3
    if (n < 0){
        return search(1/x, -1*n)
    }
    return search(x, n)

};