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