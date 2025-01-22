# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        delete only the leaf nodes that have the value == target
        if deleting the leaf node causes the parent to become a leaf node with the target value,
        delete that as well.

        Approach:
        Postorder Traversal (left, right then node)
        1) At any point during postorder traversal, if we were to delete a node, we would return null
        in the recursive call. Otherwise, we would return the root.
        2) Upon bubbling back up the recursive call to the parent, say if we were going down the left side,
        and we just hit the leaf node on the left and return null to delete it,
        we would want to set the root.left to be the result of the recursive call. 
        Same idea would apply on the right side.

        In the case where deleting the child leaf node would cause the parent to become a leaf node,
        the condition (if not root.left and not root.right) would check for this. This is why postorder
        is important here, since we would already set root.left to be None before checking for this.

        Time complexity: O(N)
        Space: O(N) for the recursive stack
        """
        def search(root, target):
            if root:
                root.left = search(root.left, target)
                root.right = search(root.right, target)
                # if we're at the leaf node and the node == target, delete this node
                if not root.left and not root.right and root.val == target:
                    return None
                # otherwise, return the root
                return root
        
        return search(root, target)
