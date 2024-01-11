"""
https://leetcode.com/problems/add-binary/submissions/
O(N) Time
O(N) Space (to create the string once it's converted back to binary)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aBase10 = 0
        bBase10 = 0
        # convert a and b to base 10
        # add
        # start from the end, but we also want
        # the "end" to be 0, so we use j, where j = 0 represents 1, 
        # j = 1 represents 2, j = 2 represents 4 etc
        for i in range(len(list(a))-1, -1, -1):
            j = len(a) - 1 - i
            aBase10 += (2**j * int(a[i]))
        for i in range(len(list(b))-1, -1, -1):
            j = len(b) - 1 - i
            bBase10 += (2**j * int(b[i]))
        res = aBase10 + bBase10 
        # convert the sum back to base 2
        # continually divide by 2 until num <= 1,
        # at this case, we return either 1 or 0
        # if its >= 1, we return mod 2 to get the quotient
        # it should either be 1 or 0 as well
        def decimalToBinary(num: int):
            if num <= 1:
                return str(num) 
            else:
                res = decimalToBinary(num // 2) 
                return res + str(num % 2)
        resString = decimalToBinary(res) if res != 0 else "0"
        return resString
        
            