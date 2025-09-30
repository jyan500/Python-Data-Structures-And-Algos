"""
Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Revisited on 9/30/2025 with a simpler solution

        palindromes follow a pattern where there's at least 2 of each character,
        with the exception of the middle element.
        So the goal is to count the amount of elements that can be used to contribute
        to the palindrome (even count) plus an additional element with only a value of 1 that 
        can be used as the middle element (if present)

        ccdadcc
        1 + 2 + 2 + 2
        ccddcc
        2 + 2 + 2

        There is one edge case that's not handled here
        ddd, counter = {d: 3}
        In this case, you check whether the counter[d] is >= 2,
        can perform integer division to see how many times it can
        be divided by 2 evenly, and then subtract that value from the total count 
        for that counter

        i.e 
        3 // 2 is 1, so 2 goes into 3 one time evenly, so to find the total amount
        of characters that can be used to contribute towards the palindrome, it'd be
        1 * 2 = 2 characters that can be used, so 3 - 2 = 1, and you're left with c = {d: 1}

        Then, in the second for loop, check to see if there are any characters with value of 1,
        in this case, the only character left is d, so this forms the longest palindrome of 
        2 + 1 = 3

        O(N) Time
        O(N) Space

        """
        from collections import Counter
        c = Counter(s)
        # count how many characters have an amount >= 2,
        # if so, perform integer division to determine how many times that can character can be used
        # to contribute to the palindrome amount, and then decrease the count of that character
        amt = 0
        for keys in c:
            if c[keys] >= 2:
                evenAmt = (c[keys] // 2) * 2
                amt += evenAmt
                c[keys] -= evenAmt
        # after accounting for all values >= 2,
        # find at least one key with value of 1 so it can be used in the palindrome 
        # if not, the palindrome can still be made, but it will be an even numbered palindrome
        # this can also be the same character as well (like in the case of "ddd", c = {d: 3} becomes c = {d:1})
        for keys in c:
            if c[keys] == 1:
                amt += 1
                break
        return amt

class Solution:
    """
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
                
        
        