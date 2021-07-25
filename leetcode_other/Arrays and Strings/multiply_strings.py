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
            