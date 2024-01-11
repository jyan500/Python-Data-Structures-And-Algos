'''
Concept:
Time complexity: O(N) to find paths to p and q, and an additional while loop to compare the path lists
Space complexity: O(N), to store the node paths to p and q

1)search the tree to find the path to p (using our traverse helper which gets the nodes up to p)
2)search the tree to find the path to q (using our traverse helper which gets the nodes up to q)
because each node in the tree is unique, once we find these nodes, these would be the only occurences
of p and q in the tree
3) traverse the list of paths simultaneously, checking if the node values are the same
4) once the node values aren't the same the while loop will stop, and we just need to return the previous node,
as this would represent the lowest common ancestor before the paths diverged

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Revisited on 8/5/2023
Recursive Concept from https://www.youtube.com/watch?v=WO1tfq2sbsI&ab_channel=CrackingFAANG
1) While traversing, if we find p or q, return the root
The idea is that once we return the root in our recursive call on one side,
we check to see if the other side's recursive call also returned a root, or if it returned None
2) If both sides returned a root, that means an ancestor was found, but we can continue to bubble up
the recursion to naturally find the lowest common ancestor.
If only one side returned root, we will continue going up the recursion until:
1) both sides return a root, OR
2) the recursion ends, which means the returned root is the lowest common ancestor, 
because the other target node is on the same side is this root
"""
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        root1 = self.lowestCommonAncestor(root.left, p, q)
        root2 = self.lowestCommonAncestor(root.right, p, q)
        if root1 and root2:
            return root
        if (root1 and not root2):
            return root1
        elif (not root1 and root2):
            return root2
            
            
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## search the tree to find the path to p
        ## because each node in the tree is unique, once we find p, we would've found its only occurence
        p_path = []
        self.traverse(root, p, p_path)
        ## search the tree to find the path to q
        ## because each node in the tree is unique, once we find q, we would've found its only occurence
        q_path = []
        self.traverse(root, q, q_path)
        i = 0
        j = 0
        ## traverse the path lists simultaneously, checking if the node values are the same
        ## as soon as the paths diverge, the LCA would be the node right before the paths diverge
        while (i < len(p_path) and j < len(q_path) and q_path[i].val==p_path[j].val):
            i+=1
            j+=1
        return p_path[i-1]

    ## https://www.geeksforgeeks.org/print-path-root-given-node-binary-tree/
    def traverse(self, root, node, path):
        
        # if root is None there is no path
        if (not root):
            return False

        # push the current root's value in 'path'
        path.append(root)    

        # if it is the required node
        # return true
        if (root.val == node.val):    
            return True

        # else check whether the required node
        # lies in the left subtree or right
        # subtree of the current node
        if (self.traverse(root.left, node, path) or
            self.traverse(root.right, node, path)):
            return True

        # required node does not lie either in
        # the left or right subtree of the current
        # node. Thus, remove current node's value 
        # from 'pop'and then return false    
        path.pop(-1)
        return False
    
    
            