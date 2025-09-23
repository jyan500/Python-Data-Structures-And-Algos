# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        https://youtu.be/vm63HuIU7kw
        postorder traversal visits all the children first before any of the parents.
        Therefore, the root of the tree should be visited last in this traversal.
        inorder traversal visits the left child, parent then the right child.

        In this example:
        inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
        3 is the root, so the inorder:

        9               3       15 20 7
        left subtree         right subtree

        the next root in the postorder traversal is 20
        you would somehow need to figure out which subtree contains the 20?
        According to neetcode's video, the key is that we continually pop off the postorder traversal,
        this would give us the "right" subtree's root, if it exists.

        inorder = [15 20 7]   

        we then pop off the postorder traversal to get the next root
        7

        inorder = [7]

        Time Complexity: O(N^2), because on each recursive call, it performs a find index operation, which takes O(N) 
        Space Complexity: O(N^2), because on each recursive call, it performs array slicing. In the worst case scenario,
        you could have an inorder traversal that's skewed entirely to the right side like so: [1, 2, 3, 4, 5], and a postorder
        traversal for that tree would like this: [1,2,3,4,5]
        1 
          2
            3
              4
                5

        On each recursive call, you'd create array slices like so:
        [2,3,4,5]
        [3,4,5]
        [4,5]
        [5],
        4 + 3 + 2 + 1 = 10
        the total size is 10, this follows the arithmetic series formula, which would translate to O(N^2), as shown below:

        Arithmetic Series Formula simplified down to Big O of N^2 by dropping the constants and lower order terms.
        n(n-1)/2 = (n² - n)/2 = n²/2 - n/2 = n² (after all constants and lower order terms are dropped)

        """
        # if the inorder is empty, that means that there is no child here, return None
        if not inorder:
            return None
        # pop off the postorder traversal 
        root = postorder.pop()
        node = TreeNode(root)

        # find the root within the inorder traversal
        rootIndex = inorder.index(root)
        # everything to the left of the root is the left subtree, and vice versa for the right subtree
        leftSubtree = inorder[:rootIndex]
        rightSubtree = inorder[rootIndex+1:]

        # try to build the right subtree first since popping off the postorder traversal gives us
        # the root of the right subtree
        node.right = self.buildTree(rightSubtree, postorder)
        node.left = self.buildTree(leftSubtree, postorder)

        return node
