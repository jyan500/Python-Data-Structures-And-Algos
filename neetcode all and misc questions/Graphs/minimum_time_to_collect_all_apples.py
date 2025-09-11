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
        """
        Time: O(N)
        Space: O(N)
        Revisited 8/11/2025
        https://neetcode.io/solutions/minimum-time-to-collect-all-apples-in-a-tree
        this is a graph problem, 
        create an adjacency list of the undirected graph,
        tracks the node and a list
        of edges and edge to node.
        then start a DFS at root 0

        the key here is recognizing when we're in a subtree with an apple in it.
        Since when we traverse the graph, we'll eventually get to a point in the DFS where we find an apple.
        Then when we return back up the tree, how do we know that we actually found an apple?

        The answer to this is that when we traverse the neighbors, if the neighbor has an apple, we know we'd
        need to add 2 to the amount of steps, and then pass that along
        Along with this, if in a previous call, if it returns an amount of steps that's greater than 0,
        we need to add the total amount of steps so far, plus an additional 2 to show that we went down and back up
        this node.

        
        """
        adjacency = {}
        for i in range(n):
            adjacency[i] = []
        for node, edge in edges:
            adjacency[node].append(edge)
            adjacency[edge].append(node)

        def dfs(node, prev):
            steps = 0
            for neighbor in adjacency[node]:
                if neighbor == prev:
                    continue
                amt = dfs(neighbor, node)
                if amt or hasApple[neighbor]:
                    steps += (amt + 2)
            return steps
        return dfs(0, -1)


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


        