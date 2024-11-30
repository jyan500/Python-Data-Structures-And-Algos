"""
https://www.lintcode.com/problem/637/description
Approach:
This assumes that the word only has alphabetical characters in it, and that abbreviation
can have alphanumeric chars, and that the numbers can be greater than one digit.

1. First find the numbers in the abbreviation string, where the numbers can be more than 1 digit,
	so once the first digit is found, run a while loop that continually adds a number to the current until 
	it's no longer a number
2. Track three pointers, one for the word, one for the abbreviation, and one for the list of numbers that we
parsed out of abbreviation (call it parsed numbers list)
3. while our left and right pointers are less than the length of word
	if the characters between word and abbr are the same
		increment both pointers
	else:
		if we still have numbers available
			increment the right pointer such that it passes over the digits to the next non numeric char
			increment the left pointer such that it skips over the specified amount of indices based on the current number in parsed number list
			increment the pointer that represents the current value of the parsed numbers list
		else
			break, because we have a case where the abbreviation number and character in word does not line up
4. In the end, we track whether the two pointers are equal to the length of the word - 1 and length of abbr - 1 respectively,
OR l == len(word) and r == len(abbr), due to an edge case like so:

"a"
1

where if we ran the algorithm, it'd result in the two pointers with value 1, which is the same as the length of the string.
This is because the last (and only character) of the abbreviation was a number, and it does abbreviate "a"

Time: O(N)
"""
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        curr = ""
        nums = []
        i = 0 
        while (i < len(abbr)):
            curr = ""
            while (i < len(abbr) and abbr[i].isnumeric()):
                curr += abbr[i]
                i += 1
            if curr != "":
                nums.append(int(curr))
            i += 1
        l = 0 
        r = 0
        k = 0
        while (l < len(word) and r < len(abbr)):
            if word[l] == abbr[r]:
                l += 1
                r += 1
            else:
                # pass over the numbers to the next non-numeric character
                if (k < len(nums)):
                    r += (len(str(nums[k])))
                    l += nums[k]
                    k += 1
                else:
                    break
        return (l == len(word)-1 and r == len(abbr) - 1) or (l == len(word) and r == len(abbr))
