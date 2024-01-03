"""
https://www.youtube.com/watch?v=Xdt5Z583auM&t=16s&ab_channel=NeetCodeIO
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/submissions/
Time Complexity: O(N)
Space Complexity: O(N)

Concepts:
1) Although listed as a tree problem, it's a really an undirected graph problem, so the first step is 
creating the adjacency list, where you add both the node and it's edge to the adjacency list
2) We start at node 0 and perform DFS, checking whether the node is an apple or not based on whether hasApple[node]
is True
3) The key realization is that within the DFS, whenever we get to a node that's apple, we know that it would've taken
at least 2 steps to get to that apple. Another is that given we're at a node P, whenever we visit the children nodes,
and at least one of the children nodes contained an apple,
the amount of steps taken would be the sum of all the steps needed to get to this point, PLUS an additional two,
since this node is also part of the path required to get to the apple nodes.
4) Also if we don't reach an apple node during our DFS, we would return 0

"""
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, adjacencyList, visited):
            steps = 0
            if node in adjacencyList:
                for neighbor in adjacencyList[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        neighborSteps = dfs(neighbor, adjacencyList, visited)
                        # if the node that we're visiting is an apple, OR
                        # the subtree that we visited has an apple, we add the amount of time taken
                        # PLUS an additional 2, since we travel through this node to reach the remainder of the subtree
                        if hasApple[neighbor] or neighborSteps > 0:
                            steps += neighborSteps + 2
            return steps

        adjacencyList = dict()

        for node, edge in edges:
            if node in adjacencyList:
                adjacencyList[node].append(edge)
            else:
                adjacencyList[node] = [edge]
                
            if edge in adjacencyList:
                adjacencyList[edge].append(node)
            else:
                adjacencyList[edge] = [node]
        return dfs(0, adjacencyList, set([0]))


        