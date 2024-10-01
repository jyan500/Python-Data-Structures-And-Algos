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
the diameter of the binary tree is just the depths of the left and right subtrees added together,
so while we calculate the height of the left and right subtrees, we can calculate the max diameter
at the same time (essentially doing it bottom up starting from the leaf, instead of top down starting from the root)

A key concept behind this is using a global variable to simplify the recursion, in this case, we need to return the 
height of the subtree in the recursive call, but we also need to track diameter. We can keep track of max diameter
via the global variable.

[6, 3, 10, 4, 7, null, null, null, null, 2, 8, 1, null, null, null, null, 5, null]

        6
    3       10 
  4   7     
     2 8 
    1
     5  

In this example, we can see the diameter of the tree is 6, starting to the left
of the root 6 (6 -> 3 -> 4, which is 2) (3->7->2->1->5, which is 4)

1) root = 6 left_depth = self.getDepth(3)
2) root = 3, left_depth = self.getDepth(4)
3) root = 4, left_depth = self.getDepth(None) -> base case, returns 0 

back to recursive call 2)
root = 3
left_depth = 0
right_depth = self.getDepth(7)

4) root = 7, left_depth = self.getDepth(2)
5) root = 2, left_depth = self.getDepth(1)
6) root = 1, , no left child,  right_depth = self.getDepth(5)
7) root = 5, no left and right child, returns 0 


Back to recursive call 6), no right child, diameter is 1, returns 1
Back to recursive call 5), no right child, diameter is 2, returns 2
Back to recursive call 4), has right child

root = 7
left_depth = 0
right_depth = self.getDepth(8)

8) root = 8, right_depth = self.getDepth(None) -> base case, returns 0 
right_depth is 1


back to recursive call 4)
diameter is left + right (which is 3+1), returns tree height of 3

Back to recursive call 2)
increase tree height to 4, maxDiameter is now 4 + 1 = 5 (1 being the left subtree of 3)

pops back to recursive call 1)
maxDiameter is now 6, tree height is 5

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    revisited on 9/30/2024 using the same approach as below
    https://neetcode.io/problems/binary-tree-diameter
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def getHeight(root):
            if (root):
                leftHeight = getHeight(root.left)
                rightHeight = getHeight(root.right)
                diameter = leftHeight + rightHeight
                if (diameter > self.maxDiameter):
                    self.maxDiameter = diameter
                return 1 + max(leftHeight, rightHeight)
            return 0
        getHeight(root)
        return self.maxDiameter

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
            # calculate the height of the left subtree and right subtree
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
            


