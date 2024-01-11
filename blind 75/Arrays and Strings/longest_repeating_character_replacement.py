'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

https://leetcode.com/problems/longest-repeating-character-replacement/
https://www.youtube.com/watch?v=gqXU1UyA8pk&ab_channel=NeetCode
'''

class Solution2:
    """
    Revisited 7/7/2023
    Concepts:
    https://www.youtube.com/watch?v=gqXU1UyA8pk&ab_channel=NeetCode
    1) sliding window by tracking left and right pointer
       right pointer increments to create window
    2) keep track of a dict to get the max amount of characters that need to be replaced
    3) window size - max amt of characters gives us the amount of characters that needs to be replaced in this window
       if this value exceeds k, we need to shrink the window by incrementing the left pointer, 
       which also decreases the character amount in our dict
    4) we also need another boolean (updatedRight) so that in the case the left side is updated,
       we don't increment the count of the character that the right pointer is pointing to unnecessarily
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        left = 0
        right = 0
        longest = 1
        updatedRight = True
        while (left < len(s) and right < len(s) and left <= right):
            windowSize = right - left + 1
            if updatedRight:
                if s[right] in count:
                    count[s[right]] += 1
                else:
                    count[s[right]] = 1
            
            greatestAmtChars = max(count.values())
            numReplacements = windowSize - greatestAmtChars
            if numReplacements <= k:
                right += 1
                longest = max(longest, windowSize)
                updatedRight = True
            else:
                count[s[left]] -= 1
                left += 1
                updatedRight = False
        return longest
                

class Solution:
    ## Using the O(26N) solution, where the "26" is searching
    ## all possible 26 capital letters within count to find the most frequently occuring
    ## char in our window, but still linear since we're only iterating over the string once
    ## explanation here, solution not the same, but similar to https://www.youtube.com/watch?v=gqXU1UyA8pk&ab_channel=NeetCode
    def characterReplacement(self, s: str, k: int) -> int:
        ## keep a count of all the characters we've seen so far within our window
        count = dict()
        ## keep a sliding window to keep track of the length of the substring
        left_ptr = 0
        right_ptr = 0
        max_so_far = 0
        updated_right_ptr = True
        while (left_ptr < len(s) and right_ptr < len(s) and left_ptr <= right_ptr):
            window_size = right_ptr - left_ptr + 1
            ## make sure that we don't repeat-count a character in case
            ## the right ptr was not updated (in that case, the left pointer was updated)
            if (updated_right_ptr):
                char = s[right_ptr]
                if (count.get(char) != None):
                    count[char] += 1
                else:
                    count[char] = 1
            most_amount_of_chars = ''
            ## find the character that occurs the most within our current window
            ## most_frequent_char_amount = 0
            ## replaced the loop with max of the count dict's values
            most_frequent_char_amount = max(count.values())
            # for key in count:
            #     most_frequent_char_amount = max(most_frequent_char_amount, count[key])
            
            ## the amount of replacements that we need to make will be equal
            ## to the window size subtract the amount of the most frequently occuring character
            ## since we'll want to do the least amount of replacements
            
            amount_of_replacements = window_size - most_frequent_char_amount
            # print('count: ', count)
            # print('window_size: ', window_size)
            # print('most_frequent_char_amount: ', most_frequent_char_amount)
            # print('amount_of_replacements: ', amount_of_replacements)
            if (amount_of_replacements <= k):
                max_so_far = max(max_so_far, window_size)
                right_ptr += 1
                updated_right_ptr = True
            else:
                ## shift the left pointer by one
                ## since we are essentially removing a character from the window,
                ## decrement the count as well
                char = s[left_ptr]
                if (char in count):
                    count[char] -= 1
                left_ptr += 1
                updated_right_ptr = False
                
        return max_so_far
                
            