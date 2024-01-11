'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

https://leetcode.com/problems/multiply-strings/
'''

"""
Alternate solution simulating cross multiplication
O(N*M)
1) Same concept as add two strings, pads the shorter number with zeroes to make 
it easier if two numbers are different lengths to avoid edge cases
2) Calculates the "levels", where the levels are added at the end to get the final result. Each level
has one zero padded to it like in regular elementary cross multiplication
3) carryover gets added to the multiplied result, but on the last digit of each level, we just append
the result even if it's greater than 10

            123
            456 
            ___
            738 level = 0
           6150 level = 1 (1 zero padded)
          49200 level = 2 (2 zeroes padded)

    sum of all levels = 56088


"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def helper(top, bottom):
            carryover = 0
            levels = []
            cur = ""
            level = 0
            for i in range(len(bottom)-1,-1,-1):
                for j in range(len(top)-1,-1,-1):  
                    res = carryover + int(bottom[i]) * int(top[j])
                    if res >= 10:
                        # if we're on the last digit, don't do the carryover
                        # and just put the result
                        if j == 0:
                            cur = str(res) + cur
                            carryover = 0
                        else:
                            # carryover is the first digit of the result
                            carryover = int(str(res)[0])
                            # digit is the 2nd digit of the result
                            digit = str(res)[1]
                            cur = digit + cur
                    else:
                        cur = str(res) + cur
                        carryover = 0
                levels.append(int(cur))
                level += 1
                # each "level" of addition has one more zero padded to the end
                # like in regular cross multiplication
                cur = "0" * level
            return str(sum(levels))
        
        if len(num1) >= len(num2):
            numDifference = len(num1) - len(num2)
            num2 = ("0" * numDifference) + num2
            return helper(num1, num2)
        else:
            numDifference = len(num2) - len(num1)
            num1 = ("0" * numDifference) + num1
            return helper(num2, num1)

class Solution:
    ## O(N) time complexity, we're an iteration for num1 and for num2
    ## O(1) space
    def multiply(self, num1: str, num2: str) -> str:
        nums_dict = dict()
        ## map the string digit to its integer equivalent
        for i in range(10):
            nums_dict[str(i)] = i
        int_num1 = 0
        int_num2 = 0
        ## since we're building the integer up by calculating the integer amount at each 10's place
        ## we need to figure out the total number of 10's places to account for
        ## i.e 123 is equivalent to
        ## 123 =(1 * 10^2) + (2 * 10^1) + (3 * 10^0)
        num_places_1 = len(num1)-1
        num_places_2 = len(num2)-1
        for i in range(len(num1)):
            digit = num1[i]
            int_num1 += nums_dict[digit] * (10**num_places_1)
            num_places_1-=1
        for i in range(len(num2)):
            digit = num2[i]
            int_num2 += nums_dict[digit] * (10**num_places_2)
            num_places_2-=1
        return str(int_num1*int_num2)
    
    '''
    test cases
    num1 = "2", num2 = "3"
    nums_dict = {'0' : 0, '1' : 1, ...... '9' : 9}
    
    num_places_1 = 1 - 1 = 0
    num_places_2 = 1 - 1 = 0
    
    i = 0
    int_num1 = 0 + 2 * (10**0) = 2
    int_num2 = 0 + 3 * (10**0) = 3
    
    2 * 3 = 6
    
    test cases
    num1 = "123", num2 = "456"
    num_places_1 = 3 - 1 = 2
    num_places_2 = 3 - 1 = 2
    int_num1 = 0 + 1 * (10**2) = 100 (num_places_1 = 1)
    int_num1 = 100 + 2 * (10**1) = 20 (num_places_1 = 0)
    int_num1 = 120 + 3 * (10**0) = 123
    
    123 * 456
    
    '''
            