'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

https://www.youtube.com/watch?v=XZnWETlZZ14&ab_channel=KevinNaughtonJr.
'''

"""
Revisited on 9/30/2024 with the same solution
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        q.append(root)
        levels = []
        if not root:
            return []
        while (q):
            N = len(q)
            level = []
            for i in range(N):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            levels.append(level)
        return levels

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Revisited on 7/17/2023 (came up with the same solution)
O(N) time, O(N) space

Key Realizations:
You can use BFS, adding the left and right children onto the queue
The items in the queue will always represent the current level,
so you can iterate through the items in the queue and pop off,
appending to a level list
        1
      /   \
     2     3
    / \   / \
   4  5  6   7

queue = [1]
level = []
result = []

iterate through queue
only 1, so add 1 to level
1's children are 2 and 3, so add 2 and 3 to the queue
append [1] to result

queue = [2, 3]
level = []
result = [[1]]

iterate through queue
pop left which results in 2
add children 4 and 5
queue is now [3, 4, 5] at this point
add 2 to the level list
pop left which results in 3
add children 6 and 7
queue is now [4, 5, 6, 7] at this point
add 3 to the level list

result = [[1], [2, 3]]

in the last iteration, 4, 5, 6, and 7 don't have children,
so these are all added to level list, and because they're 
all popped off without appending any new children, 
the while loop ends
"""
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
            
        