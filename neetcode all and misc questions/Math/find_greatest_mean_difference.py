"""
Note this is NOT a leetcode question, but does involve math, and seems like it could be a good question.
It came up while trying to manually calculate this during handshake AI training task
"""
class Solution:
	def find_greatest_mean_difference(self, numbers: [int]):
		"""
		1) must partition into two groups that have the same median 
		2) Find the mean for both groups, then calculate the mean difference
		3) Save the recursive result as the mean difference, until finding the greatest
		"""	
		N = len(numbers)
		numbers.sort()
		self.greatest = float("-inf")
		self.greatest1 = []
		self.greatest2 = []
		def find_median(group: [int]) -> float:
			group.sort()
			mid = len(group) // 2
			if len(group) % 2 == 0:
				return (group[mid] + group[mid-1])/2
			return group[mid]

		def find_mean(group: [int]) -> float:
			return sum(group)/len(group)

		def dfs(i: int, group1: [int], group2: [int]) -> None:
			# start with two empty groups
			if i == N:
				if len(group1) > 0 and len(group2) > 0:
					if find_median(group1) == find_median(group2):
						mean1 = find_mean(group1)
						mean2 = find_mean(group2)
						if (abs(mean1-mean2) > self.greatest):
							self.greatest = abs(mean1-mean2)
							self.greatest1 = group1
							self.greatest2 = group2
				return 
			# try adding into group1 first, then group 2
			dfs(i+1, group1 + [numbers[i]], group2)
			dfs(i+1, group1, group2 + [numbers[i]])

		dfs(0, [], [])
		return [self.greatest, self.greatest1, self.greatest2]

if __name__ == "__main__":
	"""
	79%, 83%, 83%} and {80%, 80%, 80%, 83%, 87%, 87%, 89%
	"""
	s = Solution()
	print("test case [79, 80, 80, 80, 83, 83, 83, 87, 87, 89]")
	ans, combo1, combo2 = s.find_greatest_mean_difference([79, 80, 80, 80, 83, 83, 83, 87, 87, 89])
	print("ans: ", ans)
	print("combo1: ", combo1)
	print("combo2: ", combo2)

	print("test case [79,80,80,80,83,83,87,89]")
	ans, combo1, combo2 = s.find_greatest_mean_difference([79,80,80,80,83,83,87,89])	
	print("ans: ", ans)
	print("combo1: ", combo1)
	print("combo2: ", combo2)

	print("test case [79,80,80,80,83,83,84,87,87,89]")
	ans, combo1, combo2 = s.find_greatest_mean_difference([79,80,80,80,83,83,84,87,87,89])	
	print("ans: ", ans)
	print("combo1: ", combo1)
	print("combo2: ", combo2)

	print("test case [85, 85, 85, 86, 86, 87, 87, 87]")
	ans, combo1, combo2 = s.find_greatest_mean_difference([85, 85, 85, 86, 86, 87, 87, 87])	
	print("ans: ", ans)
	print("combo1: ", combo1)
	print("combo2: ", combo2)

	print("test case [71,72,72,73,81,82,82,82,85,85,85,86,86]")
	ans, combo1, combo2 = s.find_greatest_mean_difference([71,72,72,73,81,82,82,82,85,85,85,86,86])	
	print("ans: ", ans)
	print("combo1: ", combo1)
	print("combo2: ", combo2)


