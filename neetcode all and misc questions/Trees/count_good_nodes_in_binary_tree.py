"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Time: O(N)
Space: No additional Space (O(1))

Key Concept:
1) My mistake was thinking you need to track the entire path, but really you only need to
keep track of the current maximum in the recursive call stack so far. 

2) Whenever we see a node greater than our current max, we update the current max and
increment the final global result by one since this current node would be considered "good"

For example, in the following tree

        3
     1      4
  3       1   5

Left side:
3 is a good node, because it's current max (the root 3) is greater than or equal to 3, increment res to 1

3 -> 1, 1 is not a good node, because the node <= current max (3) 

1 -> 3, 3 is a good node, because the node >= current Max (3), increment res to 2

So far in this path, there's 2 nodes, but we only needed to track what the current max was through the recursion

Right side:
3 -> 4, 4 is a good node, because the node >= current Max (3), we also update the current max to 4, increment res to 3

4 -> 5, 5 is a good node, because the node >= current Max (5), we also update the current max to 5, increment res to 4

4 -> 1, 1 is not a good node, because the node < current Max (5)

Final result is 4

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Revisited 10/1/2024, same solution as below
        at a given node, it would be helpful if we knew the values of the nodes
        before it on the path. Specifically, we're interested in what the "max"
        we've found so far on this path. Whenever the current max is updated, this means
        this is a "good" node, as there shouldn't be any node we've visited in this path
        with a value greater than this current max.
        
        Traverse the tree, passing down the current max with each recursive call. Whenever
        the current node val >= currentMax (meaning previous nodes CAN be equal to the current max but not exceeding it), increment the count of good nodes by 1,
        and in the next recursive call, pass in the
        current node val instead of currentMax to update it
        """
        self.count = 0
        def search(root, currentMax):
            if root:
                curMax = currentMax
                if root.val >= currentMax:
                    self.count+=1
                    curMax = root.val
                search(root.left, curMax)
                search(root.right, curMax)
        search(root, float("-inf"))
        return self.count            

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0
        def helper(root, curMax):
            if root:
                if root.val >= curMax:
                    self.res += 1
                    curMax = max(curMax, root.val)
                helper(root.left, curMax)
                helper(root.right, curMax)
        helper(root, root.val)
        return self.res