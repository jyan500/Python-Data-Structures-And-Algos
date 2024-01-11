'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Explanation:
https://www.youtube.com/watch?v=ihj4IQGZ2zc&ab_channel=NeetCodeNeetCode

Basic Concept:
the preorder will provide us the root of the tree at each level, and the inorder tells us what should
go in the left subtree and right subtree

definitions
preorder: visit root, visit left, visit right
inorder: visit left, visit root, visit right

// Tried this problem again on 7/22/2021
the key insight was that for the inorder traversal, items to the left of our node contain the left subtree, and items to the right of our node contain the right subtree. 
        
after watching neetcode's video, the flaw in my thinking was that I was only looking for how to find 
the current's node left and right children, rather than looking at it from an entire left and right subtree perspective

For example looking at preorder1 and inorder1's values:

3 will always be the root of the tree
looking at 3 within the inorder1 list, nodes on the left are the left subtree of 3, nodes to the right are the right subtree. 

We can define this index where 3 is located as "m", and then partition our inorder and preorder lists
into left and right halves, and pass those into recursive calls to further build the left and right subtrees.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Revisited on 7/18/2023
Key concepts in this problem:
1) the preorder traversal will always give you the roots
2) the inorder traversal tells you whether the roots are on the left or right subtree

You can get the root from preorder and then find that within the inorder list
any elements to the left of the root within the inorder list = left subtree
any elements to the right = right subtree

Recursively, you can pass in smaller sections of the preorder and inorder lists, 
we can take the length of the left subtree we found from the inorder list,
and then slice the preorder list such that it gives us all the roots for the left subtree,
and same for the right

can also pass in the left/right subtrees found from the inorder

recursively build the left and right passing in these smaller sections of preorder and inorder

Base case is when the preorder list is empty, which means the previous recursive call
was a leaf node with no children

example:

             3
          /     \
         9      20
        /  \   /  \
       12  15 16  7
      /
     10

[3, 9, 12, 10, 15, 20, 16, 7] preorder traversal
[10, 12, 9, 15, 3, 16, 20, 7] inorder traversal

3 is the root based on preorder[0]
find 3 in the inorder traversal list and section it off like so:
left sub = [10, 12, 9, 15] 
right sub = [16, 20, 7]

in the next recursive call, we slice the preorder where we get the roots for the
left and right subtrees
[9, 12, 10, 15] is passed in to the left, [20, 16, 7] is passed into the right

in the next recursive call to build the left
[9, 12, 10, 15] is our preorder
[10, 12, 9, 15] is our inorder

preorder[0] is 9, which is the next root in our tree on the left side
we find 9 within the inorder and split it off again
left sub = [10, 12]
right sub = [15]

we then slice the preorder list again
[12, 10] is passed in to the left, [15] is passed into the right

in the next recursive call to build the left
[12, 10] is our preorder
[10, 12] is our inorder

preorder[0], 12 is the root
find 12 in the inorder list
left sub = [10]
right sub = [], which means there's no child on the right of root 12

slice the preorder list again
[10] is passed into the left, [] is passed into the right

in the next recursive call to build the left
[10] is our predrder
[10] is our inorder

at this point, if we go further, we'll pass in an empty list and return None in the base case
because our left recursive call has now returned, we try building the right side now.

We actually can't build anything on the right either, so now we create our first node 10,

If we continue to follow the recursion, you'll see the nodes getting built in the following order
10 -> 12 -> 15 -> 9 -> 16 -> 7 -> 20 -> 3
which is technically the postorder traversal, and it makes sense: left, right and then process


"""
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root is always the first element of the preorder list
        if len(preorder) == 0:
            return None
        root = preorder[0]
    
        # find the root in the inorder list
        rootIndex = inorder.index(root)
        inOrderRoot = inorder[rootIndex]
        # Anything to the left of this root
        # is the left subtree, and anything
        # to the right is the right subtree
        leftSubtree = inorder[:rootIndex]
        rightSubtree = inorder[rootIndex+1:]

        # within the recursion, we progressively pass in smaller sections of the preorder and inorder lists
        # for preorder, we know the root is always the 0th element, so we slice from 1 to the 1+len(leftSubtree)
        # to get all roots for the left subtree, and then for the right subtree,
        # slicing from len(preorder) - len(rightSubtree) to get all the roots for the right subtree
        left = self.buildTree(preorder[1:1+len(leftSubtree)], leftSubtree)
        right = self.buildTree(preorder[len(preorder)-len(rightSubtree): ], rightSubtree)
        newRoot = TreeNode(val=root, left=left, right=right)
        return newRoot

class Solution:
    ## Neetcode's solution
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

    ## own solution based off of neetcode
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, inorder)

    def helper(self, preorder: List[int], inorder: List[int]):
        ## note that if the preorder list is empty
        ## that means our current node has no children, so we just return None
        if (len(preorder) == 0 or len(inorder) == 0):
            return
        m = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        ## for our left half, recursively call self.helper on the left subtree section of the preorder list
        ## (Everything from the first element (not including the root) to the end of the left subtree section m+1)
        ## as well as the left half of the inorder list (everything up to and including the index of current root)
        root.left = self.helper(preorder[1:m+1],inorder[:m])
        
        ## for our right half, recursively call self.helper on the left subtree section of the preorder list
        ## as well as the right half of the inorder list (everything beyond the index of current root)
        root.right = self.helper(preorder[m+1:],inorder[m+1:])
        
        ## by the end, we would've recursively built both left and right subtrees in our root.left and root.right
        ## so we can just return the root at the end
        return root
