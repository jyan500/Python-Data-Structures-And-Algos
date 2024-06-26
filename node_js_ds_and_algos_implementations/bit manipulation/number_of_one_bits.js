/**
 * @param {number} n
 * @return {number}
 */
/*
Approach:
Whenever we perform bitwise AND with 1,
it will determine whether the LAST bit is 1 or not,
since 0 & 1 = 0, 1 & 0 = 0, but 1 & 1 = 1

If it's 1, we increment our count

Then, we perform a bit shift to the right so the next
bit becomes the LAST bit again.

For example:
0101 (number 5)

0101 ^ 0001 = 0001, increment res by 1
010 ^ 001 = 000
01 ^ 01 = 01, increment res by 1
0 ^ 1 = 0
0, while loop ends

returns 2

Time: O(N)
Space: O(1)

*/
var hammingWeight = function(n) {
    let res = 0
    while (n !== 0){
        if (n & 1 === 1){
            ++res
        }
        n = n >> 1
    }
    return res
};