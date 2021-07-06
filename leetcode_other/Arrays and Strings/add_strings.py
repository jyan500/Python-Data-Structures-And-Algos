'''
https://leetcode.com/problems/add-strings/
https://leetcode.com/problems/add-strings/solution/
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ## initial thoughts
        ## if we can't convert num1 or num2 to integers at any point...
        ## convert to different data type?
        ## binary?
        
        ## elementary digit by digit addition with carryover
        
        ## for this solution, instead of using a dict to map the string version of the digit
        ## to its integer equivalent
        ## then we can use ord(), which takes in a string and returns an integer representing the unicode character
        ## we can get the integer version of the digit by taking ord(current_string_digit) - ord('0')
        
        ## time complexity 
        ## O(max(num1,num2)), where the time complexity comes from the string with the greater length
        ## space complexity, O(max(num1, num2)), where the space complexity comes from adding in characters of the string with the greater length to the stack
        
        digits = '0123456789'
        m = dict()
        ## map the string version of the digit to an integer
        for d in digits:
            m[d] = int(d)
        print(m)
        ## implement addition using carry-over
        '''
            129
             15
              4
              9+5 = 14
              if (cur_sum > 10), carry over 1
            3 + carryover = 7
        '''
        ## loop through the longer string
        longer_string = ''
        shorter_string = ''
        if (len(num1) > len(num2)):
            longer_string = num1
            shorter_string = num2
        else:
            longer_string = num2
            shorter_string = num1
        stack = []
        carryover = 0
        i = len(longer_string)-1
        j = len(shorter_string)-1
        while (i >= 0):
            if (j >= 0):
                res = m[longer_string[i]] + m[shorter_string[j]] + carryover
                ## print(res)
                if (res >= 10):
                    carryover = 1
                    stack.append(res % 10)
                else:
                    carryover = 0
                    stack.append(res)
                i-=1
                j-=1
            else:
                res = m[longer_string[i]] + carryover
                if (res >= 10):
                    carryover = 1
                    stack.append(res % 10)
                else:
                    carryover = 0
                    stack.append(res)
                i-=1
            ## print(stack)

        if (i <= 0 and j <= 0 and carryover != 0):
            stack.append(carryover)
                
        # s = ''
        # for i in range(len(stack)-1,-1,-1):
        #     s+=str(stack[i])
        # also can use join, by doing a list comprehension, with the third param of slice operator set to -1
        # to reverse the list
        
        return ''.join(str(s) for s in stack[::-1])
                
            
                
        