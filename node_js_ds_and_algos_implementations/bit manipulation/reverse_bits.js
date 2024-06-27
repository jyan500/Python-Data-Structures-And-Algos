/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    /*
    check out the top comment on
    https://www.youtube.com/watch?v=UcoN6UjAI64&ab_channel=NeetCode
    
    for each bit in 32 bit integer
        left shift res by 1
        determine whether the last bit in n is 1 
        by doing logical AND
        add the bit to res
        right shift n by 1
    
    Example:
    n = 1010
    res << 1  res += n & 1  n >> 1
       00         00         101
      000        001          10
     0010       0010           1
    00100      00101           0
    
    In javascript, the final result needs a final
    unsigned right shift (>>>) in order to remove
    the sign to fix issues with negative numbers
    
    */
    let res = 0
    for (let i = 0; i < 32; ++i){
        res = res << 1
        res += (n & 1)
        n = n >> 1
    }
    return res >>> 0
};
