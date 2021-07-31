'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

initial approach (but not the most efficient)
Find the depth of the left and right subtree at each node and add them together to get
the diameter at that subtree

find the max diameter

Time Complexity:
O(N^2), as the depth operation is O(N), and you have to repeat this for every node 
issue is that there's a lot of repeated work
Space : O(1)

Alternative O(N) solution
the diameter of the binary tree is just the depths of the left and right subtrees added together

so alternatively, we can just modify our getDepth function so that it will calculate the diameter at each
point and return the max so we don't have to recur into each node

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        ## keep diameter as a class variable that gets updated at each point
        self.diameter = float('-inf')

    ## faster approach O(N)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ## key: pass down the max diameter so it gets updated at each node
        self.getDepth(root)
        return self.diameter
    
    def getDepth(self, root):
        if (root == None):
            return 0
        else:
            left_depth = self.getDepth(root.left)
            right_depth = self.getDepth(root.right)
            ## since the diameter is the left subtree depth + right subtree depth, add together and set the max
            ## of the sum, and the current diameter variable 
            self.diameter = max(left_depth+right_depth, self.diameter)
            ## continue to calculate the depth
            return 1 + max(left_depth,right_depth)

    ## Initial Solution O(N^2), because we have to re-calculate the depth at each node to then calculate the diameter,
    ## there's a lot of repeated work here
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ## find the depth on the left subtree
        ## find the depth on the right subtree
        ## add them together?
        max_diameter = float('-inf')
        if (not root):
            return max_diameter
        diameter = self.getDepth(root.left)+self.getDepth(root.right)
        max_diameter = max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max_diameter

    def getDepth(self, root):
        if (root == None):
            return 0
        else:
            return 1 + max(self.getDepth(root.left),self.getDepth(root.right))
            


