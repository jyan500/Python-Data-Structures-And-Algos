'''
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []

(An additional case)
Input: root = [1,2]
output: [1,2]

explanation of above case:
by right side view, we define this as the rightmost node of each level of the tree
that explains why a right side view of [1,2] is [1,2], despite 2 being the left child of 1
because in this case for the 2nd level, 2 is the only node that isn't None so that would be the rightmost child

Concept:
perform a level order traversal on our tree using a queue and BFS:
for each node that gets popped from the queue, add its left and right children to the queue
except on each level, we only add the last node of our queue to our result list, as this will be the rightmost node on our current level
(i.e the right most node that is visible if we were to be standing on the right side of the tree as mentioned in the problem description)

Time complexity: O(N), representing the nodes in the tree
space complexity: O(N), N nodes in the queue

Revisited on 8/9/2023
One important note is that we save the length of the queue before we start popping out elements from the level
so we know which element was last in the level

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        queue = deque()
        queue.append(root)
        res = []
        while (queue):
            N = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                ## the last item in the queue will be the rightmost node in our current level
                if i == N-1:
                    res.append(node.val)              
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
               
                
        