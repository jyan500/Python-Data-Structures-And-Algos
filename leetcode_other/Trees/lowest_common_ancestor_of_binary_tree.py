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
    
    
            