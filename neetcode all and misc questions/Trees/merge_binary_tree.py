'''
https://leetcode.com/problems/merge-two-binary-trees/

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Approach: we create a new tree Node, and recur down left and right like a pre-order traversal
we account for three cases: 
1. when one root is null but the other is not, we will set the root to be equal
to the node that is not null, and continuing recurring down left and right, but for the node that is null,
we'll just pass null into the recursive call. 
2. When both roots are not null, we'll add the two node values together
to form the root.
3. If both roots are null, we've hit our base case, so there's no more nodes to traverse anymore, just return None

by the end, our r.left and r.right will contain the left and right subtrees merged together
so we just return r

Time complexity: O(max(T1,T2)), as it will depend if T1 or T2 has more nodes, 
Space complexity: O(max(T1,T2)), as the space will need to be enough to include the bigger of the two trees

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""" Revisited 10/5/2024 """
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            return TreeNode(root1.val + root2.val, left=self.mergeTrees(root1.left, root2.left), right=self.mergeTrees(root1.right, root2.right))
        elif root1:
            return TreeNode(root1.val, left=self.mergeTrees(root1.left, None), right=self.mergeTrees(root1.right, None))
        elif root2:
            return TreeNode(root2.val, left=self.mergeTrees(None, root2.left), right=self.mergeTrees(None, root2.right))
        return None

# Revisited on 12/26/2023
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """

        1) Make recursive calls to go down the left subtree of both trees first, then the right subtrees
        2) If one root exists in one tree while the other does not, return the root that exists 
        3) If both roots do not exist, return None
        4) Once we've traversed both left and right for the given node, that means that we're at the parent, which exists
        for both trees. Create the treenode by setting the left and right to be the recursive calls, and then the value
        to be the sum of both parents' values.

        """
        if (root1 and not root2) or (root2 and not root1):
            return root1 if root1 else root2
        elif (not root1 and not root2):
            return None
        else:
            left = self.mergeTrees(root1.left, root2.left)
            right = self.mergeTrees(root1.right, root2.right)
            return TreeNode(root1.val + root2.val, left, right)

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        ## base case, when both roots are None, we return None
        if (not root1 and not root2):
            return None
        ## if root1 is not null and root 1 is null
        ## we set the root to be root1.val, and continue
        ## recurring, passing down root1.left, but for root2, we'll pass None instead
        ## since there's no children
        elif (root1 and not root2):
            r = TreeNode(root1.val)
            r.left = self.mergeTrees(root1.left, None)
            r.right = self.mergeTrees(root1.right, None)
        ## if root1 is null and root 2 is not null
        ## we set the root to be root2.val, and continue
        ## recurring, passing down root2.left, but for root1, we'll pass None instead
        ## since there's no children
        elif (not root1 and root2):
            r = TreeNode(root2.val)
            r.left = self.mergeTrees(None, root2.left)
            r.right = self.mergeTrees(None, root2.right)
        ## if root1 and root2 are not null, add the two root values since they're overlapping
        ## and continue to recur down both sides of the tree
        else:
            r = TreeNode(root1.val+root2.val)   
            r.left = self.mergeTrees(root1.left, root2.left)
            r.right = self.mergeTrees(root1.right,root2.right)
        return r
    
    '''
    test case
    root1 = [1,3,2,5] root2 = [2,1,3,null,4,null,7]
    
    r = TreeNode(1+2) = 3
    r.left = self.mergeTrees(root1.left=3,root2.left=1)
    
    recur #1
    r = TreeNode(3+1)=4
    r.left = self.mergeTrees(root1.left=5,root2.left=None)
    
    recur #2
    in this case, root1 is not None, but root2 is None
    r = TreeNode(5)
    r.left = self.mergeTrees(root1.left = None, None)
    
    recur #3
    hit our base case when both roots are None
    
    go back to recur #2
    r.right = self.mergeTrees(root1.right = None, root2.right = 4)
    
    recur #4
    case when root1 is None but root2 is not None
    r = TreeNode(4)
    r.left = self.mergeTrees(None, root2.right = None)
    
    hits our base case, this will return back to #4, and #4 returns r
    
    return to recur #2
    
    recur #2 will now return r
    back to recur #1
    r.right = self.mergeTrees(root1.right=2,root2.right=3)
    
    recur #5
    r = TreeNode(2+3)=5
    r.left = self.mergeTrees(root1.left = None, root2.left = None)
    
    recur #6
    root1 is None and root2 is None
    r = TreeNode(7)
    r.left = self.mergeTrees(None, root2.right = None)
    
    to base case, return None, back to recur #6
    recur #6
    r.right = self.mergeTrees(None, None)
    
    also to base case, return None, back to recur #6
    recur #6 returns r, back to recur #5
    
    r.right = self.mergeTrees(root1.right=None, root2.right=7)
    
    recur #7
    root1 is None but root2 is not None
    r = TreeNode(7)
    
    ... after this it should backtrack eventually to recur #1
    where it will return r which is our final answer, since r.left and r.right
    would've contained the left and right subtree at that point
    
    
    '''