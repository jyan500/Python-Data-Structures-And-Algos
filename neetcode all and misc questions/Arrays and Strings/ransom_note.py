"""
https://leetcode.com/problems/ransom-note/
"""
"""
First try:
Similar to the anagram problem,
make two hashmaps counting the number of occurences of each letter
Except in the second hashmap that represents the magazine,
because the magazine may have more characters than the ransom note for a given character,
we only increment the count of the character found in the magazine if it's less than the count
of characters that's necessary
i.e
ransom note: "fffbfg"
magazine: "effjfggbffjdgbjjhhdegh"

since f appears 4 times in the ransom note, but 5 times in the magazine,
we only increment f up to 4 times in the magazine dict

Check whether the magazine dict and the ransom note dict are the same. If there wasn't
enough characters in magazine dict to complete it, this should be false

Time complexity: O(N), where we perform O(1) checks to the hashmap to check for existence
Space Complexity: O(N)

"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteMap = dict()
        for i in range(len(ransomNote)):
            if ransomNote[i] in ransomNoteMap:
                ransomNoteMap[ransomNote[i]] += 1
            else:
                ransomNoteMap[ransomNote[i]] = 1
        magazineMap = dict()
        for i in range(len(magazine)):
            if magazine[i] in ransomNoteMap:
                if magazine[i] in magazineMap:
                    if magazineMap[magazine[i]] < ransomNoteMap[magazine[i]]:
                        magazineMap[magazine[i]] += 1
                    continue
                else:
                    magazineMap[magazine[i]] = 1
        return magazineMap == ransomNoteMap