/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    /*
    using bit manipulation:
    the important property (similar to the problem "single number") 
    is using XOR to zero out two numbers that have the same value
    
    so if we were to have [0, 1, 3], where n = 3,
    to determine that 2 is the missing number, we'd need to XOR
    all values 0, 1, 2, 3 together, and then XOR 0, 1, 3 together.
    And then XOR these final two values together, this would give us the number
    that hasn't been cancelled out, which is 2
    
    XOR of 0 and 1
    0000 ^ 0001 = 0001
    XOR of the last result and 2
    0001 ^ 0010 = 0011
    XOR of the last result and 3
    0011 ^ 0011 = 0000
    
    XOR of 0 and 1
    0000 ^ 0001 = 0001
    XOR of the last result and 3
    0001 ^ 0011 = 0010
    
    XOR of the final two values
    0000 ^ 0010 = 0010, which gives us 2
    
    */
    let res1 = 0
    let res2 = 0
    for (let i = 0; i <= nums.length; ++i){
        res1 = res1 ^ i
    }
    for (let i = 0; i < nums.length; ++i){
        res2 = res2 ^ nums[i]
    }
    return res1 ^ res2
};