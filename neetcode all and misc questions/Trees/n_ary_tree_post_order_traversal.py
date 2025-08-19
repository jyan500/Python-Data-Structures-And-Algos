"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        since there are n-ary trees (not just strictly a left and right child), you have to
        loop through all children first, and recur down each child, then after that, visit the current node
        and add it to the global res list.

        Finally, after running the recursion, you can add the root level's value as the last node visited 

        O(N) Time
        O(1) Space (no additional space besides the result)
        """
        if not root:
            return []
        self.res = []
        def search(root):
            if root:
                for node in root.children:
                    # visit all children first, and then
                    # append the current node
                    search(node)
                    self.res.append(node.val)
        search(root)
        self.res.append(root.val)
        return self.res