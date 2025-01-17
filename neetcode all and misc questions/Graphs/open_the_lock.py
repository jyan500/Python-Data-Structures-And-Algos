class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        https://leetcode.com/problems/open-the-lock/
        Was able to solve this one with just the hint on leetcode!
        
        Approach:
        It's actually a graph problem, but the trick is figuring out
        how to define the graph relationship:

        Based on the hint on leetcode,
        There are 10000 nodes in total, since the unique values are 
        0000 to 9999. There is an edge between each node if they differ by one digit,
        and if both nodes are not in the "deadends" list.
        Note that this includes when a digit "wraps around" from 0 to 9 and vice versa.

        After that, this is similar to other "shortest path" problems using BFS,
        where you loop through every element in the queue added at that level,
        and pop out, and determine which neighbors to add back in.

        You also keep a "distance" variable on the outside, whenever a level is iterated,
        you add one. So once the target is found, the distance is returned. And by definition,
        this will be the minimum distance.

        Time Complexity: O(E+V), note that there's an additional O(4) amount of work being done to find the "next"
        neighbor with string parsing but it's constant time.
        Space: O(E+V) for creating every new string neighbor
        """
        # if the origin point is a deadend, you cannot proceed since none of the locks can be turned
        # so return -1
        if "0000" in deadends:
            return -1
        visited = set()
        q = deque()
        q.append("0000")
        visited.add("0000")
        distance = 0
        while (q):
            N = len(q)
            for i in range(N):
                node = q.popleft()
                if node == target:
                    return distance
                """
                determine all the nodes that are "one" digit away,
                whether that's going "forwards" or "backwards"
                for example
                0000 -> 0001
                        0010
                        0100
                        1000
                        9000
                        0900
                        0090
                        0009
                add these to the queue
                """
                for k in range(len(node)):
                    mutable = list(node)
                    # if the current digit <= 8, add one, otherwise wraps around back to 0
                    newNodeForward = "".join(mutable[0:k]) + str(int(node[k])+1 if int(node[k]) <= 8 else 0) + "".join(mutable[k+1:])
                    # if the current digit >= 1, subtract one, otherwise wraps around back to 9
                    newNodeBackward = "".join(mutable[0:k]) + str(int(node[k])-1 if int(node[k]) >= 1 else 9) + "".join(mutable[k+1:])
                    if newNodeForward not in visited and newNodeForward not in deadends:
                        visited.add(newNodeForward)
                        q.append(newNodeForward)
                    if newNodeBackward not in visited and newNodeBackward not in deadends:
                        visited.add(newNodeBackward)
                        q.append(newNodeBackward)
            distance += 1
        # if the target was not found inside the BFS, return -1
        return -1