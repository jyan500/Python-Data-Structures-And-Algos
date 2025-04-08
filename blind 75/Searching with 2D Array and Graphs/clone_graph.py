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
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Revisited 4/8/2025
        Revisited on 10/2/2024, tried for a DFS approach this time from Neetcode
        As we traverse the graph, we can create the graph copy at the same time
        start by creating a graph node with empty neighbors. 
        https://neetcode.io/problems/clone-graph
        IMPORTANT:
        I got stuck on this, but you need to use a hashmap that maps the old node to the new node,
        this is used instead of a "visited" set like normal DFS.
        This is important because this is an undirected graph, so if you're at a node,
        you would need to add the backwards relationship too. So if you go to a neighbor that we already
        visited for the backwards relationship, 
        we'd look this up in our hashmap, and see that the old node was already visited and cloned,
        then return the new Node.

        Time: O(E + V)
        Space: O(E + V)
        """
        self.oldToNew = {}
        def dfs(node):
            # important! if we're at the backwards relationship, we should've seen node already, 
            # so return the cloned new node and don't continue
            # to avoid an infinite loop
            if node in self.oldToNew:
                return self.oldToNew[node]
            root = Node(node.val)
            # note that when we update the neighbors, it should also update the reference
            # inside the self.oldToNew dict 
            self.oldToNew[node] = root
            neighbors = []
            for neighbor in node.neighbors:
                # each DFS will return the cloned node for each neighbor with all of its corresponding neighbors intact
                n = dfs(neighbor)
                neighbors.append(n)
            root.neighbors = neighbors
            return root
        
        return dfs(node)

"""
revisited on 7/19/2023
revisited on 11/15/2024 with the same solution
Used BFS again
Key concepts:
1) similar to a linked list problem, you need to track
a head and a current pointer that leads back to head.
whenever we "visit" a node that we just popped off,
we also need to set the current pointer to the node
that we just created (not the node that we popped off directly though
since we're creating new nodes and not setting them equal to the existing input node)

2) keep track of the nodes that we've already created using a dict with the 
key as the node value (since the problem states that these values are unique within the graph),
and the created node

3) as we traverse the graph using BFS, we should be able to create new nodes, and then 
in the following iteration, we can then set the neighbors for that node based 
on the neighbors list given for each existing node. If we've already created a node, we can
find it in our dict. This case will also account for the backwards relationship between nodes.


"""
class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        if not node:
            return None
        q = deque()
        q.append(node)
        visited = [node.val]
        # keep track of the head, which is what we'll be returning
        # similar to a linked list problem
        head = Node(node.val, neighbors = [])
        # keep track of the node that we've currently made
        cur = head
        createdNodes = dict({node.val: head})
        # perform a BFS through the existing graph
        while (len(q) != 0):
            n = q.popleft()
            # advance cur to the node that we're evaluating currently
            if n.val in createdNodes:
                cur = createdNodes[n.val]
            for neighbor in n.neighbors:
                if neighbor.val not in visited:
                    q.append(neighbor)
                    visited.append(neighbor.val)
                # if we haven't created the neighbor node, create it
                if neighbor.val not in createdNodes:
                    neighborNode = Node(neighbor.val, neighbors = [])
                    createdNodes[neighbor.val] = neighborNode
                # otherwise, retrieve node directly
                else:
                    neighborNode = createdNodes[neighbor.val]
                # add to the list of neighbors for the current node
                cur.neighbors.append(neighborNode)
        return head

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