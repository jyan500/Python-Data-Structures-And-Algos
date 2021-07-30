'''
Description
Given a string s and a list of strings dict, you need to add a closed pair of bold tag and to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. 
Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

https://www.lintcode.com/problem/1127/ (this is a leetcode premium problem)

Concept: 
https://www.youtube.com/watch?v=4JPKLcpggCE&ab_channel=HappyCoding

create a boolean array that is the same length as the string s 
we also want a variable called cur_end, which represents the index at which every index
before will need to be marked as bold (True in our array)
as we iterate through the string, we want to check if the word in the dict
is a prefix of the string starting at index i (using startswith built-in method)

An example of how startswith works:
text = 'Python programming is easy'
result = text.startswith('programming is', 7)

result should return true, because the substring starting at index 7 is:
programming is easy, so 'programming is' would be a proper prefix


'''

"""
@param s: a string
@param dict: a list of strings
@return: return a string
"""
def addBoldTag(s: str, word_dict: [str]) -> str:
    # write your code here
	'''
	concept:

	'''
	flag = [False] * len(s)

	cur_end = 0
	for i in range(len(s)):
		for w in word_dict:
			## if w is a prefix of the substring of s starting at i 
			if (s.startswith(w, i)):
				## update the cur end to be the max of the current end  and the length of the word (in word dict) + the current
				## value of i
				## its len(w) + i
				cur_end = max(cur_end, i+len(w))
		is_bold = i < cur_end
		flag[i] = is_bold

	res = ''
	for i in range(len(s)):
		if flag[i] and (i == 0 or (i > 0 and not flag[i-1])):
			res += '<b>'
		res+=s[i]
		if flag[i] and (i == n - 1 or (i < n-1 and not flag[i+1])):
			res += '</b>'
	return res



s1 = "aaabbcc"
d1 = ["aaa","aab","bc"]

print(addBoldTag(s1,d1))




    

