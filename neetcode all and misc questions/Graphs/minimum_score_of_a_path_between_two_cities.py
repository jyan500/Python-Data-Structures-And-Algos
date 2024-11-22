class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        this is an undirected graph, not necessarily connected.
        find all possible paths to the target, that includes paths that go "through" the target as well
        https://www.youtube.com/watch?v=K7-mXA0irhY&ab_channel=NeetCodeIO
        
        The tricky part is realizing that you can technically "revisit" old edges, but you won't continue
        to run DFS down these edges, which is why there's no need to differentiate between the "to" and "from" edges. However, inside the "for neighbor in adjacency[node]" loop allows you to
        constantly update the smallest distance between two edges, as you will eventually visit every node (including the target), so a path has to be found since the problem states there will ALWAYS be at least one path between 1 to n.
        """
        adjacency = {}
        for i in range(n):
            adjacency[i+1] = []
        # label the forwards and backwards edges to differentiate in the visited set
        for src, dst, dist in roads:
            adjacency[src].append((dst, dist))
            adjacency[dst].append((src, dist))
        self.res = float("inf")
        self.visited = set()
        def dfs(node):
            if node in self.visited:
                return
            self.visited.add(node)
            for neighbor, dist in adjacency[node]:
                self.res = min(self.res, dist)
                dfs(neighbor)
        
        dfs(1)
        return self.res
            
            