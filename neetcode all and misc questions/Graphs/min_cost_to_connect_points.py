class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Neetcode:
        https://www.youtube.com/watch?v=f7JOBJIC-NA
        
        Prim's Algorithm solves for the minimum spanning tree here

        Creating the adjacency list is different from most other graph problems
        we treat a given set of points as an index within N (for example, if there are 4 sets of coordinates,
        we label them 0, 1, 2, 3), and then in the adjacency list, save the edge (i.e 0 -> 1), and also keep track
        of the distance between the two edges

        so the adjacency would look something like this:
        points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
        0 -> (0,0)
        1 -> (2,2)
        2 -> (3,10)
        3 -> (7,0)

        {0: [
                [1, distance between (0,0) and (2,2)],
                [2, distance between (0,0) and (3,10)],
                [3, distance between (0,0) and (7,0)],
        ],
        1: [
            [0, distance between (2,2) and (0,0)],
            [2, distance between (2,2) and (3,10)],
            [3, distance between (2,2) and (7,0)]
        ],
        ...
        }

        From there, you would apply BFS, but use a min heap instead of a normal queue, so we're always
        getting the next edge with the smallest distance.

       	Time Complexity: 
        O(N^2LogN), where N is the amount of edges
        the NLogN comes from Prim's algorithm, since it uses heappop()
        """
        import heapq
        N = len(points)
        adj = {}
        # list of [cost, node]
        # creating the edges
        for i in range(N):
            adj[i] = []
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        # Prim's Algorithm
        res = 0
        visit = set()
        # [cost, point], min of the min heap is based on the cost
        minH = [[0, 0]]
        # continue iterating until we visit all the points at least once
        while len(visit) < N:
            # using the min heap, we are able to minimize our total cost
            cost, i = heapq.heappop(minH)
            # if this point has already been visited, skip this iteration
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neighborCost, neighbor in adj[i]:
                if neighbor not in visit:
                    heapq.heappush(minH, [neighborCost, neighbor])
        return res
            
        
        