'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

""" 
revisited on 7-17-2023, O(N) time O(1) space
Neetcode: https://www.youtube.com/watch?v=s6ATEkipzow

Concept:
At any point in the subtree, if we're in the left subtree, we need to make sure the root value
is less than the max value of that subtree, and if we're in the right subtree,
we make sure the root value is greater than the min value of the subtree

We can do this by keeping track of a min and max as we traverse the tree
      3
    /   \
   1     5
  / \   / \
 0  2  4   6

 traverse the left side
 root = 3
 min = float(-inf)
 max = float(inf)

 is min < root < max? yes, update
 max as we're in the left subtree, every value needs to be < 3

 root = 1
 min = float(-inf)
 max = 3

 is min < root < max, yes, update
 max as we're in left subtree, every value needs to be < 1

 root = 0
 min = float(-inf)
 max = 1

 no children here, starting from the case above where root = 1, we go to the right subtree instead.
 Update min because each value in the right subtree must be > min
 we keep the maximum the same, as the value must also be < 3, which is the max
 root = 2
 min = 1
 max = 3

 min < root < max, yes,

 continue this process for the rest of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Revisited 4/16/2025
    apply preorder search, tracking current min and current max
    for this subtree
    1) when searching left, we only update the cur max since every
    node is smaller than the current max on the left side
    2) when search right, we only update the cur min since every node
    is larger than the current min on the right side
    if node falls outside of these boundaries, it should return False
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root, curMin, curMax):
            if root:
                return root.val > curMin \
                and root.val < curMax and \
                search(root.left, curMin, root.val) and \
                search(root.right, root.val, curMax)
            return True

        return search(root, float("-inf"), float("inf"))

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(root, currMin, currMax):
            """ 
            Revisited 10/1/2024 
            https://neetcode.io/problems/valid-binary-search-tree
            at each new node, we update the currMin to be the node's value 
            when going to the right to ensure that each node > currMin, 
            and update the currMax to be the node's value when going to the left to ensure
            that the values at each nodes < currMax, to ensure that every node in the subtree
            on the respective side follows this BST property.
            the left and right children immediately below the current node must also
            follow BST properties where the left val < root.val and right.val > root.val

            Cleaned up logic:
            rather than checking the existence of the left and right nodes each time and comparing
            it to node, we can check node against the currMin and currMax values, as this one of these 
            values will contain the parent value since we're passed in root.val on each recursive call
            """
            if root:
                if root.val >= currMax or root.val <= currMin:
                    return False
                """
                on the left subtree, we update our currMax value, as every node
                on the left subtree must be less than currMax
                whereas on the right subtree, we update currMin value to be root.val,
                as every node must be greater than current min
                """
                return search(root.left, currMin, root.val) and search(root.right, root.val, currMax)
            # if neither side exists, this is a just a node with two leaf nodes with value None,
            # and this is by definition, a binary search tree since it's a single node by itself
            return True
        
        return search(root, float("-inf"), float("inf"))
""" 
8/3, same idea but shorter solution 
"""
class Solution3:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, minVal, maxVal):
            if root:
                return minVal < root.val < maxVal and helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)
            return True
        return helper(root, float("-inf"), float("inf"))

class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        return self.isValidBSTHelper(root, float("-inf"), float("inf"))
   
    def isValidBSTHelper(self, root: Optional[TreeNode], minimum, maximum) -> bool:
        if not root:
            return True
        if not (root.val < maximum and root.val > minimum):
            return False
        else:
            return self.isValidBSTHelper(root.left, minimum, root.val) and self.isValidBSTHelper(root.right, root.val, maximum)

class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)
    def validate(self, root, min_val, max_val) -> bool:
        if (not root):
            return True
        elif (min_val != None and root.val <= min_val or max_val != None and root.val >= max_val):
            return False
        else:
            ## pass in root.val for max on the left subtree
            ## to check that the left subtree's nodes are less than that max
            ## pass in root.val for min on the right subtree
            ## since the right subtree's nodes must always be greater than that min
            return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)