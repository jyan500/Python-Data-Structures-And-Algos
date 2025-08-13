'''
https://leetcode.com/problems/basic-calculator-ii/


Initial Approach

The idea behind this solution is that it will evaluate the multiplication/division
numbers first by doing a linear scan of the multiplication/division signs, and then it will
search outwards (left and right) to find the numbers next to the multiplication/division signs to evaluate it
and update the numerical string with the result. And continue searching

Then, it will do a second pass over the numerical string, this time evaluating the addition/subtraction.
For this case, it accounts for negative numbers by including the dash (-) symbol as a part of the number
when searching outwards.

Potentially an O(N^2) time solution and O(N) space?

Optimized Approach (Using stack)
O(N) time and O(N) space

whenever we see a number, we add to a current number
if we see a - sign, we will push the current number to be negative (so that we can add all numbers at the end)
once we see an operator, we push our current number to the stack
and set the operator
if we see a multiplication or division,
we will pop off the stack and calculate the result using our current number, then evaluate
one last case is at the end of our iteration, we need to make sure to evaluate the last operator
since normally, we don't make an evaluation until we see another operator (but we're at the end of the string so we won't see another one)
finally, at the end, sum up all values in the stack
'''
class Solution:
    def calculate(self, s: str) -> int:
        """
        Revisited on 8/12/2025
        Revisited on 5/22/2025
        Similar to the solution on 4/22, slightly cleaner
        1) I would use a stack since I need to evaluate previous entries
        2) in order to follow order of operations, I could evaluate all the 
        multiplying and dividing first, and then make a second pass to evaluate
        addition and subtraction
        3) I could also make subtraction easier to evaluate by converting the number
        that's being subtracted to a negative number, and then I'd only need to perform a 
        sum( ... ) on the evaluated array

        4) String parsing, numbers can be more than one digit. It could be easier to just evaluate
        all the numbers first, doing all the string parsing. And then start evaluating operators
        """
        currentNumber = 0
        evaluatedNumbers = []
        stack = []
        operators = set(["-", "+", "/", "*"])
        for i in range(len(s)):
            if s[i].isdigit():
                # in order to add a digit, we have to multiply the existing number by 10 and then add the digit
                currentNumber = (currentNumber * 10) + int(s[i])
            # if we see an operator, we can reset the current number to 0 and add the current number
            # and operator to the stack
            if s[i] in operators:
                evaluatedNumbers.append(currentNumber)
                evaluatedNumbers.append(s[i])
                currentNumber = 0
        # it's assumed that we'll always have a valid expression, so we need to add the last number
        # after we finish building and iterating the string s
        evaluatedNumbers.append(currentNumber)
        for i in range(len(evaluatedNumbers)):
            if len(stack) > 0:
                if stack[-1] in operators:
                    operator = stack.pop()
                    if operator == "-":
                        stack.append(-1 * evaluatedNumbers[i])
                    elif operator == "*":
                        number = stack.pop()
                        stack.append(number * evaluatedNumbers[i])
                    elif operator == "/":
                        number = stack.pop()
                        stack.append(int(number/evaluatedNumbers[i]))
                    else:
                        stack.append(evaluatedNumbers[i])
                    continue
            stack.append(evaluatedNumbers[i])
        return sum(stack)

