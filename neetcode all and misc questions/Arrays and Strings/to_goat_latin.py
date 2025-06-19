"""
https://leetcode.com/problems/goat-latin/description/
Approach:
Main logic is figuring out whether the first letter (when lowercase) is in the vowels set or not.
From there, its just string parsing
O(N) Time
O(N) Space
"""
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        words = sentence.split(" ")
        res = []
        for i in range(len(words)):
            numA = (i+1) * "a"
            word = words[i]
            newWord = ""
            if word[0].lower() in vowels:
                newWord = word + "ma"
            else:
                newWord = word[1:] + word[0] + "ma"
            newWord += numA
            res.append(newWord)
        return " ".join(res)