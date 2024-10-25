class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Directed acyclic graph (acyclic because in the problem constraints,
        it mentions in connections[i] = [a, b], a != b)
        
        Adjacency List
        see if you can reach 0 from every other node
        if a node cannot reach 0, figure out the path that leads to zero
        minimum number of edges changed, 
        this is a candidate for BFS search because of that fact, because
        we want the minimum, which means we have to know at each point, which neighbors
        would need to be reversed
        
        If you keep both an undirected and directed version of the adjacency list,
        it might be possible to check if there's a route that "could've" existed to reach
        0. Also using reverse thinking, you can see whether an outgoing node from 0 to another node would be considered "one" node that would need to be changed in order to connect that node to 0 (in the opposite direction back towards 0)
        
        Using BFS, if we start from 0, we check whether there's any nodes that 0 points to based on the directed version of the adjacency list, if so go down that path, and then increment a "total" counter by one to indicate that this edge would need to be reversed

        Time: O(E+V) (normal time for BFS)
        Space: O(E+V) (technically two times since there's both directed and undirected adjacency list versions)
        
        """
        from collections import deque
        undirected = {}
        directed = {}
        for i in range(n):
            undirected[i] = set()
            directed[i] = set()
        for a, b in connections:
            undirected[a].add(b)
            undirected[b].add(a)
            directed[a].add(b)
        
        q = deque()
        q.append(0)
        total = 0
        visited = set()
        visited.add(0)
        while q:
            # similar to level order traversal, this loop exists in order to traverse through all
            # immediate neighbors of a given node first, so we're able to increment the total count per "level"
            # by doing so, BFS automatically gives us the minimum amount
            for i in range(len(q)):
                node = q.popleft()
                # if we've already visited this node, ignore
                for neighbor in undirected[node]:
                    # if the node exists in the directed version,
                    # these are the nodes that would need to be reversed in order
                    # for the node to reach 0, so increment count by 1
                    if neighbor not in visited:
                        if neighbor in directed[node]:
                            total += 1
                        q.append(neighbor)
                        visited.add(neighbor)                
        return total
                
            
    