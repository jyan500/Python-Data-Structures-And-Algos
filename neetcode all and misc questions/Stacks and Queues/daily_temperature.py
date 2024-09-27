'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Important Concept to optimal solution: 

Monotonic Decreasing Stack
-where the items on the stack are in strictly decreasing order or equal to each other
meaning that if we add any item to the stack that changes the order, we need to pop
the items to keep it in monotonic decreasing order

-We utilize the monotonic stack by appending to the stack whenever we see a lower temperature than before
-If we see a greater temperature, we will start popping off from the stack and filling in the output array

https://leetcode.com/problems/daily-temperatures/
https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode

'''
"""
Revisited again on 9/26/2024
Have to remember about the monotonic stack where descending order is kept, this can be helpful
when you need to know a previous max
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if (len(stack) > 0):
                prevTemp, prevIndex = stack[-1]
                # if the current temperature is greater than the top of the stack,
                # that means we've found the first possible day where a temp was greater than
                # the temperature at the top of the stack, so we record the difference in indices
                # if we continue to pop, it's possible we continue finding temperatures that are less
                while (len(stack) > 0 and temperatures[i] > prevTemp):
                    stack.pop()
                    res[prevIndex] = i - prevIndex
                    if (len(stack) > 0):     
                        prevTemp, prevIndex = stack[-1]
            stack.append((temperatures[i], i))
        return res
"""
Revisited on 8/15/2023, watching Neetcode

Concept:
iterate through temps, push a tuple containing the value and the index
if the current temp is greater than the top of the stack, record the result and pop off the top of the stack
in a while loop, continue to do this process until the current temp is not greater than the top of the stack

input = [73,74,75,71,69,72,76,73]
result = [0, 0, 0, 0, 0, 0, 0, 0]
i = 0 stack = [(73, 0)]
i = 1 stack = [(73, 0)], 74 > 73, i = 0 in our result, record 1 - 0 and pop 73 off the stack
i = 2 stack = [(74, 1)], 75 > 74, at i = 1 in our result, record 1 - 0 and pop 74 off the stack
i = 3 stack = [(75, 2)] 71, 71 < 75, continue pushing
i = 4 stack = [(75, 2), (71, 3)], 69 < 71, continue pushing
i = 5 stack = [(75, 2), (71, 3), (69, 4)] 72, 69 < 72, at i = 4 in our result, record 5 - 4, pop 69 off stack
(we still are checking 72 here via the while loop)
i = 5 stack = [(75, 2), (71, 3)] 72 72 < 71, at i = 3, record 5 - 3, pop 71 off the stack
75 > 72, so our while loop breaks here
i = 6 stack = [(75, 2)] 76, 76 > 75, at i = 2, record 6 - 2 = 4, pop off stack
stack = [(76, 6)], 73, 73 < 76
stack = [(76, 6), (73, 7)], no more elements to compare

O(N) time:
even though there is a while loop, 
it simply pops out stack elements one by one,
and there can't be more than n elements pushed inside the stack as every element is pushed once.

O(N) space
""" 

# shorter solution 11/8/2023
class Solution:
    stack = []
    res = [0 for i in range(len(temperatures))]
    for i in range(len(temperatures)):
        if len(stack) > 0:
            while (len(stack) > 0 and temperatures[i] > stack[-1][0]):
                temp1, index1 = stack.pop()
                res[index1] = i - index1
            
            stack.append((temperatures[i], i))
                
        else:
            stack.append((temperatures[i], i))
    return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            if len(stack) > 0:
                while stack:
                    top, index = stack[-1]
                    if temperatures[i] > top:
                        res[index] = i - index
                        stack.pop()   
                    else:
                        break
            stack.append((temperatures[i], i))
        return res

class Solution:
    ## Brute Force
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## O(N^2) 
        output = []
        for i in range(len(temperatures)):
            output.append(0)
        for i in range(len(temperatures)):
            current_temperature = temperatures[i]
            num_days = 0
            for j in range(i, len(temperatures)):
                future_temperature = temperatures[j]
                if (future_temperature > current_temperature):
                    output[i] = num_days
                    break
                num_days+=1
        return output
        
    ## First attempt based off of neetcode's algorithm (O(N) space, O(N) time)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        output = []
        for i in range(len(temperatures)):
            output.append(0)
        ## save the temperature along with the index within the temperatures list as a tuple
        ## we start at 1 since we don't need to compare the zeroeth index item with itself
        stack = [(temperatures[0], 0)]
        i=1
        while (i < len(temperatures)): 
     
            stack_temperature = stack[-1][0]
            stack_temperature_index = stack[-1][1]
            ## if the current temperature is greater than the last temperature on stack
            if (temperatures[i] > stack_temperature):
                ## continue popping off the stack if the temperature on stack is less than our current temperature, we stop if the stack is empty or the stack's temperature exceeds our current temperature
                while (stack and stack[-1][0] < temperatures[i]):
                    stack_temperature = stack[-1][0]
                    stack_temperature_index = stack[-1][1]
                    ## save the index within temperatures array that was saved in the tuple
                    ## along with the difference between the current i - saved index
                    output[stack_temperature_index] = i-stack_temperature_index
                    stack.pop()
 
            ## if our current temperature is less than the last temperature on the stack
            ## append to our stack
            stack.append((temperatures[i], i))
            i+=1
      
        return output 
        
        
                
        