"""
Revisited on 4/22/2025
this solution is not as clean as the one on 2/4/2025 but
I managed to come up with it from memory.

Thought it made sense to do all the number parsing first to remove any
white spaces 

i.e from "  10 + 5 / 2 - 1" to [10, +, 5, /, 2, -, 1]
And then handling the multiplication/division using stack, and also treating any subtraction symbols
like negative numbers
so:
[10, 2, -1]

And then sum of the result above to get 11
"""
class Solution:
    def calculate(self, s: str) -> int:
        parsed = []
        stack = []
        curNum = 0
        # handle the number parsing first
        for i in range(len(s)):
            if s[i].isdigit():
                curNum = (10 * curNum) + int(s[i])
            elif s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/":
                parsed.append(curNum)
                curNum = 0
                parsed.append(s[i])
        # the reason for the extra curNum is that you have to include the
        # last number in the expression as it doesn't get added in the code above due
        # to the loop ending
        # note that it's okay if it's zero, since that doesn't affect the calculations below
        parsed.append(curNum)

        # handle only multiplication and division first
        onlyMultAndDiv = []
        stack.append(parsed[0])
        for i in range(1, len(parsed)):
            if len(stack) > 0:
                if stack[-1] == "*" or stack[-1] == "/":
                    operator = stack.pop()
                    num = stack.pop()
                    if operator == "*":
                        stack.append(num * parsed[i])
                    elif operator == "/":
                        stack.append(int(num/parsed[i]))
                    continue
                # if there's subtraction, we can treat the current
                # number as a negative number in order to make the next
                # step easier
                if stack[-1] == "-":
                    operator = stack.pop()
                    stack.append(parsed[i] * -1)
                    continue
            # if it's a subtraction symbol or number
            if parsed[i] == "-" or parsed[i] != "+":
                stack.append(parsed[i])
        # after creating the stack with all the multiplication and division evaluated,
        # and subtraction treated as negative numbers, we can just add everything in the stack
        # for the final result
        return sum(stack)
            

# revisited 2/4/2025, was asked this on interview today
# https://www.youtube.com/watch?v=2EErQ25kKE8&ab_channel=SaiAnishMalla 
# same solution as below
class Solution:
    def calculate(self, s: str) -> int:
        curNumber = 0
        operator = ""
        digits = set([str(i) for i in range(10)])
        operators = set(["+","-","/","*"])
        stack = []
        for i in range(len(s)):
            if s[i] in digits:
                curNumber = (curNumber * 10) + int(s[i])
            # we evaluate the numbers in the stack as soon as we reach another operator
            # the goal is to evaluate all multiplication and division signs first, then
            # evaluate addition and subtract after
            if s[i] in operators or i == len(s) - 1:
                # the operator == "" condition is only for the first time an operator is seen,
                # because we still need to add the current number the first time we see an operator
                # (no matter what the operator is)
                if operator == "+" or operator == "":
                    stack.append(curNumber)
                if operator == "-":
                    stack.append(-curNumber)
                if operator == "*":
                    # evaluate the previous element on the stack
                    stack[-1] = curNumber * stack[-1]
                if operator == "/":
                    # evaluate the previous number / cur number
                    stack[-1] = int(stack[-1]/curNumber)
                curNumber = 0
                operator = s[i]
        return sum(stack)

