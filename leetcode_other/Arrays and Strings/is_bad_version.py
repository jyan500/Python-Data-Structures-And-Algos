'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1

Concept:
this is just a binary search, where when performing our binary search,
when we call isBadVersion(n) to determine if the current version is bad, 
if its bad we set the right to our midpoint to continue searching the left half
however, isBadVersion(n) is false (which means its a good version), we need to check
later versions by setting the left = midpoint + 1 to search the right half.

'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    ## Time complexity: O(LogN), since we're splitting the possibilities in half each time
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        midpoint = None
        while (left < right):
            midpoint = left+(right-left)//2          
            if (isBadVersion(midpoint)):
                right = midpoint
            else:
                left = midpoint+1
        ## the left pointer will contain the first bad version
        ## to account for cases where the last version is bad (rightmost element)
        ## because of our condition left < right, we can't always rely on the midpoint to give 
        ## the answer since it won't be calculated in those cases.
        return left
        