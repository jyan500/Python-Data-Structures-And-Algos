"""
Key Concept:
Binary Search, where the value returned by "guess" function will
determine whether to search the left or right half
calculate mid as normal, where left = 1 ... right = n
pass in mid to the guess function
1) a guess value of 1 means the value we guessed is too small, so search the right half
2) a guess value of -1 means the value we guessed is too big, so search the left half
3) a guess value of 0 means we got it, so we return our mid (which is the number we guess)

Time Complexity:
O(LogN)
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        def search(left, right):
            mid = left + (right-left)//2
            ourGuess = guess(mid)
            # our guess is equal to target, return the value we guessed (which is mid)
            if ourGuess == 0:
                return mid
            # our guess is higher than the target, search the left half
            elif ourGuess == -1:
                return search(left, mid)
            # our guess is lower than the target, search the right half
            elif ourGuess == 1:
                return search(mid+1,right)
        return search(left, right)