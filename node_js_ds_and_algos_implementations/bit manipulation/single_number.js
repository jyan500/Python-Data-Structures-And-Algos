/**
 * @param {number[]} nums
 * @return {number}
 */
/*
The trick to this problem is recognizing that you can use bit manipulation,
specifically XOR

Remember that XOR means that
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

Therefore, if we were to convert each number to it's base 2 form and then take the XOR
of each number, if two numbers are the same, they will also have the SAME bits. Therefore,
taking XOR of two numbers will always result in them becoming 0. So the number
that only appears once will be the final result, as it'd be the only bits that don't get 
zeroed out.

It also doesn't matter what order we XOR in, so we can just start in the beginning of the array
For example:

1 = 0001
2 = 0010
4 = 0100
4 = 0100
2 = 0010

We see that there's two 2's and two 4's

If we run the algorithm starting from 1

(res starts at 0)
res = 0000

0000 ^ 0001 = 0001
0001 ^ 0010 = 0011
0011 ^ 0100 = 0111
0111 ^ 0100 = 0011
0011 ^ 0010 = 0001

Therefore, you can see at the end, it reverts back to 0001

Time: O(N)
Space: O(1)
*/
var singleNumber = function(nums) {
    res = 0
    for (let num of nums){
        res ^= num
    }
    return res
};
