"""
Revisited on 5/5/2025
Problem found on intuit's list: 
https://github.com/liquidslr/leetcode-company-wise-problems/blob/main/Intuit/2.%20Three%20Months.csv
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        you can convert the numbers to strings first, perform string concatentation,
        and then check if there's a carryover after adding one
        and then convert back to string, split into an array

        can also iterate from the back of the array and add the numbers without needing
        to perform string concatenation

        [1,2,3]
        3 * (10*0)
        2 * (10^1)
        1 * (10^2)
        -----
        3 + 20 + 100 = 123
        O(2N) Time
        O(1) Space

        Can also keep as an array, and then perform the plus one operation directly
        on the array numbers starting from the back
        O(N) Time
        O(1) Space
        """

        # num = 0
        # j = 0
        # for i in range(len(digits)-1,-1,-1):
        #     num += (digits[i] * (10**(j)))
        #     j+=1
        # num += 1
        # res = []
        # while (num > 0):
        #     digit = num % 10
        #     res = [digit] + res
        #     num = num//10
        # return res

        carryover = 0
        res = [0] * len(digits)
        for i in range(len(digits)-1,-1,-1):
            curSum = digits[i] + 1 if i == len(digits) - 1 else carryover + digits[i]
            if curSum >= 10:
                carryover = 1
                res[i] = 0
            else:
                carryover = 0
                res[i] = curSum
        # in the case where there's still a carryover after iterating through all digits,
        # include the last digit
        if (carryover == 1):
            res = [carryover] + res
        return res
            
"""
https://leetcode.com/problems/plus-one/
simplified version of add strings
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover = 0
        output = []
        for i in range(len(digits)-1,-1,-1):
            s = digits[i] + carryover + 1 if i == len(digits)-1 else digits[i] + carryover
            if s >= 10:
                carryover = 1
                output.append(s - 10)
            else:
                output.append(s)
                carryover = 0
        if carryover != 0:
            output.append(carryover)
        output.reverse()
        return output
        