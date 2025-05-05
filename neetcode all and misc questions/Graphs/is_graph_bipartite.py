'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

https://leetcode.com/problems/is-graph-bipartite/

BFS solution adapted from:
https://www.youtube.com/watch?v=FofydiwP5YQ&ab_channel=NideeshTerapalli
https://www.youtube.com/watch?v=CscLi1gVGUk&ab_channel=TimothyHChang
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Revisited 5/1/2024
        Revisited 11/15/2024
        Time: O(E+V)
        Space: O(V)
        Bi partite means that two adjacent nodes in the graph cannot have the same 
        "color"
        Theory:
        https://www.youtube.com/watch?v=bZBmN7I7GNQ&ab_channel=WrathofMath
        Neetcode Explanation:
        https://youtu.be/mev55LTubBY
        
        You're already given an adjacency list, where each node at index i within
        graph represents the neighbors of that node
        
            0       1       2       3
        [[1,2,3], [0,2], [0,1,3], [0,2]]
        
        0 --- 1 
        | \   |
        |   \ |
        3 --- 2
        
        you'd run BFS on each node, since there's no guarantee that
        the nodes are all connected.
        
        if you start at 0, you can color this edge "blue"
        then using BFS, you'd look at the immediate neighbors (which are 1, 3 and 2)
        and color these red
        
        at 1, we would not re-color 0 since we've already visited 0, but we would attempt to color the neighbor 2 to the opposite color ("blue"), but we see that 
        it's already the same color, so this is invalid.
        
          0      1     2     3       
        [[1,3],[0,2],[1,3],[0,2]]
        
        
        0 -- 1
        |    |
        3 -- 2
        
        at 0, we color this blue
        then the neighbors 1 and 3 would be colored red
        visiting 1, we would then try to color the neighbor blue, which is 2
        visiting 3, we would then try to color the neighbor blue, which is 2
        at 2, we already visited 1 and 3, so there's no more nodes to color
        
        
        """
        # the colors list acts as both a visited set and color indicator
        colors = [0] * len(graph)
        def bfs(node):
            # if we've already visited this node (since the graph is undirected),
            # return True
            if colors[node]:
                return True
            # color this node
            q = deque([node])
            colors[node] = -1
            while (q):
                n = q.popleft()
                for neighbor in graph[n]:
                    # if we've already visited this neighbor, AND 
                    # the neighbor is the same color as the current node,
                    # this is a conflict, as this means two adjacent nodes have the same color, return False
                    if colors[neighbor] and colors[neighbor] == colors[n]:
                        return False
                    # if we have not visited the neighbor
                    elif not colors[neighbor]:
                        # we set the color of the neighbor to be the "opposite" color
                        # of the current node, hence multiplying by -1
                        colors[neighbor] = -1 * colors[n]
                        # append the next node to the queue
                        q.append(neighbor)
            return True
                    
        
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        ## represent -1 as uncolored nodes
        ## we need to iterate through each node in the graph and run BFS
        ## to account for nodes that are not connected components
        colors = [-1]*len(graph)
        for i in range(len(graph)):
            ## when looping through to check for nodes that are not connected components, we can
            ## optimize here by not repeating work on nodes that have already been colored,
            ## as that means that we've already visited this node.
            if (colors[i] == -1):
                if (not self.bfs(graph, colors, i)):
                    return False
            
        return True
    def bfs(self, graph, colors, node):
        queue = deque()
        ## print('node: ', node)
        queue.append(node)
        colors[node] = 1
        
        while (queue):
            node = queue.popleft()
            ## iterate through neighbors, set each neighbor as the opposite color of the node
            ## we just popped
            for i in range(len(graph[node])):
                neighbor = graph[node][i]
                ## print('colors array: ', colors)
                if (colors[neighbor]==-1):
                    if (colors[node] == 1):
                        colors[neighbor] = 0
                    else:
                        colors[neighbor] = 1
                    queue.append(neighbor)
                else:
                    ## if the neighbor node already has a color, check to see if
                    ## its the opposite color. if it isn't, then our graph cannot be bipartite
                    ## because that means that we have two edges that are visiting the same node,
                    ## unable to create an independent set this way
                    if (colors[neighbor] == colors[node]):
                        return False
       
                
        return True