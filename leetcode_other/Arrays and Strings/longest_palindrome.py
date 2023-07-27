"""
Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Time complexity: O(N)
Space Complexity: O(26 + 26) (at most one of each upper and lower case english letter)
Key Realizations:

1) Find the count of each amount of character within the input string
2) When finding the length of the palindrome, we pay attention to the amount that each character appears
so in the case of the following input string:
aaaaccdd
we get a counter dict like so: {a: 4, c: 2, d: 2}

3) Whenever we add two even numbers, they will ALWAYS be palindromes
So we can just add all the even numbered occurrences together

4) For odd numbered occurrences, we can take the greedy approach, odd numbered amount - 1, 
which retrieves the max
amount that's still an even number so we can add to our palindrome, like so:
aaaaccddeeeeejjj, {a: 4, c: 2, d: 2, e: 5, j: 3}

While we can't accept both e: 5 and j:3, we can do e:4 and j:2 instead

5) In the end, if we added an odd number and performed this greedy approach by subtracting one
from each odd numbered occurrence, we still need to add 1 back to our palindrome,
as that can be the center of our palindrome. In the previous example, 
{a: 4, c: 2, d: 2, e: 5, j: 3} -> greedy approach -> {a: 4, c:2, d:2, e:4, j:2}
could result in a palindrome like so:

aacdeejjeedcaa

We could add an additional "j" OR "e" into the center to then create the longest palindrome

aacdeej(e)jeedcaa OR aacdeej(j)jeedcaa

6) One edge case that occurs with this greedy approach is that if there's a letter that occurs
an odd numbered amount of times, AND a letter that only appears once
{a: 4, e:3, d:1}
because the "d" can act as our center of the palindrome, we don't need to add another 1 to 
our total result, and just count "d" as the center

"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = dict()
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1
        evenAmounts = 0

        oddAmounts = 0
        addedOne = False
        for val in counter.values():
            # you can add as many even
            # numbered length strings to a palidrome, and it'll remain
            # a palindrome, so add up all the even numbered occurences
            # of characters
            # i.e c: 4, d: 2, the longest palindrome is automatically ccddcc or dccccd, 
            # if you add e: 2, it'll still be a palindrome after that
            # eccddcce, etc
            if val % 2 == 0:
                evenAmounts += val
            # for any odd occurrences greater than 1, you CAN choose to take all letters but one letter
            # making this occurrence amount even again   
            elif val % 2 != 0:
                if val != 1:
                    oddAmounts += (val - 1)
                elif val == 1 and not addedOne:
                    oddAmounts += 1
                    addedOne = True
        # as an edge case,
        # when taking in all odd amounts that are not 1,
        # you need to add a 1 back to the total amount,
        # as for one of those odd numbered occurrences,
        # could add 1 additional letter as the center of our palindrome.
        # in the case there's already a letter that only occurs once, we DON't need to do this again,
        # which explains the "addedOne" boolena
        # i.e d: 3, e: 5,
        # collect d: 2 and e:4, eeddee,
        # we can add either e or d into the center to get the longest palindrome here
        # eedddee OR eededee
        if oddAmounts != 0 and not addedOne:
            oddAmounts += 1
        return evenAmounts + oddAmounts
                
        
        