from math import ceil
class Solution:
	def calculate(self, s: str) -> int:
		stack = []
        operator = '+'
        current_number = 0
        for i in range(len(s)):
            ## if digit
            if (s[i].isdigit()):

                if (current_number != 0):
                    current_number = int(str(current_number) + s[i])
                else:
                    current_number = int(s[i])

            ## if we're about to end the loop at i == len(s)-1, we have to do a final evaluation
            ## for our last operator, since normally we don't do the evaluation until we see another operator
            if (s[i] in '+-*/' or i == len(s)-1):
                ## if we see an operator
                ## we will evaluate the previous operator we've seen
                if (operator == '+'):

                    stack.append(current_number)
                ## if our last operator was a - sign, we need to convert the current number
                ## we've built up to be negative
                elif (operator == '-'):
                    stack.append(-current_number)
                elif (operator == '*'):
                    left = stack.pop()
                    stack.append(left * current_number)
                elif (operator == '/'):
                    left = stack.pop()
                    if (left < 0 and current_number < 0):
                        stack.append(left//current_number)
                    elif (left < 0 or current_number < 0):
                        stack.append(ceil(left/current_number))
                    else:
                        stack.append(left//current_number)
                current_number = 0
                operator = s[i]
        
        return sum(stack)
        
        '''
        33+6/2-30*2
        stack = []
        current_number = 0
        operator = '+'
        
        stack = []
        current_number = 3
        operator = '+'
        
        stack = []
        current_number = 33
        operator = '+'
        
        (+ operator found)
        stack = [33]
        current_number = 0
        operator = '+'
        
        stack = [33]
        current_number=6
        operator = '+'
        
        (/ operator found)
        stack = [33, 6]
        current_number = 0
        operator = '/'
        
        stack = [33, 6]
        current_number = 2
        operator = '/'
        
        (- operator found)
        stack = [33,6]
        (do the division based on the current operator, since operator hasn't been updated to - yet)
        pop 6 and do division 6/2

        stack should now be [33,3]
        operator = -
        
        stack = [33, -3]
        current_number = -3
        operator = '-' ( we append -3 instead of 3 since we want to add all numbers at the end)
        
        (* operator found)
        stack = [33, 3]
        current_number = 0
        operator = '*'
        
        stack = [33, -3]
        current_number = 2
        operator = '*'
        
        we need to evaluate the last expression since we're at the end of the string
        stack = [33]
        pop -3 and 2, -3*2 = 6, append -6
        
        loop exits
        
        
        
        stack = [33,-6]
        return 27
        
        '''

    def calculate(self, s: str) -> int:
        ## iterate through s, looking at each character
        ## have to be implementing order of operations
        ## PEMDAS, in this case there's no parenthesis
        ## what we can do is have some kind of priority
        ## on the multiplication and division operators over the addition and subtraction operators
        
        ## remove all the spaces
        new_s = ''
        result = 0
        for i in range(len(s)):
            if (s[i] != ' '):
                new_s += s[i]
        ## when iterating over s, if we see a multiplication or division operator
        ## immediately get the numbers previous and next of it by iterating left and right until we see
        ## another operator on either side
        N = len(new_s)
        i = 0
        while (i < N):
            if (new_s[i] == '/' or new_s[i] == '*'):
                left = i-1
                right = i+1
                left_num = []
                right_num = []
                ## iterate outwards from the operator to find the numbers to the left and right of the operator
                while (left >= 0 and new_s[left] not in '/*+-'):
                    left_num.append(new_s[left])
                    left-=1
                while (right < len(new_s) and new_s[right] not in '/*+-'):
                    right_num.append(new_s[right])
                    right+=1
                ## reverse the numbers in left_num array to print out the proper orientation 
                ## since they get added in from last to first
                left_num = int(''.join(left_num[::-1]))
                right_num = int(''.join(right_num))

                ## evaluate the result as an integer
                if (new_s[i] == '/'):
                   
                    result = int(left_num)/int(right_num)
                else:
                    result = int(left_num)*int(right_num)
                
                ## update new_s so that it will remove all the old numbers and include the new result
                ## of the multiplication/division
                new_s = new_s[0:left+1] + str(int(result)) + new_s[right:]
                
                ## shift i backwards to adjust depending on the length of our new_s
                i = i - (N-len(new_s))
                ## if i becomes less than zero though, adjust i to start back at 0
                if (i < 0):
                    i = 0
                ## recalculate the new string length
                N = len(new_s)     
            i+=1
        
        i = 0
        N = len(new_s)
        ## after evaluating all multiplication and division operations
        ## evaluate the string with all addition and subtractions
        while (i < N):
            if (new_s[i] == '+' or new_s[i] == '-'):                
                left = i-1
                right = i+1
                left_num = []
                right_num = []
                ## iterate outwards from the operator to find the numbers to the left and right of the operator
                while (left >= 0 and new_s[left] not in '/*+-'):
                    left_num.append(new_s[left])
                    left-=1
                while (right < N and new_s[right] not in '/*+-'):
                    right_num.append(new_s[right])
                    right+=1
                ## special case to handle negative numbers, we include the negative as part of the number
                if (new_s[left] == '-'):
                    left_num.append('-')
                left_num = int(''.join(left_num[::-1]))
                right_num = int(''.join(right_num))
                
                if (new_s[i] == '+'):                 
                    result = int(left_num)+int(right_num)
                else:
                    result = int(left_num)-int(right_num)

                ## another edge case to handle negative numbers
                ## we want to include just the negative number in the result and not the negative
                ## number and an additional - sign
                if (new_s[left] == '-'):
                    new_s = new_s[0:left] + str(result) + new_s[right:]
                else:
                    new_s = new_s[0:left+1] + str(result) + new_s[right:]
                
                ## shift i backwards depending on the length of our new_s
                i = i - (N-len(new_s))
                if (i < 0):
                    i = 0
                ## recalculate the new string length
                N = len(new_s)                
            i+=1
        return int(new_s)
            
                
                
                
                    
                    
        
        