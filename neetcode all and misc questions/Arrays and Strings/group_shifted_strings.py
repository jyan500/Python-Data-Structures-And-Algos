"""
249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

class Solution:
    def groupShiftedStrings(self, strList: [str]) -> [[str]]:
        """ 
        The brute force solution is to compare each string to every other string 
        O(N^2)
        
        To determine distance, we can assign each character to a numerical value within a hashmap
        {
            "a": 0,
            "b": 1,
            ...
            "z": 25 
        }
        1) you would check only the strings that have the same length, since we can only shift characters and not add/remove them
        from a given string.
        2) abc bcd
        a -> b is one character apart
        b -> c is one character apart
        c -> d is one character apart

        so this is valid
        abc xyz
        a -> x  23 characters
        b -> y  23 characters
        c -> z  23 characters

        also valid
        
        az ba
        note that in this case a -> b is one distance,
        z -> a is also one distance, but it rotates around. So in order to compare the relative distance
        where in value1 -> value2, map[value1] > map[value2],
        you can perform map[value1] - 26, i.e where z: 25, 25 - 26 = -1, and you compare -1 to 0

        Midway through the problem, I realized its difficult group strings like this,
        since if the distances between two strings aren't the same, how would this case be grouped?

        for example,
        "abc", "aaa", these are not in the same group. Would I determine to split off a new group for ones that are in the same
        shift group as "abc", and another for "aaa"?

        Optimization:

        I'm thinking if its easier to check the distance between each of the characters
        on individual strings instead, as long as the len(str) > 1

        "abc" has a distance of 1 between each character, like so: 11,
        so any string that has this shift pattern, like
        "bcd", "xyz", where the distance between each character is 1, will match.

        "aca" has a distance pattern like so a -> c is 2 chars, c->a is also two characters, 22,
        and then group the strings based on this pattern

        "az" has a distance of 25
        "ba" also has a distance of 25 too, since we're going backwards

        so we still need to apply the logic of subtracting by 26 first if value1 > value2

        This version:
        O(N*M) Time, where N is the size of the list, and M is the length of each word in the list 
        O(N) Space

        """

        from collections import defaultdict
        letters = {}
        chars = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(chars)):
            letters[chars[i]] = i

        def getShiftPattern(s1):
            # compare the distance between each character of the string
            shift = []
            for i in range(1, len(s1)):
                cur = letters[s1[i]]
                prev = letters[s1[i-1]]
                # note that if we're looping back around
                # i.e b -> a, or z -> a, where the first value is greater than the second,
                # we do (prev - 26) first, since b -> a, we technically do 25 more shifts
                # to get all the way back to a
                shift.append(abs(prev-26-cur) if prev > cur else abs(cur-prev))
            return tuple(shift)

        grouped = defaultdict(list)
        for i in range(len(strList)):
            shiftPattern = getShiftPattern(strList[i])
            grouped[shiftPattern].append(strList[i])
        # convert to nested list
        return [value for value in grouped.values()]


if __name__ == "__main__":
    s = Solution()
    print(s.groupShiftedStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    
