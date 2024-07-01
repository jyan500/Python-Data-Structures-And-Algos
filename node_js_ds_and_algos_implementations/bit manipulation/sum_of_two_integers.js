/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
/*
It seems that this is a trick that you need to memorize,
but to add two numbers (i.e a, b) using bit manipulation,
you need to
a ^ b, which is (a XOR b)
(a & b) << 1, which is (a AND b) left shift by 1

This happens in a while loop, where each operation you do will
update the values for a and b, and the process repeats itself
until b === 0, which means there is no more carryover value.

Note that you have to store the value of (a & b) << 1 first,
since you don't want to use the new value of a, which would have changed to a = a ^ b

For example:
9 + 11

the binary rep for 9 is:
1001
binary rep for 11 is: 
1011

a = 1001, b = 1011
1st iteration
a & b << 1
1001
     &
1011
----
1001

1001 << 1 = 10010

a ^ b
1001
    ^
1011
----
0010

a = 0010, b = 10010

2nd iteration
a & b << 1
(when doing the &,
pads on the extra zero at the beginning)
00010
    &
10010
-----
00010 << 1 = 00100

a ^ b
00010
     ^
10010 
-----
10000

a = 10000 b = 00100
3rd iteration

a & b << 1

10000
00100

becomes 0

10000
     ^
00100
-----
10100

because b is now 0, we don't enter the while loop again

final answer, returns a

10100 which is 2^4 + 2^2 = 20


*/
var getSum = function(a, b) {
    while (b !== 0){
        let tmp = (a & b) << 1
        a = a ^ b
        b = tmp
    }
    return a
};