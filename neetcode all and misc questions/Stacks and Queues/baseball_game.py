"""
https://leetcode.com/problems/baseball-game/
"""
class Solution:
    """ Revisited 10/8/2024 """
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+" and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "D" and len(stack) > 0:
                stack.append(stack[-1] * 2)
            elif operations[i] == "C" and len(stack) > 0:
                stack.pop()
            else:
                stack.append(int(operations[i]))
        return sum(stack)

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