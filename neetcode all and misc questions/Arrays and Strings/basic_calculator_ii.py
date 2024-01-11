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
            
                
                
                
                    
                    
        
        