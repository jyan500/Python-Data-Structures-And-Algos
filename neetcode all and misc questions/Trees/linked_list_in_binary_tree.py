# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Neetcode: https://youtu.be/OaA9MgG00AE
        perform traversal of the tree, but also pass in the current head of the linked list
        whenever we see a node.val == head.val, we pass in head.next and search the left and right children
        of the tree
        If the head becomes null, that means we've covered every value in the LL in the current path,
        return true

        we then need to try this search on every node in an outer recursive call

        Time: O(N*M), because in the worst case scenario, we could be running a tree traversal per node (i.e if
        we had a linked list of all 0's except for the last node which is 1, and a tree full of 0's except for 
        one child, which has a value of 1). Since in this case, we'd be performing a traversal for nearly every node of the tree.

        Space: O(N*M) for recursive stack
        """
        def search(node, head):
            if not head:
                return True
            if not node or node.val != head.val:
                return False
            return search(node.left, head.next) or search(node.right, head.next)

        if not root:
            return False
        if search(root, head):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        

        