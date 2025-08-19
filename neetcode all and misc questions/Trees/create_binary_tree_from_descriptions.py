# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        https://leetcode.com/problems/create-binary-tree-from-descriptions/
        
        [parent, child, isLeft]
        isLeft == 1, child is left child of parent
        isLeft == 0, child is right child of parent

        brainstorming:
        based on the descriptions, how to figure out which one is the root?

        root should have no parent, meaning that root should never be a child,
        so it wouldn't appear in index 1 of any list.

        perhaps we can treat this as a graph problem, so you'd try to create an adjacency list,
        where index 0 is the node and index 1 is an edge.

        if we were to try this with the example below:
        [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]

        20: [15, 17],
        50: [20, 80],
        80: [19]

        we can see here that 50 is the root because there is no other parent pointing to it.

        We'd also need to take into account whether its the left or right child by keeping this
        information in a tuple alongside the child value itself like so:

        20: [(15, 1), (17, 0)],
        50: [(20, 1), (80, 0)],
        80: [(19, 1)]

        Using DFS, we can construct the tree
        by starting at the root and then exploring the nodes below. Then at each recursive call,
        we return a TreeNode() consisting of the current node, and the left subtree (which is the result
        of the recursive call) and right subtree. This is a similar concept to the problem: "Construct
        binary tree from inorder and preorder travresal"

        Time: O(N+M) (performing DFS, where N is the amount of nodes and M is the amount of edges)
        Space: O(N) (to hold the adjacency list)

        """
        # construct adjacency
        adjacency = defaultdict(list)
        children = set()
        for parent, child, isLeft in descriptions:
            adjacency[parent].append((child, isLeft))
            children.add(child)
        
        # identify the root
        rootVal = 0
        for parent, child, isLeft in descriptions:
            if parent not in children:
                rootVal = parent
                break
        
        # perform DFS, by looping through the neighbors on the adjacency list
        def construct(node, adj):
            left = None
            right = None
            for edge, isLeft in adj[node]:
                if isLeft == 1:
                    left = construct(edge, adj)
                else:
                    right = construct(edge, adj)
            # return a tree node with the current node and the results of the left and right subtree
            return TreeNode(node, left=left, right=right)
    
        return construct(rootVal, adjacency)
