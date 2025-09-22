# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Revisited 9/22/2025 with a fix, the test cases got updated so the solution below has been edited.

        Solved 6/20/2025, was able to solve without a guide in ~30 mins, level order traversal seemed quite natural here.
        https://leetcode.com/problems/check-completeness-of-a-binary-tree/

        every level (except the last) is filled
            this means that every node (in the n-2 level, where n is the height) has two children
        nodes on the last level are as far left as possible
            this means that in the last level (Beyond the last node in that level), there no "gaps" between nodes
        
        Since we're looking at this by levels, it makes sense to perform a level order traversal, which uses BFS
        1) First, get the height of the tree using recursion
        2) Perform BFS starting from the root of the tree
            -store each node in this level in a list
            If one of the nodes doesn't have 2 children, and we're at a level before the n-2 level, return False,
            since this means the level below is not fully filled with nodes.
            If we're on the N-2 level, we then put a condition where we allow null values, and we add them 
            to the level.
            
            - append the list to a result list (to form a nested list of all the levels)
        
        Once we have the nested list, we check the last level, and see if there are "gaps":
        last level: [4,5,6, null] , this would be valid since there are no "null" values until after the last value
        last level: [4, 5, null, 7] would not be valid, since there's a "null" gap between values 5 and 7


        EDIT 9/22/2025 due to updated test cases:
        We also have to check on every level above the current level, if the amount of nodes == 2^i,
        where i is the current level (0 indexed), this shows that this level is fully complete.

        Time: O(N)
        Space: O(N)

        """
        def getHeight(node):
            if node:
                return 1 + max(getHeight(node.left), getHeight(node.right))
            return 0
        
        def getLevels(root, height):
            q = deque()
            q.append(root)
            curHeight = 1
            levels = []
            while (q):
                N = len(q)
                level = []
                for i in range(N):
                    node = q.popleft()
                    if curHeight + 1 == height:
                        q.append(node.left)
                        q.append(node.right)
                    else:
                        if node:
                            if node.left:
                                q.append(node.left)
                            if node.right:
                                q.append(node.right)
                    if node:
                        level.append(node.val)
                    else:
                        level.append(None)
                levels.append(level)
                curHeight += 1
            return levels

        height = getHeight(root)
        levels = getLevels(root, height)
        lastLevel = levels[-1]
        for i in range(len(levels)):
            curLevel = levels[i]
            # if we're on the last level, check for gaps.
            # if the previous value is None, but the current is not None, that means there's a gap,
            # return False
            if height - 1 == i:
                for i in range(1, len(curLevel)):
                    if curLevel[i-1] == None and curLevel[i] != None:
                        return False
            # for every level that's not the last level, the amount of values must be equal to
            # 2^h, where h is the current level
            else:
                if 2**(i) != len(curLevel):
                    return False
        return True