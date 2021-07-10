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
        
        
                
        