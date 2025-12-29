"""
This is a modification of the problem "Top K frequent words", where
in the case there are ties, you need to return all elements from that frequency group

For example:

parameters:
input = ["abc", "abc", "dbc", "dbc", "jet", "abd", "abd", "abd"]
k = 2

output:
["abd", "abc", "dbc"]

the reasoning is because "abd" is the top 1 most frequent element since it has a
frequency of 3,
and then for the top 2, both "abc" and "dbc" would be considered because
they both have a frequency of 2, so we need to include both "abc" and "dbc"

My proposed solution would be to take the normal approach of using a Counter
to map the word to its frequency, and then using a heap and popping out k times, 
but modify it slightly where you create a reverse lookup, so now you're mapping
the frequency to a set of words that have that frequency.

When popping out of the heap, get the frequency and look up in the reverse lookup
table to get the values that have that frequency, and add to the result array.

"""
import heapq
from collections import Counter

def topKFrequentWithTies(arr, k):
	heap = []
	c = Counter(arr)
	reverseLookup = {}
	for key,value in c.items():
		if value in reverseLookup:
			reverseLookup[value].add(key)
		else:
			reverseLookup[value] = set([key])

		# also add into the heap at the same time
		heapq.heappush(heap, (-value, key))

	res = []
	for i in range(k):
		freq, _ = heapq.heappop(heap)
		elements = reverseLookup[-freq]
		res.extend(list(elements))

	return res

print(topKFrequentWithTies(["abc", "abc", "dbc", "dbc", "jet", "abd", "abd", "abd"], 2))