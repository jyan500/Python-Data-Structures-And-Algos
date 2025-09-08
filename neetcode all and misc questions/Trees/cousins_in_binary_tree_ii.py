# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        level order traversal, but each level, we can track the root's parent value, so when we have all the 
        nodes at each level, we can get all the nodes which are on the same level, but don't share the same parent,
        and then sum those.

        For some reason, this didn't seem to work, so I'm going with the editorial solution instead:
        The editorial solution:
        2 Pass BFS

        1) the first pass, you calculate the sum at each level, and then store in a hashmap that maps the current
        level index to its total sum
        2) the second pass, at each level, you're essentially setting the values for the level "below" the current level.
        Similar to above, you pop off the node, but then check whether the node has left and right children.
        If so, you sum these two together to form the sibling sum, and then you would set the node.left child's value by subtracting the totalSum of that level
        (which was stored in the hashmap) and the sibling sum, this would give you the cousin sum.

            5
        4       9
    1      10     7

        In the example above, you'd get the total sums at each level with the first pass of BFS
        levelSums = {0: 5, 1: 13, 2: 18}

        In the second pass of BFS, you'd actually start at level index 1 instead of 0, since the root
        cannot have any cousins

        from here, you'd initially pop out 5 from the queue, and then check its left and right children (4 and 9)
        since we the sibling sum here is 13 and the total sum is also 13, we'd set the values of left and right children to 0

        In the next pass, we now have 4 and 9 on the queue
        4's children are 1 and 10. We can sum these two together to get 11, and we know the total is 18. Therefore,
        the cousin sum is 7, and we'd set the left and right children to 7

        Similarly for 9, the child is only 7. Since there's only a right child, the cousin sum would be 18 - 7, which is 11,
        so we'd set the node.right to be 11

        """
        from collections import deque, defaultdict
        q = deque()
        q.append(root)
        levelSums = defaultdict(int)
        levelIndex = 0
        while (q):
            N = len(q)
            for i in range(N):
                node = q.popleft()
                levelSums[levelIndex] += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelIndex += 1
        
        # reappend the root, this time set the root val to 0
        q.append(root)
        # set root.val to be 0 since the root cannot have any cousins
        root.val = 0
        # we're now looking at each level below the current level, so set levelIndex to 1
        levelIndex = 1
        while (q):
            N = len(q)
            for i in range(N):
                node = q.popleft()
                siblingSum = 0
                # get the sibling sum by adding the left and right val's together if they exist
                if node.left:
                    siblingSum += node.left.val
                if node.right:
                    siblingSum += node.right.val
                # the sum that we should be setting for the children below would be
                # the totalSum for the level below - siblingSum
                cousinSum = levelSums[levelIndex] - siblingSum
                if node.left:
                    node.left.val = cousinSum
                    q.append(node.left)
                if node.right:
                    node.right.val = cousinSum
                    q.append(node.right)
            levelIndex += 1

        return root