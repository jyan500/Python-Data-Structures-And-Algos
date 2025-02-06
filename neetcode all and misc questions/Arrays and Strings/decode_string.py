'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

https://leetcode.com/problems/decode-string/
'''
class Solution:
    def decodeString(self, s: str) -> str:
        """
        Revisited 2/5/2025
        Time: O(N)
        Space: O(N)
        Approach:
        stack = []
        curNumber = 0
        iterate through s
            if the current number is a digit, 
                continue building the digit by multiplying the current number by 10,
                and then adding the current digit (since the number can be greater than 9)
            if you reach an "[". 
                add the current number and then the "[" to the stack
                reset current number back to 0
            otherwise, if it's a letter
                add it to the stack normally

            if you reach a "]", 
                you need to pop off the stack until you reach
                a "[", all the while you need to be saving the popped off characters 
                as this will contain the sequence of characters that needs to be multiplied

                Once you reach the "[", pop off once more as this will be the number. 
                Multiply the number by the sequence of characters, and add to the stack

        At the end, join the stack and return

        """
        stack = []
        curNumber = 0 
        for i in range(len(s)):
            if s[i].isdigit():
                curNumber = (curNumber * 10) + int(s[i])
                continue
            if s[i] == "]":
                char = ""
                while (len(stack) > 0 and stack[-1] != "["):
                    char = stack[-1] + char
                    stack.pop()
                # pop off the opening brace
                stack.pop()
                # the number should now be the top of the stack
                # evaluate and pop off the number 
                number = stack.pop()
                result = number * char
                stack.append(result)
                continue
            if s[i] == "[":
                stack.append(curNumber)
                stack.append("[")
                curNumber = 0
            else:
                stack.append(s[i])
        return "".join(stack)
        
"""
Revisited on 1/23/2024
Took around ~25 mins to do after some refreshing on the solution
The slight change in approach this time was if the previous element 
on the stack was a digit, just continue adding onto this element to 
form the number instead of appending a separate element to the stack

i.e 
10[abc]

stack = [1],

in the next iteration, add 0 to 1
stack = [10]

instead of 
stack = [1, 0]

That way, once we start evaluating the expression between the braces,
stack =  [10, [, c, ], ]
after getting our inner string of "c",
we can just pop off once more to get 10,
and then multiply and append back to the stack


"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            # if the previous element in the stack was also numeric, continue forming the number
            if s[i].isnumeric() and len(stack) > 0 and stack[-1].isnumeric():
                stack[-1] += s[i]
                continue
            if s[i] == "]":
                inner = ""
                while (len(stack) > 0 and stack[-1] != "["):
                    inner = stack[-1] + inner
                    stack.pop()
                stack.pop() # pop once more for the opening bracket
                # because a bracket is always after the multiplier, the multiplier should be the next element in the stack
                multiplier = stack.pop()
                res = int(multiplier) * inner
                # append the result once we've evaluated everything between the braces
                # and multiplied by the appropriate multiplier
                stack.append(res)
                continue
            stack.append(s[i])
        return "".join(stack)
"""
Revisited on 8/25/2023
https://www.youtube.com/watch?v=qB0zZpBJlh8&ab_channel=NeetCode
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            # closing bracket found
            # continually pop until we reach the opening bracket
            # after the opening bracket is popped, the top of the stack
            # must be a digit of the integer k in k[encoded string], 
            # keep popping until it's no longer a digit
            # multiply the string with the number k and append back to the top of the stack
            if s[i] == "]":
                element = []
                while (len(stack) and stack[-1] != "["):
                    element.insert(0, stack[-1])
                    stack.pop()
                # pop the opening bracket
                stack.pop()
                num = []
                while (len(stack) and stack[-1].isdigit()):
                    num.insert(0, stack[-1])
                    stack.pop()
                # multiply the string element by num
                # i.e 2 * "ab" = "abab"
                element = "".join(element) * int("".join(num))
                # bring element back to the top of the stack
                stack.append(element)
            else:
                stack.append(s[i])

        # at the end, we're going to end up with a list of strings, so join them together
        return "".join(stack)
        
                
        class Solution:
    def decodeString(self, s: str) -> str:
        ## Time: O(N), because we are iterating through the string once, plus some additional iterations
        ## through our stack, but our stack will always less than N elements
        ## Space: O(max(amount of characters between a set of braces within the input string))
        ## as we iterate, we pushed onto the stack
        ## however, if we see a numerical value, we want to make sure to keep the digits together into one number on the stack
        ## so append to the build_digit string, until our next element (s[i+1]) is not a digit, then
        ## we append our build_digit to the stack
        ## however, if we saw a closing brace
        ## we would pop off the stack, and add to an eval_string that would be operated on
        ## we continue to pop until we see a numerical number, then we multiply the numerical number with the eval string
        ## and append the eval string to our stack and break, so that we can continue to look for additional
        ## closing braces that appear later in the string
        ## at the end, our stack may contain more than one item, so we join the strings to form our answer
        
        stack = []
        build_digit = ''
        for i in range(len(s)):
            if (s[i].isdigit()):
                build_digit += s[i]
                if (not s[i+1].isdigit()):
                    stack.append(build_digit)
                    build_digit = ''
            elif (s[i] == "]"):
                eval_string = ''
                build_digit = ''
                while (stack):
                    char = stack.pop()   
                    if (char.isdigit()):
                        eval_string = int(char) * eval_string
                        stack.append(eval_string)
                        break
                    elif (char == "["):
                        continue     
                    else:
                        eval_string = char + eval_string
            else:
                stack.append(s[i])
        if (len(stack) > 1):
            return ''.join(stack)
        else:
            return stack[-1]
                        
                        
                        
            
    '''
    3[a]2[bc]
    stack = []
    i = 0, stack = [3]
    i = 1, stack = ['3', '[']
    i = 2, stack = ['3', '[', 'a']
    i = 3, closing brace is found
    pop off stack, get a, append to eval string
    pop off stack, get opening brace (skip)
    pop off stack, get 3
    eval_string = 3 * a = aaa
    stack = ['aaa']
    i = 4, s[i] = 2, stack = ['aaa', '2']
    i = 5, s[i] = [, stack = ['aaa', '2', '[']
    i = 6, s[i] = b, stack = ['aaa', '2', '[', 'b']
    i = 7, s[i] = c, stack = ['aaa', '2', '[', 'b', 'c']
    i = 8, s[i] = ], closing brace found, 
    pop off stack, get c, append to eval string
    pop off stack, get b, append to eval string
    pop off stack, get opening brace
    pop off stack, get 2, evaluate 2 * bc = bcbc
    append to stack ['aaa', 'bcbc']
    
    
    '''
    '''
    2[3[a]2[bc]]
    stack = []
    i = 0, stack = [2]
    i = 1, stack = ['2', '[']
    i = 2, stack = ['2', '[', '3']
    i = 3, stack = ['2', '[', '3', '[']
    i = 4, stack = ['2', '[', '3', '[', 'a']
    i = 5, closing brace is found
    pop off stack until we see number, evaluate
    stack = ['2', '[', 'aaa']
    i = 6, stack = ['2', '[', 'aaa', '2']
    i = 7, stack = ['2', '[', 'aaa', '2', '[']
    i = 8, stack = ['2', '[', 'aaa', '2', '[', 'b']
    i = 9, stack = ['2', '[', 'aaa', '2', '[', 'b', 'c']
    i = 10, closing brace is found
    pop off stack until we see number, evaluate
    stack = ['2', '[', 'aaa', 'bcbc']
    i = 11, closing brace is found
    pop off stack until we see number
    eval_string = aaabcbc
    2 * aaabcbc = aaabcbcaaabcbc
    stack = [aaabcbcaaabcbc]
    return -1
    '''
    '''
        s = "3[a2[c]]"
        stack = []
        i = 0, s[i] = 3
        stack = [3]
        i = 1, s[i] = [
        stack = [3,[]
        i=2, s[i] = a
        stack = [3,[,a]
        i=3, s[i] = 2
        stack = [3,[,a,2]
        i=4, s[i]=[
        stack=[3,[,a,2,[]
        i=5, s[i]=c
        stack=[3,[,a,2,[,c]
        i =6, s[i]=] (closing brace is found)
        pop off c
        eval_string = c
        stack = [3,[,a,2,[]
        pop off [ (don't add ot eval string)
        stack = [,3,[,a,2]
        pop off 2, isdigit
        2 * c = cc, append to stack
        stack = [3,[,a,cc]
        eval_string = ''
        i = 7, s[i] = ],
        after building up eval string we get acc
        once we see 3 popped off the stack ,it should evaluate to accacccacc
        on the stack it should be 
        stack = [accaccacc]
        
        
        
        
        
    '''
        