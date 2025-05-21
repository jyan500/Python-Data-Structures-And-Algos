"""
https://www.youtube.com/watch?v=cw826XIOZIg&ab_channel=CodingwithMinmer

# this is a variation of "random pick with weight" that's commonly
asked by Meta.

You are conducting an A/B test and need to randomly pick a person
from across multiple cities. Each city has a known population,
and you need to ensure that the probability of choosing a user
from each city is proportional to the city's population.

You are given a 0-indexed array of pairs `city_populations`,
where each pair consists of a string representing the name of the 
`ith` city, and an integer representing the population of the `ith`
city (in millions, but treat these values as if in ones for computation 
purposes).

You need to implement the function `pickIndex()`, which randomly
picks a person in a city, and returns the name of the city
the person is in.

Example 1:
["Solution", "pickIndex", "pickIndex"]
[[["Seattle", 500], ["New York", 900], ["Los Angeles", 400]], [], []]
Output:
[null, "New York", "Los Angeles"]

Explanation
Solution solution = new Solution([["Seattle", 500"], ["New York", 900], ["Los Angeles", 400"]])
solution.pickIndex(); // return "New York". It is returning
the second element (index = 1) that has a probability of 900/(500+900+400)
"""

"""
The main difference between this problem and the original "random pick with weight" problem
is that the data is now in pairs. So within each pair, pair[1] (the "weight") corresponds to the population, and the 
"person" represents the index within the weights array.

w = [["Seattle", 500], ["New York", 900"], ["Los Angeles", 400]]

total of 500 + 900 + 400 = 1800
500/1800 chance of picking someone in seattle
900/1800 chance of picking someone in new york
400/1800 chance of picking someone in LA

We can still approach the problem in the same manner, but we need to save the cities that correspond
to each index

cities = ["Seattle", "New York", "Los Angeles"]
populations = [500, 900, 400]

We can then apply the prefix sum on the populations

populations = [500, 1400, 1800]

we can roll a number between 1 and 1800, and then determine the range where this number
falls under using binary search

(see random pick with weight)

"""
class Solution:
	def __init__(self, weights: [int]):
		self.cities = [weight[0] for weight in weights]
		self.weights = [weight[1] for weight in weights]
		self.prefix = [0] * len(self.weights)
		self.prefix[0] = self.weights[0]
		for i in range(1, len(self.weights)):
			self.prefix[i] = self.prefix[i-1] + self.weights[i]

	def pickIndex(self): 	
		from random import randint
		pick = randint(1, self.prefix[-1])
		def binarySearch(l, r):
			if l > r:
				return l
			mid = l + (r-l)//2
			if pick > self.prefix[mid]:
				return binarySearch(mid+1, r)
			else:
				return binarySearch(l, mid-1)

		index = binarySearch(0, len(self.prefix)-1)
		return self.cities[index]

if __name__ == "__main__":
	solution = Solution([["Seattle", 500], ["New York", 900], ["Los Angeles", 400]])
	print(solution.pickIndex())
	print(solution.pickIndex())
	print(solution.pickIndex())
	print(solution.pickIndex())
