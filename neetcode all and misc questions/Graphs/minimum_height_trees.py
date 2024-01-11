"""
https://leetcode.com/problems/minimum-height-trees/
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Optimal Solution:
        https://leetcode.com/problems/minimum-height-trees/solution/
        Short Summary:
        1) An important observation to make this is that in a graph with no cycles,
        there can only be up to TWO nodes in the final answer, because we're looking
        for nodes that have the most connections, known as "centroids", see the diagram
        in the post
        2) If we're only looking for two nodes that have the most connections, we can start
        by looking at all the "leaf" nodes that only have one connection and then trimming
        those away
        3) By using BFS and then visiting the trimmed neighbor, 
        we continue trimming until we find the centroids

        Time Complexity:
        O(V), where V is the amount of vertices in the graph
        Space Complexity:
        O(V) to form the adjacency list
        """

        # edge case, if there's less than or equal to two nodes in our graph
        # we return the amount of nodes since there can only be up to two
        # centroids in the graph
        if n <= 2:
            return [i for i in range(n)]
        
        # build adjacency list
        adjacencyList = dict()
        for i in range(n):
            adjacencyList[i] = set()
        for j in range(len(edges)):
            node, edge = edges[j]
            adjacencyList[node].add(edge)
            adjacencyList[edge].add(node)
            
        # initialize the first layer of leaves,
        # where a leaf should only have one neighbor
        leaves = []
        for i in range(n):
            if len(adjacencyList[i]) == 1:
                leaves.append(i)
        
        # Trim the leaves until reaching the centroids
        remainingNodes = n
        while remainingNodes > 2:
            # decrement the number of remaining nodes by number of leaves
            remainingNodes -= len(leaves)
            newLeaves = []
            while leaves:
                leaf = leaves.pop()
                # pop off the one neighbor of that leaf
                neighbor = adjacencyList[leaf].pop()
                # in our neighbor, remove the edge (which was the leaf) that we just removed
                adjacencyList[neighbor].remove(leaf)
                
                # for the neighbor, because we just trimmed off a leaf, this neighbor
                # could become a leaf itself, so we need to check for this
                if len(adjacencyList[neighbor]) == 1:
                    newLeaves.append(neighbor)
            
            # after one round of trimming, prepare for the next round 
            # of trimming by setting leaves = newLeaves
            leaves = newLeaves
        
        # The remaining 1 (or 2) nodes left are the centroids, which is the final answer
        return leaves
                
                
        """
        I think this is saying that given a root,
        you construct the tree from that root
        and then see what the maximum distance is to get from the root
        to one of the nodes in the graph, and then we check all the possible
        configurations, and see which one has the smallest distance required
        
        BFS seems like a good candidate to solve this problem, the amount of iterations
        it takes for BFS to complete should indicate the height of the tree
        
        Brute Force would be to repeat this process on every root:
        O((N+M) * N), repeating BFS for the number of nodes
        
        """
        # create adjacency list for undirected graph, so
        # node -> edge, edge -> node
        # adjacencyList = dict()
        # for i in range(n):
        #     adjacencyList[i] = []
        # for j in range(len(edges)):
        #     node, edge = edges[j]
        #     adjacencyList[node].append(edge)
        #     adjacencyList[edge].append(node)
    
        
#         def bfs(node):
#             from collections import deque
#             q = deque()
#             q.append(node)
#             visited = set()
#             visited.add(node)
#             height = 0 
#             while(q):
#                 for i in range(len(q)):
#                     cur = q.popleft()
#                     for neighbor in adjacencyList[cur]:
#                         if neighbor not in visited:
#                             q.append(neighbor)
#                             visited.add(neighbor)
#                 height += 1
#             return height
        
#         heights = dict()
#         minHeight = float("inf")
#         for node in adjacencyList:
#             height = bfs(node)
#             minHeight = min(height, minHeight)
#             if height in heights:
#                 heights[height].append(node)
#             else:
#                 heights[height] = [node]
#         return heights[minHeight]
        
       