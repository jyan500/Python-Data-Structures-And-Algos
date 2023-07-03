"""
Find the Celebrity
https://www.lintcode.com/problem/645/
(leetcode premium)

The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

# sample "knows" method implementation
class Celebrity:
	def __init__(self, n):
		self.index = n
	def knows(self, a, b):
		print(f'{a}, {b}')
		print("b == index", b == self.index)
		return b == self.index

class Solution:
	# @param {int} n a party with n people
	# @return {int} the celebrity's label or -1
	def __init__(self, celebrity, n):
		self.celebrity = celebrity
		self.n = n

	# brute force O(N^2) time, O(N^2) space
	def findCelebrity(self):
		# Write your code here
		knows = dict()
		adjacencyList = dict()
		for i in range(self.n):
			adjacencyList[i] = [j for j in range(0, i)] + [j for j in range(i+1, self.n)]
			knows[i] = False
		for key in adjacencyList:
			for node in adjacencyList[key]:
				knows[node] = self.celebrity.knows(key, node)
		for key in knows:
			if knows[key]:
				return True
		return -1

	# optimal solution O(N) time, O(1) space
	def findCelebrityOptimal(self):
		"""
		Important point:
		knows(a, b) tells us two things:
		1) if a knows b, b could be a potential celebrity
		2) if a does not know b, b cannot be a celebrity because the celebrity must be known by everyone

		In the problem statement, there can only be either one celebrity or no celebrity at the party,
		so we can find a potential candidate by looping through all candidates,
		and then keeping track of one variable to see if knows(a, b) returns true, where a is the potential celebrity

		We also know that the celebrity cannot know anyone at the party, so if once we 
		find a potential candidate that is known by everyone, 
		we can see if that candidate does not know everyone else in a second for loop by running
		knows(a, b), where a is the potential celebrity and b is everyone else

		"""
		candidate = 0
		for i in range(1, self.n):
			# if a knows b, that means b could be a potential candidate
			# so we update potential to be the current index. 
			# this also means once we find a candidate, we'd expect that candidate
			# to not know anyone either
			if self.celebrity.knows(candidate, i):
				candidate = i

		# check whether the potential candidate knows anyone, or if someone does not know the candidate,
		# they cannot be the celebrity
		# if that's the case
		for i in range(self.n):
			# ignore the case where the candidate index is the same as i
			if candidate == i:
				continue
			if self.celebrity.knows(candidate, i) or not self.celebrity.knows(i, candidate):
				return -1
		return candidate

# test case #1
c = Celebrity(1)
s = Solution(c, 3)
print(s.findCelebrity())

# test case #2
c1 = Celebrity(-1)
s1 = Solution(c1, 3)
print(s1.findCelebrity())

c = Celebrity(1)
s = Solution(c, 3)
print(s.findCelebrityOptimal())

# test case #2
c1 = Celebrity(-1)
s1 = Solution(c1, 3)
print(s1.findCelebrityOptimal())


