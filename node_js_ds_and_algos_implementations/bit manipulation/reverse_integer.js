/**
 * @param {number} x
 * @return {number}
 */
/*
O(LogN) solution, since LogN represents the number of digits in the number
O(1) space
*/
var reverse = function(x) {
    var isOutOfBounds = (digit, result) => {
        const MIN = -(2**31)
        const MAX = 2**31-1
        // note that MIN is -2147483648
        // MAX is 2147483647
        let [maxProduct, maxRemainder] = [MAX/10, MAX%10]
        let [minProduct, minRemainder] = [MIN/10, MIN%10]
        // maxProduct represents the max number that can be received
        // before multiplying by 10 and receiving the value of MAX
        // and then maxRemainder represents the max digit that is possible
        // for example, if a number exceeds 214748364, then it's out of bounds, since if you multiply this
        // by 10, it would exceeds the value of MAX
        // alternatively, if a number exceeds 7 (the last digit of 2147483647), then it's
        // also out of bounds
        // similar logic applies to the negative, except it's <= 
        let case1 = result > maxProduct || (result === maxProduct && digit >= maxRemainder)
        let case2 = result < minProduct || (result === minProduct && digit <= minRemainder)
        return case1 || case2
    }
    let res = 0
    while (x !== 0){
        // mod gives us the last digit of the number (one's place, ten's place, etc)
        let digit = x % 10
        // integer division by 10 moves the last digit one place
        // to the left (i.e from one's place to ten's place)
        if (isOutOfBounds(digit, res)){
            return 0
        }
        // use Math.trunc in javascript, otherwise with negative numbers,
        // if using floor, it will round down for negative numbers instead of rounding up (i.e -.5 goes to -1 instead of 0)
        x = Math.trunc(x / 10)
        // add the digit to the result by multiplying by
        // 10 first (i.e res = 3, lastDigit = 2, to get 32, it'd
        // be 3 * 10 = 30, 30 + 2, 32)
        res = (res * 10) + digit
    }
    return res
};