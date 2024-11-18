"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/
Neetcode Explanation:
https://youtu.be/69rcy6lb-HQ

There's a more optimal solution where you only perform BFS one time instead of twice (Neetcode's explanation),
but I decided to implement the simpler solution with two BFS runs as it's easier to remember (which is explained at the beginning of the video)

Approach:
1) Create two separate adjacency lists with the red edges and blue edges
2) Create a "res" array starting with [float(inf)] * n, where on each BFS run, we will update each value
from 0 ... n - 1 based on the shortest path that we found using min(res[i], current steps taken)
2) Run BFS, but two separate times, passing in a different starting color (using -1, and 1, similar to the "Is Graph Bipartite" problem).
    - The idea is that when running BFS, we store a tuple on the queue like so:
    (currentNode, currentStepsTaken, currentColor)
    - Whenever we push onto the queue, we increment the currentStepsTaken, and also do -1 * currentColor to alternate the color
    - This way, we'll always be alternating the edge color on each step.
3) The tricky part of the problem is that there can be cycles and parallel edges, meaning that
there can be two edges that go to the same node, but they are different colors. To handle this, I kept a visited set
which stores tuples like so:

visited = set((currentNode, currentColor)),
storing the current color ensures that you can distinguish between parallel edges where the node is the same but the colors are different

You can then check if node in visited like normal, and continue if it's already in the visited set to avoid cycles, but allow for
parallel edges.

4) If there are any float(inf) remaining in res, iterate through and set these to -1 to indicate that this node could not be reached
using alternate colors

BFS
Time: O(E+V)
Space: O(V)
"""
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [float(inf)] * n
        redAdj = {}
        blueAdj = {}
        for i in range(n):
            redAdj[i] = []
            blueAdj[i] = []
        for node, vertex in redEdges:
            redAdj[node].append(vertex)
        for node, vertex in blueEdges:
            blueAdj[node].append(vertex)
        # alternate the starting color using two BFS runs starting at 0
        def bfs(startingColor):
            q = deque()
            # store the tuple containing the current node and the amount of steps
            # taken so far, and the current color
            q.append((0, 0, startingColor))
            # need visited set in case of cycle, but also store the current color
            # along with this, as it's okay to re-visit the same node, but with a different
            # color edge. This handles edge cases when you have two edges going to the same node, but different colors
            visited = set()
            while q:
                node, stepsTaken, currentColor = q.popleft()
                # to handle edge 
                if (node, currentColor) in visited:
                    continue
                visited.add((node, currentColor))
                res[node] = min(res[node], stepsTaken)
                # depending on which color, use that specific adjacency list for 
                # that color of edges
                edges = redAdj if currentColor == -1 else blueAdj
                for neighbor in edges[node]:
                    # when visiting the next edge, switch the current color,
                    # by changing from -1 to 1, or 1 to -1.
                    q.append((neighbor, stepsTaken+1, -1 * currentColor))   
        bfs(-1)
        bfs(1)
        for i in range(len(res)):
            # if any node couldn't be reached with an alternating path,
            # it should still be float(inf). In this case, change these to -1
            if res[i] == float("inf"):
                res[i] = -1
        return res
        
                    
            
            