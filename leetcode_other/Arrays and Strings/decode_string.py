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
        