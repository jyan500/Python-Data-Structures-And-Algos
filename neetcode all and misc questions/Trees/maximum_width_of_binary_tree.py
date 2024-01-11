"""
https://leetcode.com/problems/maximum-width-of-binary-tree/
https://www.youtube.com/watch?v=FPzLE2L7uHs&ab_channel=NeetCodeIO
Key Concepts:
Level Order Traversal with heap counting trick:
    1) because we need to treat the tree as if it were complete, we'd be including null values as part of our width 
    calculation
    2) however, because level order traversal doesn't include null value nodes, we need to a trick to assign 
    each node a number which represents the amount of nodes so far in our tree. 
    For a binary tree, if the parent is num

    the left child's value would be num * 2
    the right child's value would be 1 + num * 2

    For example:

        A  
     B       C         
  D    E  None    G

  A would have the value 1, since it's the 1st node, call it num
    

  num value of A = 1

  B would be num * 2 = 2
  C would be 1 + num * 2 = 3 
 
  num value of B = 2

  D would be num * 2 = 4
  E would be 1 + num * 2 = 5

  num value of C = 3

  G would be 1 + num * 2 = 7

  here, the maximum width would be
  num - leftmost num + 1
  the leftmost node's num value is always the first non-null element in our level.
  we continually calculate the max width by subtracting the current value of 
  num with our left most node's num value

  In this case, 7 - 4 + 1 = 4

  3) We can store the node as well as the num value in our queue using a tuple


Time Complexity: O(N)
Space Complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q = deque()
        q.append((root, 1))
        maxWidth = float("-inf")

        while (q):
            leftMost = None
            for i in range(len(q)):
                node, num = q.popleft()
                if not leftMost:
                    leftMost = num
                if node.left:
                    q.append((node.left, num*2))
                if node.right:
                    q.append((node.right, 1+num*2))
                maxWidth = max(maxWidth, num - leftMost + 1)
        return maxWidth
                