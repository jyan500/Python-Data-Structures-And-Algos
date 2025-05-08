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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Revisited on 5/8/2025, this solution isn't as clean compared to 2/3/2025's solution
        Approach:
        1) find the path to nodes p and q using preorder traversal which visits the node before the left and right, store the values in array.
        2) iterate through both paths simultaneously until the nodes
        are no longer the same, and then return the node right before. We can do this
        because all nodes in the tree are assumed to be unique, so we won't run into case
        where we have to handle values that are the same as p or q.
        """
        self.pathToP = []
        self.pathToQ = []
        def getPath(node, target, forQ =False):
            # perform a preorder traversal
            if node:
                if node.val == target.val:
                    if forQ:
                        self.pathToQ = [node] + self.pathToQ
                    else:
                        self.pathToP = [node] + self.pathToP
                    return True
                pathA = getPath(node.left, target, forQ)
                pathB = getPath(node.right, target, forQ)
                if pathA or pathB:
                    if forQ:
                        self.pathToQ = [node] + self.pathToQ
                    else:
                        self.pathToP = [node] + self.pathToP
                return pathA or pathB

            return False

        getPath(root, p)
        getPath(root, q, True)

        i = 0
        j = 0
        # get the previous value. Note that if one of the paths have already
        # ended, the last node in the shorter path is the LCA
        while (i < len(self.pathToP)-1 and j < len(self.pathToQ)-1):
            # if the next value in the path is not the same, break. As i will now
            # be the LCA 
            if self.pathToP[i+1].val != self.pathToQ[j+1].val:
                break
            i += 1
            j += 1
        return self.pathToP[i]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Revisited 2/3/2025 with the same solution

        This works on the assumption that every node in the tree is unique,
        which means that there is only ONE valid path to p and q
        1) store the tree node path from the root node to p in a list
        2) store the tree node path from the root node to q in a list
        3) Use a while loop to compare the two lists simultaneously until the node
        is no longer the same. This means that the path has diverged.  
        """
        # get path from root to target
        def getPath(root: 'TreeNode', target: 'TreeNode', path: ['TreeNode']) -> bool:
            if root:
                path.append(root)
                # once we've found the path, return True
                if root.val == target.val:
                    return True
                # continue searching for the node
                found = getPath(root.left, target, path) or getPath(root.right, target, path)
                # if we didn't find the proper path, we backtrack path so we don't
                # include the unnecessary nodes
                if not found:
                    path.pop()
                return found
            return False
        
        pathP = []
        pathQ = []
        getPath(root, p, pathP)
        getPath(root, q, pathQ)
        
        lenP = len(pathP)
        lenQ = len(pathQ)
        i = 0
        j = 0      
        while (i < lenP and j < lenQ):
            if pathP[i].val != pathQ[j].val:
                # get the previous node, this was the LCA since the paths have differed
                return pathP[i-1]
            i += 1
            j += 1
        # if one of the lists ended, that means all the nodes were the same up until
        # the end of one path, which means the previous node before the end is the LCA,
        return pathP[i-1]


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
    
    
            