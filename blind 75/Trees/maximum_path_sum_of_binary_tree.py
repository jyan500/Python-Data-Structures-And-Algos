'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

https://www.youtube.com/watch?v=6cA_NDtpyz8&ab_channel=MichaelMuinos
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Revisited on 10/1/2024
        https://neetcode.io/problems/binary-tree-maximum-path-sum
        Also re-referenced:
        https://www.youtube.com/watch?v=6cA_NDtpyz8&ab_channel=MichaelMuinos

        1) A postorder traversal would be appropriate here, because we want
        to determine the sum from the children and then include the parent in the value,
        and work our way upwards.
        2) When doing a postorder traversal, we always visit the left, the right and then the node,
        so in the case there's no left and right, this would indicate a sum of 0, and then including
        the node's value would just be node. 
        3) In the case one side is negative, we wouldn't want to include this part of the path in the path sum,
        as it'd cause the max to go down. In this case, we bound the sum by taking max(sum, 0).
        4) We would then need to determine which side to include in our max path sum, as the max path sum
        cannot include a branch with two children, so we have to take the max between the left and right sums 
        and return the max(left sum, right sum) + root.val into the previous recursive call
        5) Lastly, setting a global variable that has the maxPathSum allows us to keep track
        of the maxPathSum at any point during the traversal.
        """
        self.maxSum = float("-inf")
        def traverse(root):
            if root:
                leftSum = traverse(root.left)
                rightSum = traverse(root.right)
                """
                # bound the left sum + right sum + node.val to 0 in case it's negative
                # so we don't decrease the path sum value
                """
                boundedLeft = max(leftSum, 0)
                boundedRight = max(rightSum, 0)
                """
                # we would then check if this bounded sum (which represents the path sum between
                # the parent node and it's two subtrees exceeds the maxsum)
                """
                self.maxSum = max(boundedLeft+boundedRight+root.val, self.maxSum)
                """
                # what we want to return is the max between the left and right sum, because
                # the boundedSum includes two children which we can't include as we go further up
                # in the tree, so we have to take the max between left and right, and add that to the
                # root.val and return that instead

                A visual explanation of above is:
                    5
                  6   8
                     7  9

                The path sum cannot contain the sums of 5 + 6 + 8 + 7 + 9. It can only include
                either:
                   5           5
                6    8   OR  6   8
                    7              9

                In this example, we'd choose the right side (9), and return 8 + 9 to the previous recursive call
                """
                return max(boundedLeft,boundedRight)+root.val
            return 0
        traverse(root)
        return self.maxSum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_val = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        self.postOrder(root)
        return self.max_val
    def postOrder(self, root: TreeNode) -> int:
        if (not root):
            return 0
        ## the value that is returned must always be greater than zero, otherwise it will subtract from the total max
        left = max(0, self.postOrder(root.left))
        right = max(0, self.postOrder(root.right))
        self.max_val = max(self.max_val, left + right + root.val)
        ## the max(left, right) only takes either the left or right since it can only take one path
        return max(left, right) + root.val
        
        
        