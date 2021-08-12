"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

## Time complexity : O(N), as we visit each node once
## Space complexity : O(level with the most nodes), since the max amount of space we need is the 
## level of the tree with highest amount of nodes
## Concept:
## Perform level order traversal using queue and BFS
## the next node in the queue will be the "next" of the node that was just popped off
## make sure to set the queue length N before iteration
## since we only want to iterate and set the nodes on our current tree level
## and not any additional children on lower level

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    
    def connect(self, root: 'Node') -> 'Node':
        if (not root):
            return None
        q = deque()
        q.append(root)
        while (q):
            prev =  q[0]
            N = len(q)
            last_node = None
            for i in range(N):
                node = q.popleft()
                next_node = None
                if (i == N-1):
                    node.next = None
                else:
                    node.next = q[0]
                    
                if (node.left != None):
                    q.append(node.left)
                if (node.right != None):
                    q.append(node.right)          
        return root
                    