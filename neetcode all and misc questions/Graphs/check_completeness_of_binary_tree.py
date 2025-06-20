# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Solved 6/20/2025, was able to solve without a guide, level order traversal seemed quite natural here.
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

        Time: O(N)
        Space: O(N)

        """
        # figure out how many levels there are first by taking the height of the tree
        if not root:
            return True
        def getHeight(node):
            if node:
                left = getHeight(node.left)
                right = getHeight(node.right)
                return 1 + max(left, right)
            return 0
        from collections import deque
        q = deque()
        q.append(root)
        numLevels = getHeight(root)
        curLevel = 1
        allLevels = [[root.val]]
        # if there's only one level, return True by default,
        # since there are no levels below to be filled, so the current level is the last level
        if numLevels == curLevel:
            return True
        while (q):
            N = len(q)
            levelList = []
            for i in range(N):
                node = q.popleft()
                if node:
                    # second to last level, allow null values
                    if curLevel == numLevels - 1:
                        if node.left:
                            levelList.append(node.left.val)
                        else:
                            levelList.append(None)
                        
                        if node.right:
                            levelList.append(node.right.val)
                        else:
                            levelList.append(None)
                        # don't add the last row to the queue, since we don't want all null values
                    else:
                        if node.left and node.right:
                            levelList.append(node.left.val)
                            levelList.append(node.right.val)
                            q.append(node.left)
                            q.append(node.right)
                        # before the second to last level, if there a
                        else:
                            return False
            allLevels.append(levelList)
            curLevel += 1
        lastLevel = allLevels[-1]
        for i in range(len(lastLevel)):
            # if we reach a "None" value, if the values to the right is not None,
            # this means there's a gap, so this level doesn't have all the nodes shifted to the left
            # return False
            if lastLevel[i] == None and i < len(lastLevel)-1 and lastLevel[i+1] != None:
                return False
        return True