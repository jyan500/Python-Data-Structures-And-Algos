'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

https://www.youtube.com/watch?v=XZnWETlZZ14&ab_channel=KevinNaughtonJr.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## Perform BFS
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if (root == None):
            return result
        queue = []
        queue.append(root)
        while (len(queue) != 0):
            n = len(queue)
            current_level = []
            ## for each node in the queue, add to the current level list
            ## and then for each node, see if there's a left and right, add those to the queue if there are
            for i in range(n):
                ## remove the first item from the queue (First in First out)
                r = queue.pop(0)
                current_level.append(r.val)
                if (r.left != None):
                	## append the left before the right, since we need to return left through right in our return list
                    queue.append(r.left)
                if (r.right != None):
                    queue.append(r.right)
            result.append(current_level)
        return result
            
        