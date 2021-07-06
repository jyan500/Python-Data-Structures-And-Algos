'''
https://leetcode.com/problems/clone-graph/
https://www.youtube.com/watch?v=mQeF6bN8hMk&ab_channel=NeetCode
(using Depth First Search)
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
	## My first approach used breadth first search to go through the neighbors, and at
	## the same time, build up an adjacency list based on the neighbors of the original graph
    def cloneGraph(self, node: 'Node') -> 'Node':
        ## using this example of a graph with four nodes (1,2,3,4)
        ## connected like a rectangle
        ## BFS problem?
        if (not node):
            return node
        queue = [node]
        visited = [node.val]
        node_map = dict()
        new_node = None
        while (queue):
            n = queue.pop()
            if (node_map.get(n.val) != None):
                new_node = node_map[n.val]
            else:
                new_node = Node()
                new_node.val = n.val
                node_map[new_node.val] = new_node
            print('current_node: ', new_node.val)
            ## check neighbors
            for i in range(len(n.neighbors)):
                print('neighbor: ', n.neighbors[i].val)
                if (node_map.get(n.neighbors[i].val) == None):
                    
                    neighbor = Node()
                    neighbor.val = n.neighbors[i].val
                    node_map[neighbor.val] = neighbor
                    ## print('adding neighbor: ', neighbor.val)
                    new_node.neighbors.append(neighbor)
                else:
                    neighbor = node_map[n.neighbors[i].val]
                    ## print('adjacency found, adding neighbor: ', neighbor.val)
                    new_node.neighbors.append(neighbor)
                    
                if (n.neighbors[i].val not in visited):
                    
                    visited.append(n.neighbors[i].val)
                    queue.append(n.neighbors[i])
        # for key in adjacency_list:
        #     print('node val: ', key, 'id: ', id(adjacency_list[key]))
        #     print('neighbors: ----------')
        #     for n_node in adjacency_list[key].neighbors:
        #         print('neighbor val: ', n_node.val, 'id: ', id(n_node))
        return node_map[1]
                
    ## much more efficient solution using DFS
    ## the idea is that we also create the hashmap but we map the original nodes as key,
    ## and the newly copied nodes as values
    ## so when doing the dfs, we create the new copy and map the original graph node to this new copy
    ## then, we iterate through the original graph node's neighbors and perform dfs
    ## at each call of the dfs function, it will return the new copy of itself,
    ## so the copy.neighbors.append(dfs(neighbor)) will be getting the neighbors for the copied node

    ## Time Compexity O(V+E), where v is the number of vertices and m is the number of edges, Space Complexity, O(V)
    ## storing each node in the dictionary
    def cloneGraph(self, node: 'Node') -> 'Node':
    	oldToNew = dict()
    	def dfs(node):
    		if node in oldToNew:
    			return oldToNew[node]
    		else:
    			copy = Node(node.val)
    			oldToNew[node] = copy
    			for neighbor in node.neighbors:
    				copy.neighbors.append(dfs(neighbor))
    			return copy
    	if (node):
    		return dfs(node)