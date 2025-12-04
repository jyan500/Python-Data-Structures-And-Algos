# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        https://neetcode.io/solutions/construct-binary-tree-from-preorder-and-postorder-traversal

        preorder tells you the order of the roots
        whereas the postorder will tell you what the children are

        Because each value in both traversals are unique,
        and that the postorder gives you LEFT subtree, then RIGHT subtree,
        then ROOT, and preorder gives you ROOT, then LEFT subtree, then RIGHT subtree:

        You can figure out the size of the LEFT subtree by subtracting the distance between
        the index where the root is located and the "leftmost" pointer. In turn, that will also
        help you identify where the "boundary" is within the preorder traversal, so we know
        that one index AFTER the "boundary" would be the right subtree.

        For example:
        preorder 1 2 4 5 3 6 7
        postorder 4 5 2 6 7 3 1

        in preorder, the first node is the root, the second node is the left child
        so we locate 2 withini the postorder

        4 5 2

        and see that the distance between the index and the leftmost pointer (which starts at 0)
        is 3. Therefore, we know that our left subtree is size 3, so
        in our preorder

        1 { 2 4 5 } 3 6 7
        the area wrapped around the curly brackets is the left subtree, since
        its size 3 starting from index 1. Anything after the curly brackets will be the
        right subtree.

        There is an ambiguity here though, where if one of the sides of the tree doesn't exist,
        a postorder traversal doesn't actually tell us whether the side is the right subtree or the left subtree.

        For example:
        [1, 2, 4, 5]
        [4, 5, 2, 1]
        
            1   OR   1
          2            2
        4   5         4  5

        are both valid here based on this traversal.

        So in this case, if there's only one subtree, we just assume its going on the left side, and
        that's okay for the purposes of the problem.

        Would look back on the neetcode video above for more in depth explanation.
        
        O(N) Time O(N) Space
        """
        N = len(preorder)

        # map each postorder value to its index for easier lookup
        # when searching the value from the preorder side
        postOrderIdxMap = {}
        for i in range(len(postorder)):
            postOrderIdxMap[postorder[i]] = i

        def build(i1, i2, j1, j2):
            # stopping condition, i1 exceeds the length of preorder,
            # or j1 exceeds the length of postorder
            if i1 > i2 or j1 > j2:
                return None
            root = TreeNode(preorder[i1])
            # if i1 has not reached i2, that means there is some amount of
            # distance, which means there's nodes that could be used to build subtrees 
            if i1 != i2:
                # the left child is always one value to the left of the root index
                leftVal = preorder[i1+1]

                mid = postOrderIdxMap[leftVal]
                postorderLeftSize = mid - j1 + 1

                """ 
                j1 -> mid represents the start and end for our left subtree as represented in the postorder
                and i1 + 1, i1 + postOrderLeftSIze represents the start and end for our left subtree as represented in the preorder
                
                i1 + postorderLeftSize + 1 represents the start and end for the right subtree in the preorder list, up to i2, which
                would be the last node in the right subtree
                and then mid + 1 -> j2 - 1 represents the start and end for the right subtree in the postorder list,
                where its one after the boundary that represented the left subtree, up to the final index - 1, since
                the last node in the postorder traversal is the root and we don't want to include that.
                """
                root.left = build(i1+1, i1 + postorderLeftSize, j1, mid)
                root.right = build(i1 + postorderLeftSize + 1, i2, mid + 1, j2-1)

            return root
        
        return build(0, N-1, 0, N-1)
        
