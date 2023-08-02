'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''

"""
Revisited on 8/2/2023
Similar solution to below:
Key concepts:
1) Use a stack
2) Continually add any digits to the stack
3) If you see an operator, pop the last two items off the stack (both values should be digits)
evaluate, and then push back onto the stack
i.e 
tokens = ["3", "5", "+", "4", "/"]
1) adds 3 and 5 to the stack
2) stack = [3, 5], gets to "+"
3) pops off 5 then 3
   5 + 3 = 8, adds 8 to the stack
   stack = [8]
4) adds 4 to the stack
   stack = [8, 4]
5) Division operator:
   8/4 = 2
   Adds 2 to the stack
   [2]

Return stack[0]

4) In order to round a decimal towards 0, convert the division operation (i.e -2/4) to an int:
int(-2/4) = 0, if you don't do this, it's -.5 instead. Floor will actually round down to -1, so 
don't use that here

"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if i == 0:
                stack.append(int(token))
            else:
                if token == "+":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    res = secondNum + firstNum
                    stack.append(res)
                elif token == "-":  
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    res = secondNum - firstNum
                    stack.append(res)
                elif token == "*":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    res = secondNum * firstNum
                    stack.append(res)
                elif token == "/":    
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    # int rounds towards zero, even for negative decimals below 1
                    # i.e -.5 evaluates to 0
                    res = int(secondNum / firstNum)
                    stack.append(res)
                else:
                    stack.append(int(token))
        return stack[0]

from math import floor, ceil
class Solution:
    ## Stack solution by TimZeng
    ## as we iterate through our list, we append numeric values to the stack
    ## if we see an operator, we pop off twice to get the left and right, and then apply the operator
    ## then we save the result into the stack
    ## O(N) time solution since we can iterate through in one pass, without any extra iterations
    ## like in our initial solution
    ## Space is O(number of numeric elements) because we only store numeric elements on our stack
    ## https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/550862/Python-3-Stack
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        N = len(tokens)
        
        while (i < N):
            token = tokens[i]
            if (token in '+-/*'):
                ## if we see an operator, we pop one time to get the right value, and pop again to 
                ## get the left value
                right = stack.pop()
                left = stack.pop()
                result = 0
                if (token == "+"):
                    result = left+right
                elif (token == "-"):
                    result = left-right
                elif (token == "/"):
                   # if our left and right are both negative however, we'd want to do a floor operation
                    ## like normal since the final number is positive, a floor would truncate towards 0
                    if (left < 0 and right < 0):
                        result = floor(left/right)
                    ## if our left or right is a negative number, we actually want to do a ceiling
                    ## towards 0 (more positive) (as a floor in this case would make it more negative)
                    elif (left < 0 or right < 0):
                        result = ceil(left/right)
                    else:
                        result = floor(left/right)
                elif (token == "*"):
                    result = left*right
                
                stack.append(result)
            ## for numeric values, we push the int converted value onto the stack
            else:
                stack.append(int(token))
                    
            i+=1
        ## at the end, we can just return the last element in our stack as that will contain the result
        ## of the final operator
        return stack[-1]
    
        ''' 
        test case for the stack approach
        stack = []
        ["10","6","9","3","+","-11","*", "/", "*", "17","+","5","+"]
        i = 0
        stack = [10,6,9,3]
        i = 4, we see + sign
        pop off stack twice,
        left = 9, right = 3
        stack = [10,6]
        apply operator, 9+3, append to stack
        stack = [10,6,12]
        i=5, append -11 to the stack
        i=6, we see a * operator
        stack = [10,6,12,-11], pop off stack twice
        right = -11
        left = 12
        apply operator to left and right, 12 * -11 = -132, append to stack
        stack = [10, 6, -132]
        i = 7, we see divide operator
        pop off twice, left = 6, right = -132, stack = [10]
        here because one of the left and right is a negative number and we need to truncate
        our division to zero, we need to apply ceiling, so 
        6/-132 would become 0 (otherwise it'd be -1), append 0
        stack = [10,0]
        i = 8
        multiplication, pop off stack twice, left = 10, right = 0, append 0 as the result
        stack = [0]
        i = 9
        
        append 17 to the stack, stack = [0, 17]
        
        i = 10
        
        addition, stack [0,17], pop off twice
        0 + 17 = 17, append 17, stack = [17]
        
        i = 11
        append 5, stack = [17,5]
        i = 12
        + operator found, pop off twice, stack = []
        left = 17 right = 5
        result = 22, append to the stack, stack=[22]
        
        return last item in the stack, which is 22
        
        '''

    ## my initial approach involves truncating the array on each operation
    ## Time complexity I think is still O(N) but there's 2 added iterations for every operation
    ## since we're going 2 spots backwards on every operator
    ## Space complexity is O(1)
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        ["10","6","9","3","+","-11","*", "/", "*", "17","+","5","+"]
        i = 0
        at i = 4, we have our + operator
        we look at the previous two elements in our list
        apply our operator left to right,
        where in this case, left is 9 and right is 3
        after that, we truncate our list, to replace elements 9, 3 and + 
        with our result, which should be 12. The list length will decrease at this 
        point, and we would want to also change our i value as well to account
        for the decrease
        
        
        '''
        i = 0
        N = len(tokens)
        if (N == 1):
            return tokens[0]
        
        result = 0
        while (i < N):
            ## we want to look at previous two elements
            operator = tokens[i]
            if (operator in '+-/*'):
                right = int(tokens[i-1])
                left = int(tokens[i-2])
                if (operator == "+"):
                    
                    result = left + right           
                    ## print(f"{left} + {right} = {result}")
                elif (operator == "-"):
                    result = left - right
                    ## print(f"{left} - {right} = {result}")
                elif (operator == "/"):
                    ## if our left and right are both negative however, we'd want to do a floor operation
                    ## like normal since the final number is positive, a floor would truncate towards 0
                    if (left < 0 and right < 0):
                        result = floor(left/right)
                     ## if our left or right is a negative number, we actually want to do a ceiling
                    ## towards 0 (more positive) (as a floor in this case would make it more negative)
                    elif (left < 0 or right < 0):
                        result = ceil(left/right)
                    else:
                        result = floor(left/right)
                    ## print(f"{left} / {right} = {result}")
                elif (operator == "*"):
                    result = left * right
                    ## print(f"{left} * {right} = {result}")
                tokens = tokens[0:i-2] + [result] + tokens[i+1:]
                i-=2
                N-=2
            ## i, i-1, i-2, truncate the list
            ## remove elements i, i-1 and i-2 and replace with our result
            ## add everything in the list before the i - 2 element, our result, and everything
            ## from i+1 onwards (not including the value at i)
            
            ## i=4
            ## N = 13 - 3 + 1 = 11
            ## ["10","6","9","3","+","-11","*", "/", "*", "17","+","5","+"]
            ## i = 2
            ## ["10","6","12","-11" ... ]
                
            ##. in our truncated version, we've decreased the list length by 2, and decreased i by 2
        
           
            
            ## increment by 1 for the next iteration
            i+=1
            
        return result
            
        '''
        
        Test case for initial approach #1
        
        ["10","6","9","3","+","-11","*", "/", "*", "17","+","5","+"]
        i = 4, we see + operator
        result = 9+3=12
        10,6,12,-11,*,/,*,17,+,5,+
        N = 11
        i = 2
        
        i = 4, we see * operator
        12 * -11 = -132
        result = -132
        10,6,-132,/,*,17,+,5,+
        N=9
        i=2
        
        i=3, we see / operator
        6//-123 = 0
        10,0,*,17,+,5,+
        i = 1
        N=7
        
        i = 2, we see * operator
        10 * 0 = 0
        0,17,+,5,+
        i = 0
        N = 5
        
        increment i back to 2, and we see + operator
        0+17 = 17
        i = 0
        N = 3
        17,5,+
        
        22
        
        '''
            
        
    
       
