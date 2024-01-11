"""
https://leetcode.com/problems/roman-to-integer/
You can use a hashmap to track the values of each character, keeping track
of the following edge cases:

I can be placed before V (5) and X (10) to make 4 and 9, essentially subtracting 1 from the total 
X can be placed before L (50) and C (100) to make 40 and 90, essentially subtracting 10 from the total
C can be placed before D (500) and M (1000) to make 400 and 900, essentially subtracting 100 from the total

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        catalog = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        count = 0
        for i in range(len(s)):
            if s[i] == "I":
                if i+1 < len(s):
                    if s[i+1] == "V" or s[i+1] == "X":
                        count -= 1
                        continue
            if s[i] == "X":
                if i+1 < len(s):
                    if s[i+1] == "L" or s[i+1] == "C":
                        count -= 10
                        continue
            if s[i] == "C":
                if i+1 < len(s):
                    if s[i+1] == "D" or s[i+1] == "M":
                        count -= 100
                        continue
            count += catalog[s[i]]
        return count