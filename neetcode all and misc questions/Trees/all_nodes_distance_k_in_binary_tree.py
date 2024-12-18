# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Revisited 12/18/2024
        Initial thoughts:
        - convert the binary tree to an undirected graph using an adjacency list,
        and run BFS starting from the target node. Using the inner for loop in BFS,
        we make sure that only nodes of a certain distance are on the queue,
        so once cur == k, the while loop breaks and only the nodes of distance K are left on the queue.
        
        Time: O(N) 
        Space: O(N)
        """
        from collections import defaultdict, deque
        self.adjacency = defaultdict(list)
        def buildAdjacency(root):
            if root:
                if root.left:
                    # save both ways since it's an undirected graph
                    self.adjacency[root.val].append(root.left.val)
                    self.adjacency[root.left.val].append(root.val)
                if root.right:
                    self.adjacency[root.val].append(root.right.val)
                    self.adjacency[root.right.val].append(root.val)
                buildAdjacency(root.left)
                buildAdjacency(root.right)
        buildAdjacency(root)
        
        visited = set()
        q = deque()
        q.append(target.val)
        visited.add(target.val)
        cur = 0
        while (q and cur < k):
            for i in range(len(q)):
                node = q.popleft()
                for neighbor in self.adjacency[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            cur += 1
        # at the end, the only values left in the queue should be the proper
        # distance away from target
        return list(q)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        1) Create an adjacency list for an undirected graph by traversing the 
        tree using preorder traversal, where we visit the root first
        2) Run a BFS (using inner loop) to pop off the queue in levels, until
        level == k. Then we can just return the elements inside the queue. 
        3) We also need to keep visited set to avoid adding back the previous node
        we were just at since this is an undirected graph

        Time Complexity: O(N + k)
        Space Complexity: O(N)
        """
        if k == 0:
            return [target.val]
        # create an adjacency list by traversing the tree
        # then use BFS 
        from collections import deque
        self.adjacency = dict()
        def preorder(root):
            if root:
                if root.val not in self.adjacency:
                    self.adjacency[root.val] = []
                if root.left:
                    self.adjacency[root.val].append(root.left.val)
                    if root.left.val in self.adjacency:
                        self.adjacency[root.left.val].append(root.val)
                    else:
                        self.adjacency[root.left.val] = [root.val]
                if root.right:
                    self.adjacency[root.val].append(root.right.val)
                    if root.right.val in self.adjacency:
                        self.adjacency[root.right.val].append(root.val)
                    else:
                        self.adjacency[root.right.val] = [root.val]
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        
        src = target.val
        q = deque()
        q.append(src)
        numStops = 0
        visited = set()
        visited.add(src)

        while (q and numStops < k):
            for i in range(len(q)):
                n = q.popleft()
                for neighbor in self.adjacency[n]:
                    # because this is an undirected graph, ignore the edge that goes back to n
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        
            numStops += 1
        
        return list(q)
                
            
                
            
        