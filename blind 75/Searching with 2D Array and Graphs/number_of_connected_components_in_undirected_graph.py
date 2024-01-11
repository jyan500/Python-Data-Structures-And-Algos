"""
Leetcode Premium
https://leetcode.ca/all/323.html

Union Find Explanations:
https://www.youtube.com/watch?v=ymxPZk7TesQ&ab_channel=MichaelMuinos
https://www.youtube.com/watch?v=8f1XPm4WOUc&t=2s&ab_channel=NeetCode

Neetcode suggests checking out problem 547 (number of provinces) for a 
non-premium union find problem
"""

"""
Union Find Solution From Michael Muinos
(Translated from Java)

Time Complexity: O(N + M*Log(N)), where M is the number of edges and N is the number of nodes, using the 
find function to perform path compression

Without the path compression, it'd be closer to O(N * M)
"""
class Solution3:
	def __init__(self):
		pass

	def numConnectedComponents(self, n: int, edges: [[int, int]]) -> int:

		# find the parent of edge 1
		# find the parent of edge 2
		# assign one of the edges as the parent of the other, which merges
		# the two subsets
		def union(edge1: int, edge2: int, ids: [int]):
			parent1 = find(edge1, ids)
			parent2 = find(edge2, ids)
			ids[parent1] = parent2

		# if the edge we're looking at is not the parent, 
		# it will recur and continue to look for the parent and reassign the edge
		# to the parent 
		# a parent is when the index is equal to the value at that index
		def find(edge: int, ids: [int]):
			if ids[edge] != edge:
				ids[edge] = find(ids[edge], ids)
			return ids[edge]

		# initially, point all nodes to themselves as individual subsets
		ids = [i for i in range(n)]

		# union the subsets together
		for edge in edges:
			e1, e2 = edge
			union(e1, e2, ids)

		# count the amount of unique parents that we have
		parentSet = set()
		for i in range(len(ids)):
			parentSet.add(find(i, ids))

		# this will result in the number of connected components, which is our answer
		return len(parentSet)

"""
Union Find Solution from Neetcode (Optimized w/ Rank):
1) The idea is that you start out with n number of individual components without knowing
which ones are connected, you assume that the node n is connected to itself
2) As you iterate, you figure out which components are connected based on the edges, and then decrement 
the total number n 

As an optimization, we have a "rank" array to keep track of the size of the connected component
we merge the smaller "ranked" component to the larger ranked one

Time Complexity: O(N + M * amortized(LogN)), which is closer to O(N + M)
"""

class Solution2:
	def __init__(self):
		pass

	def numConnectedComponents(self, n: int, edges: [[int, int]]) -> int:
		# parent array, holds each node in the graph, 0 ... n - 1,
		# which assumes each node is connected to itself
		parent = [i for i in range(n)]
		rank = [1] * n 

		def find(n1):
			result = n1
			while result != parent[result]:
				parent[result] = parent[parent[result]]
				result = parent[result]
			return result

		def union(n1, n2):
			p1, p2 = find(n1), find(n2)

			if p1 == p2:
				return 0

			if rank[p2] > rank[p1]:
				parent[p1] = p2
				rank[p2] += rank[p1]
			else:
				parent[p2] = p1
				rank[p1] += rank[p2]

			return 1

		result = n
		for n1, n2 in edges:
			result -= union(n1, n2)

		return result

""" 
DFS Solution:
1) Create adjacency list with node as an edge and vice versa
2) Run a DFS on each node 0 ... n - 1, keeping track of visited, as well
as a visited list for that specific call to DFS
3) Check to see if the node has already been visited, if so don't add it to the
visited list for this call to DFS
4) At the end, check whether we visited any new nodes, if so increment our count + 1,
this means we've visited all nodes that can be visited from this starting node i,
which is one connected component

Time: O(E + V), where E is the number of edges, and V is the number of vertices
Space: O(E + V), for the adjacency list 
"""
class Solution:
	def __init__(self):
		pass

	def numConnectedComponents(self, n: int, edges: [[int, int]]) -> int:
		# create adjacency list
		adjacencyList = dict()
		for i in range(n):
			adjacencyList[i] = []
		# because this is an undirected graph, 
		# we need to add the nodes as edges and vice versa
		for i in range(len(edges)):
			node, edge = edges[i]
			adjacencyList[node].append(edge)
			adjacencyList[edge].append(node)

		visited = set()
		count = 0
		def dfs(node, newVisited):
			if node not in visited:
				visited.add(node)
				newVisited.append(node)
			for edge in adjacencyList[node]:
				if edge not in visited:
					dfs(edge, newVisited)

			return newVisited

		for i in range(n):
			newVisited = dfs(i, [])
			if len(newVisited) > 0:
				count += 1
		return count

s = Solution()

# expect 2 as the output
print(s.numConnectedComponents(5, [
	[0, 1], 
	[1, 2], 
	[3, 4]
]))
# expect 1 as the output
print(s.numConnectedComponents(5, [
	[0, 1], 
	[1, 2], 
	[2, 3], 
	[3, 4]
]))
# expect 5 as the output
print(s.numConnectedComponents(5, []))

s2 = Solution2()

# expect 2 as the output
print(s2.numConnectedComponents(5, [
	[0, 1], 
	[1, 2], 
	[3, 4]
]))
# expect 1 as the output
print(s2.numConnectedComponents(5, [
	[0, 1], 
	[1, 2], 
	[2, 3], 
	[3, 4]
]))
# expect 5 as the output
print(s2.numConnectedComponents(5, []))

s3 = Solution3()

# expect 2 as the output
print(s3.numConnectedComponents(5, [
	[0, 1], 
	[1, 2], 
	[3, 4]
]))
# expect 1 as the output
print(s3.numConnectedComponents(5, [
	[0, 1], 
	[1, 2], 
	[2, 3], 
	[3, 4]
]))
# expect 5 as the output
print(s3.numConnectedComponents(5, []))
