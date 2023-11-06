"""
https://leetcode.com/problems/baseball-game/
"""
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            isInt = False
            try:
                num = int(operations[i])
                isInt = True
            except:
                isInt = False
            if isInt:
                stack.append(int(operations[i]))
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                stack.append(stack[-1] * 2)
            elif operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)