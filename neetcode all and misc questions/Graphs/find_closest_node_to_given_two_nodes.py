class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        Neetcode:
        https://youtu.be/AZA8orksO4w

        Time: O(E+V)
        Space: O(V)

        create the adjacency list
        find the shortest distance from node1 and node2 to all nodes in the graph
        based on each distance, if we're able to reach a given node from both sides, we want to take the max between
        both sides. And then once we have all the maxes, we then take the min.
        
        for example, if we run BFS starting on both node 0, and then starting on node1, we'd get this
        node 0    node 1
        ------    -------
        0: 0      0: inf
        1: inf    1: 0
        2: 1      2: 1
        3: 2      3: 2
        
        we then take the max between each node, 
        0: INF
        1: INF
        2: 1
        3: 2
        
        we then take the min out of all of these to get the smallest max distance
        which would be 1. But we want to return the node associated with this, which is 2
        """
        n = len(edges)
        adjacency = {}
        for i in range(n):
            adjacency[i] = []
        for i in range(n):
            if edges[i] != -1:
                adjacency[i].append(edges[i])

        def bfs(node, shortestDistance):
            q = deque([(node, 0)])
            visited = set()
            while (q):
                n, distance = q.popleft()
                if n in visited:
                    continue
                visited.add(n)
                for neighbor in adjacency[n]:
                    q.append((neighbor, distance+1))
                    shortestDistance[neighbor] = min(shortestDistance[neighbor], distance + 1)
            return shortestDistance
        distance1 = [float("inf")] * n
        distance2 = [float("inf")] * n
        # the distance to the node itself is 0
        distance1[node1] = 0
        distance2[node2] = 0
        distance1 = bfs(node1, distance1)
        distance2 = bfs(node2, distance2)
        maxes = []
        for i in range(n):
            maxes.append(max(distance1[i], distance2[i]))
        # get the min index to receive the node with the smallest index
        minDistance = min(maxes)
        # note that if minDistance is inf, this means the node was not reachable from either node1 nor node2, 
        # so we'd return -1
        return maxes.index(minDistance) if minDistance != float("inf") else -1