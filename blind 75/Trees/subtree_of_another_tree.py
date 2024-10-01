'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Runtime: O(N * M), where N is the number of nodes in root, and M is the number of nodes in subroot
Space: Min(N, M), because the recursion is determined by the tree that has less nodes
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Revisited the problem on 7/19/2023
O(N * M) time, since for each node in the main tree, 
we're doing an O(M) operation for the amount of nodes in the subtree checking
if the given subtree and the subtree starting from node N are the same.

space is determined by the amount of nodes traversed during the recursion that was needed
to find the subtree, at worse it could be O(N * M) amount of recursive calls? 
if the subtree isn't found, we'd perform the search on every root

Key concepts:
1) for each node, check if the subtree starting with that node is the same tree as the 
given subtree. Use the same algorithm as isSameTree to solve this

2) If it's the same, we can return true
otherwise, we continue down the left and right. We can return
whether the subtree is found in the left OR right sides

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Revisited on 9/30/2024
        https://neetcode.io/problems/subtree-of-a-binary-tree
        write a function to determine if two trees are the same
        going through each node, run the function to check if the remainder of that node
        is the same tree as the tree defined by subroot
        O(N*M)
        """
        def isSameTree(p, q):
            if p is None and q is None:
                return True
            elif not p and q or p and not q:
                return False
            else:
                if p.val != q.val:
                    return False
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        # if the subroot is None, it's a subtree of the main tree
        # by default because each child Node has two leaves of value None by default
        if not subRoot:
            return True
        # if the root is None but the subRoot is not None, the subroot cannot be a subtree
        if not root:
            return False
        isSame = isSameTree(root, subRoot)
        if isSame:
            return True
        # if this particular root was not the same as the subroot, continue searching left and right
        # as long as one side yields the same tree, this will return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

class Solution2:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            isSub = self.isSameTree(root, subRoot)
            if isSub:
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    	## if the root is null, then this cannot be a subroot
    	if (root == None):
    		return False
        ## for each call, check if the sameTree function passes, if it continues
        ## to return True at each level of the tree, then subroot has been found
    	elif (self.isSameTree(root, subRoot)):
    		return True
        ## if false, then continue down the left and then the right
    	else:
    		return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
   	
   	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ## base case #1: if the two roots are null, then they're same trees
        if (p == None and q == None):
            return True
        ## base case #2: if either p or q is null but not both, then they're not the same the tree
        elif (p == None or q == None):
            return False
        ## base case #3: if the values of p and q are not equal to each other, they're not the same tree
        elif (p.val != q.val):
            return False
        else:
            ## verify whether the left subtree of p and left subtree of q is equal to the
            ## right subtree of p and right subtree of q
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 