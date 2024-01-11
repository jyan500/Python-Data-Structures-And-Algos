"""
LeetCode Premium
https://www.lintcode.com/problem/178/
https://www.youtube.com/watch?v=bXsUuownnoQ&ab_channel=NeetCode

Key concepts:
A valid tree is determined as follows:

1) all the nodes in the graph must be connected,
meaning they can all be visited
2) the graph cannot contain a cycle

Build an adjacency list, because this is an undirected graph,
we make sure that when we loop through and add an edge 
to a given node, we need to add the same relationship vice versa, where
our current node is considered an edge

i.e 0: [1], 1: [0]

starting from node 0 (we can start here because we know nodes will be from 0 ... n - 1),
perform DFS to check whether we can visit all nodes, and if any nodes form a cycle. 
We keep a visited set for cycle detection. 

Because the graph is undirected however, within our DFS when checking which nodes
to go to next, we pass in a previous node value (hence the prev), to avoid re-checking
a node we've already been to. 

At the end, dfs would've returned false if there was a cycle, so the last check
is to see if we actually visited all the nodes in the graph

Time Complexity:
O(E + V), where E is the number of edges and V is number of the vertices
Space Complexity:
O(E + V) memory

"""
from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque    
        adjacencyList = dict()
        visited = set()
        for i in range(n):
            adjacencyList[i] = []
        # create adjacency list for undirected graph where 
        # each edge is also a node
        for i in range(len(edges)):
            node, edge = edges[i]
            adjacencyList[node].append(edge)
            adjacencyList[edge].append(node)
        def dfs(node, prev):
        	# if node is in visited, this is a cycle
            if node in visited:
                return False
            visited.add(node)
            for edge in adjacencyList[node]:
            	# we keep track of prev so that we don't accidentally
            	# visit the same node twice, without interfering
            	# with our visited check
                if edge != prev:
                    if not dfs(edge, node):
                        return False
            return True

        # return true if we didn't find any cycles, and we were able to
        # visit all nodes
        # -1 is just a sentinel value for the previous value since 
        # we haven't visited any nodes yet, so there's no previous value
        return dfs(0, -1) and len(visited) == n
