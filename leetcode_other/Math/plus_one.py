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
        