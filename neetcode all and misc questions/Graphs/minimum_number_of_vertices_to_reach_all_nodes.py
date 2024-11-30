class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Approach:
        Knowing that this is graph is directed and acyclic,
        1) A node that has an incoming edge means that it can be reached from another node
        2) However, a node with no incoming edges means that it can only be reached by itself.
        3) To solve the problem, you'd just need to get the nodes that have no incoming edges

        My original solution was using DFS and visited, and then counting the incoming edges
        via DFS for each neighbor
        
        Optimal solution uses a trick where instead of mapping the adjacency from src to dest,
        you'd map from dest to src, which tells you the dest has an incoming edge.
        
        So any node that doesn't have any src would be in our answer

        Time: O(E+V)
        Space: O(E+V)
        """
        adjacency = {}
        for i in range(n):
            adjacency[i] = []
        for src, dest in edges:
            adjacency[dest].append(src)
        
        res = []
        for node in adjacency:
            # if the dest didn't have any src, this means this node has no incoming edges
            if len(adjacency[node]) == 0:
                res.append(node)
        return res

        """
        adjacency = {}
        incoming = {}
        for i in range(n):
            adjacency[i] = []
            incoming[i] = 0
        for src, dst in edges:
            adjacency[src].append(dst)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjacency[node]:
                # if this node has an outgoing edge to the neighbor, increment the neighbor's count
                # of incoming edges
                incoming[neighbor] += 1
                dfs(neighbor)
        for node in adjacency:
            if node not in visited:
                dfs(node)
        noIncomingEdges = []
        for node in incoming:
            if incoming[node] == 0:
                noIncomingEdges.append(node)
        return noIncomingEdges
        """