"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 10 
Explanation: Four 1's at depth 2, one 2 at depth 1.
Example 2:

Input: [1,[4,[6]]]
Output: 27 
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.

Leetcode #339 (Premium)

-------------------------------

Approach:
1) Use recursion where we initially iterate through the parameter list cur
	intSum = 0
	fromList = 0
	loop through the cur:
		if the type(cur) is a list,
			recur down this list, passing in the current element and depth + 1, to show
			that the depth has increased, and add the result of the recursion to fromList
		else:
			add the current number element to intSum 

	return (intSum * depth) + fromList 

2) Note that you have to separate out the result from the sum of the nested list of integers,
vs the integers at this current list depth, since only the sum of the integers at the current list depth
are multiplied by the current depth.

Time: O(N^N)
Space: O(N)

"""

class Solution:
	def nestedListWeightSum(self, intList: [[int]]) -> int:
		def search(cur, depth):
			# separate out the result of the sum of the list
			# and the sum of the integers at this current depth, as only the sum of the integers
			# is multiplied by depth
			intSum = 0
			fromList = 0
			for i in range(len(cur)):
				if type(cur[i]) == list:
					# if the element is a list, pass the list down to the next recursive call,
					# and increase depth by 1
					fromList += search(cur[i], depth+1)
				else:
					intSum += cur[i] 
			return (intSum * depth) + fromList
		# starts at depth of 1 since the parameter is a list
		return search(intList, 1)

s = Solution()
print("****** #1 ******")
print(s.nestedListWeightSum([[1,1],2,[1,1]]))
assert s.nestedListWeightSum([[1,1],2,[1,1]]) == 10
print("****** #2 ******")
print(s.nestedListWeightSum([1,[4,[6]]]))
assert s.nestedListWeightSum([1,[4,[6]]]) == 27
print("****** #3 ******")
print(s.nestedListWeightSum([]))
assert s.nestedListWeightSum([]) == 0