'''

https://leetcode.com/problems/verifying-an-alien-dictionary/

My initial approach (passes all test cases):
Write a custom string class with overriding comparators
where the less than and greater than will compare using the order that we passed in 

it will compare the characters of each string based on the value of the index in the order string
for example,
words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"

in the order string world should come before word since "l" comes before "d" in the order string
therefore, in our __lt__ method, the index of "l" (3) comes before "d" (4), so "world" should be less
than "word"

we then convert each of the strings into the customString class and store it into a list
iterate through this list of customString starting from the second word, if the previous customString is greater
than the current, then its not in sorted order. Else we can just return True

time complexity: I'm not sure if this is O(N) or O(N^2), since for each comparison that the sorting makes
it will iterate through the strings to compare the indexing via the order
space complexity: O(N) to store the custom list of strings


Another solution by Timothy Chang:
https://www.youtube.com/watch?v=FFJVrXtqepo&ab_channel=TimothyHChang

The idea behind his approach is to create a lookup dictinary, mapping the character within the order string
to its index

then, he converts each word into a list of its corresponding indices found on the order string, by mapping
each character of the word to the key on the lookup dictionary

after that, he iterates through the list of corresponding indices starting from the second item, and checking
if the previous list of indices is less than the current list of indices

This approach is O(N^2), because it takes O(N) to loop through the initial words list and another O(N)
to loop through each word within the words list, but the good news is that it only happens once

And an additional O(N) space for the lookup and words2 temp variable
'''
class customString:
    def __init__(self, s, order):
        self.s = s
        self.order = order
    def __repr__(self):
        return self.s
    def __lt__(self, s1):
        i = 0
        while (i < len(self.s) and i < len(s1.s)):
            s_index = self.order.index(self.s[i])
            s1_index = self.order.index(s1.s[i])
            i+=1
            if (s1_index < s_index):
                return False
            elif (s1_index > s_index):
                return True
            else:
                
                continue
        if (len(self.s) < len(s1.s)):
            return True
        elif (len(self.s) > len(s1.s)):
            return False
        else:
            return 0
            
        return 0
    def __gt__(self, s1):
        i = 0
        while (i < len(self.s) and i < len(s1.s)):
            s_index = self.order.index(self.s[i])
            s1_index = self.order.index(s1.s[i])
            i+=1
            if (s1_index < s_index):
                return True
            elif (s1_index > s_index):
                return False
            else:
                continue
        if (len(self.s) < len(s1.s)):
            return False
        elif (len(self.s) > len(s1.s)):
            return True
        else:
            return 0
    
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        s = customString(words[0], order)
        s1 = customString(words[1], order)
        s_list = []
        s2_list = []
        for i in range(len(words)):
            s_list.append(customString(words[i], order))
        ## print(s_list)
        s_list = sorted(s_list)
        for i in range(len(s_list)):
            s2_list.append(s_list[i].s)
        return s2_list == words

    ## Tim chang's solution
    def isAlienSortedAlternate(self, words: List[str], order: str) -> bool:
    	lookup = dict()
    	for i in range(len(order)):
    		lookup[order[i]] = i
    	words2 = []
    	for i in range(len(words)):
    		word = []
    		for j in range(len(words[i])):
    			word.append(lookup[j])
    		words2.append(word)

    	for k in range(1,len(words2)):
    		if (words2[i-1] > words2[i]):
    			return False
    	return True
        