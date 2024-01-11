'''
Basics of Bit Manipulation

Notes from Gayle Laakman McDowell's video on Bit Manipulation
https://www.youtube.com/watch?v=NLKQEOgBAnw&ab_channel=HackerRank
---------------------------------------------------------------------------
Adding Binary numbers
---------------------------------------------------------------------------
Adding binary numbers works similar to how we add base 10 numbers
since in base 10, we add each digit and carryover the remainder which goes past 10, since we can
only represent 0 to 9 in one digit

For base 2 this works the same, since there's only 2 digits (either 0 or 1)
if we add two binary numbers together, we carryover a 1 if we add two ones together

for example:
 101 (this represents 5)
+011 (this represents 3)
------------------------
   0 (carryover the 1)

  1
 101 
+011 
------------------------
  00 (carryover the 1 again, since we get 1+0+1 = 2, need to carryover)

 1 
 101 
+011 
------------------------
 000 (carryover the 1 again, since we get 1+1+0)

  
 101 
+011 
------------------------
1000 (final result is 1000, which is 8)

---------------------------------------------------------------------------
Two's complement and representing negative integers in binary
---------------------------------------------------------------------------
for example, for the positive integer 18 (in base 10), for this 8 bit representation
in base 2 (binary) this would be 00010010, because 2^1 + 2^4 = 2 + 16 = 18

however, for negative numbers (i.e -18), we would store the integer in two's complement form.

The first bit of the binary representation determines the sign (known as the sign bit)
if the sign bit is 0, the integer is positive, whereas if the sign bit is 1, the integer is negative.
The other bits would be called the "non-sign bits" (basically anything after the sign bit)

For our 8 bit example, when figuring out how to represent -18 as binary, we need to figure out what sequence of bits we need to add to 
generate 2^8, since the first bit represents our sign bit of 1, which is a negative number

1 _ _ _ _ _ _ _ 

we can do this by simply inverting the non-sign bits of the binary representation of the positive integer,
and then add 1 to this inverted version.

For example, for -18, we invert the bits (00010010) to get the inverted version, which is 11101101
Then, we add 1 to this inverted version to get 11101110

so the final result would be 11101110, which represents -18

For the positive integer 123 for example, the binary representation would be
01111011, where the first 0 is the sign bit, and anything beyond is the non-sign bits

if we invert the bits we get 10000100, then we add 1
to get 10000101, which is the final result

----------------------------------------------------
Bit Shifting
----------------------------------------------------

Left and Right Shift
-----------------------------------------------------

For this example, we use 00010111 (23 in base 10)

if we wanted to left shift (<<, with the arrows pointing left), we'd move all the digits over to the left

00010111 becomes TRASH 00101110 (this would be 43, in base 10)

if we wanted to right shift (>>, with the arrows pointing right), we'd move all the digits over to the right

00010111 becomes 00001011 TRASH, (this would be 11, in base 10)

the TRASH signifies that bit would be thrown away from the shift

For the left shift, we notice that this is the equivalent of multiplying the number by 2

For the right shift, we notice that this is the equivalent of dividing the number by 2 (with some truncation)

What if we need to shift a binary representation of a negative number?

if we have -23,
11101001

In a logical right shift for example, we would simply just shift all the digits to the right, and for the sign bit,
we would fill that in with zero

11101001 becomes 01110100 (this represents 116 in base 10)

However, we see that this new number 116 doesn't seem to have any obvious relationship to -23

For an arithmetic right shift however, we would also shift all the digits to the right including the sign bit,
but we would fill in the bit where the sign bit was with its original value.

For example,

11101001 becomes 11110100, where the sign bit gets filled with 1 again, this represents (-12 in base 10)
which is -12 (rounds up from -23/2 = -11.5)

--------------------------------------------------------------
Bitwise Operations and Masks
--------------------------------------------------------------

Bitwise
--------------------------------------------------------------
AND (&), if we AND, we only get a 1 if both bits are 1
0 & 1 = 0
0 & 0 = 0
1 & 1 = 1

OR (|), if we OR, we get a 1 if either of the bits are 1
0 & 1 = 1
0 & 0 = 0
1 & 1 = 1

Exclusive Or, XOR (^), if we XOR, we only get a 1 if one of the bits out of the two is 1. If both bits are 1 or 0, it 
will result in 0
0 ^ 1 = 1
0 ^ 0 = 0
1 ^ 1 = 0

NOT (~), if we have a 1 it becomes 0, and if its 0 it becomes 1, 
note its the only bitwise operator that only takes one parameter
~0 = 1
~1 = 0

Getting the ith bit
--------------------------------------------------------
(i.e getting the ith bit)

00101100, how we would figure that the third bit here is a 1 or 0?

If we create a mask (which is a binary representation but used to perform a bitwise operation with a different binary representation)
in this form:
00100000, which is basically having a 1 in the third spot, and the rest are zeroes. 
If we perform & operation with our original representation (00101100)

then we can figure out what the third bit is (counting from the leftside):

  00101100
& 00100000
----------
  00100000

As we can see, the third bit is a 1, because when we perform AND, we'd only get 1 if both bits are 1, otherwise we'd get 0

We can create this mask by doing the following operation:
Left shift 1 by i spots (depending on which ith bit we want to find)
1 << i (in the example above, we're actually left shifting 1 by 5 to get the mask, 1 << 5)

And then perform & operation with our binary representation (let's call it x)
x & (1 << i)

then we just need to check if the value is 1 or 0, if we get 1, we know the ith bit is 1 as well
x & (1 << i) != 0

Setting the ith bit
---------------------------------------------------------------
We can do something similar to what we did for getting a bit, involving a bit mask
but instead we will use the OR operator

for the same example as above, if we wanted to set the third bit (counting from the left) to 1
  00101100
| 00100000
----------
  00101100

This will set that bit to 1
x | (1 << i) 

Clearing the ith bit
----------------------------------------------------------------
To clear the ith bit, we need to create a mask that's different from the above two examples
We want to create a mask that has every bit as a one EXCEPT the ith position that we want to clear, that would
have a value of zero

For example:
00101100, if we wanted to clear the third bit (counting third from the left, but counting fifth from the right)
to be a 0,

we would need to create a mask like so:
11011111, notice that third position is a zero rather than a one

then we would perform AND with this mask, to clear the bit

To actually create this mask in code though, we would take the mask we
made for getting a specific bit (1 << i), but we would invert it (NOT)
~(1 << i)

  00101100
& 11011111
----------
  11011111

We can see that we have successfully cleared that third bit to become zero

'''

