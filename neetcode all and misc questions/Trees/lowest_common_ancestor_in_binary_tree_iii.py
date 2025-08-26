"""
    Lowest Common Ancestor in Binary Tree III

    Given two nodes of a binary tree Node A and Node B, return the lowest common ancestor. 
    Each node has the following attributes: int val, Node left, Node right, int parent
"""
from collections import defaultdict

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode', right: 'TreeNode', parent: 'TreeNode'):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

"""
O(N) Time O(N) Space solution
Traverse from one of the nodes to the top of the tree by using the 
parent pointer (liked a linked list), and store the visited nodes in a set

Traverse from the other node towards the top of the tree, and check
if the node we're on is in the linked list. If so, this is the LCA since
this is technically the "last" node where the two nodes have an ancestor
""" 
class Solution:
    def LCA(nodeA: 'TreeNode', nodeB: 'TreeNode'):
        ancestors = set()
        while (nodeA):
            nodeA = nodeA.parent
            ancestors.add(nodeA)
        lca = None
        while (nodeB):
            nodeB = nodeB.parent
            if nodeB in ancestors:
                lca = nodeB 
                break 
        return lca
 
        
