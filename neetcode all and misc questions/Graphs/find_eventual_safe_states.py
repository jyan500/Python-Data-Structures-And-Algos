class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Time: O(E+V)
        Space: O(E+V)
        Neetcode: https://youtu.be/Re_v0j0CRsg
        
        Revisit this as it contains a somewhat un-common pattern similar to course schedule
        1) create an adjacency list
        2) Keep a hashmap that serves as a visited set, and also for cycle detection
        3) Run DFS on each node, the idea is that if you initially assign a node in the hashmap to false since you don't know if it will reach a terminal node or if it's in a cycle. 
        4) Through DFS, get to a node that has no more neighbors,
        this is a terminal node. Then by backtracking, if that node's neighbors are also terminal nodes,
        then this node would also be considered terminal, and would be re-marked from False to True in the hashmap.
        
        The tricky part: if you've already seen a node, you would just return hashmap[node], similar to a memoization, since we by backtracking, we can determine if a node on the path had already been seen and determined
        to either be A) able to reach terminal node, B) in a cycle and not valid.

        """
        adjacency = {}
        for i in range(len(graph)):
            adjacency[i] = []
        for i in range(len(graph)):
            for outgoing in graph[i]:
                adjacency[i].append(outgoing)
        res = []
        terminalNodes = {}
        def dfs(node):
            if node in terminalNodes:
                return terminalNodes[node]
            # initially, mark the node as False since we don't know if it leads to a terminal node
            # or if it's in a cycle
            terminalNodes[node] = False
            for neighbor in adjacency[node]:
                if not dfs(neighbor):
                    return False
            # if there are no more outgoing edges, this is a terminal node.
            # it also works recursively as when this backtracks to the previous case,
            # if there are no more neighbors, then that means that node was also a terminal node as well.
            terminalNodes[node] = True
            return True
        for node in adjacency:
            if dfs(node):
                res.append(node)
        return res
        