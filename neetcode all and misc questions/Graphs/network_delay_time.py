class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Revisited on 1/16/2026
        1) build adjacency list, this is a directed graph, on each target node in the adjacency list,
        store a tuple of the target AND its weight
        2) Apply Djikstra's algorithm (BFS + minHeap), storing the current time and node into minHeap
            Store visited set and mark node as visited after popping

        For future reference:
        if the graph edges have weights, make sure to include those weights in the adjacency list as tuples,
        and use Djikstra's or Bellman Ford
        """
        import heapq
        adjacency = {}
        for i in range(1, n+1):
            adjacency[i] = []
        for source, target, weight in times:
            adjacency[source].append((target, weight))
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        visited = set()
        while (minHeap):
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            # as we pop off, mark this node as visited.
            # and if we've visited all nodes, then return the time, as 
            # djikstra's would pick the most optimal way to visit all the nodes already.
            if len(visited) == n:
                return time
            for neighbor, weight in adjacency[node]:
                heapq.heappush(minHeap, (time+weight, neighbor))
        return -1 
        
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Revisited on 10/2/2024 with this solution
        Neetcode:
        https://www.youtube.com/watch?v=EaphyqKU4PQ&ab_channel=NeetCode
        Approach:
        Djikstra's Algorithm
        Time Complexity:
        
        O(ELogV), where E is the number of edges and V is the number of vertices
        E = V^2, this is true because an a given graph, there could be bidirectional
        edges between each vertex. In Djikstra's Algorithm, we use a min heap to store
        all possible vertices. Therefore, it's possible we could have the same vertex on the min heap multiple times. So when we pop out of the min heap, it'll be 
        at worst LogV^2, and we repeat this operation for the amount of edges,
        E*LogV^2,
        
        This can be simplified to
        2*E*LogV, and since 2 becomes constant, this further simplifies to
        ELogV, O(ELogV)
        
        """
        # create the adjacency list
        # { source: [(target, time taken), (), ...]}
        # if there's no source node, the default dict takes care of that 
        # by setting to an empty list by default
        adjacency = collections.defaultdict(list)
        for source, target, time in times:
            adjacency[source].append((target, time))
        
        # min heap stores a tuple of the (time, node)
        # in this case, it takes 0 time to traverse to the starting node of k
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            # don't revisit the same node multiple times
            if node in visit:
                continue
            visit.add(node)
            # t should give us the amount of time it takes to reach this node
            t = max(time, t)
            for neighborNode, neighborTime in adjacency[node]:
                if neighborNode not in visit:
                    heapq.heappush(minHeap, (neighborTime + time, neighborNode))
        # we know if we reached every node if the len(visit) == number of nodes
        return t if len(visit) == n else -1