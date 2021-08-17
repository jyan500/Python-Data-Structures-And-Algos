'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

https://leetcode.com/problems/path-sum-iii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:     
    def pathSum(self, root: TreeNode, targetSum: int)->int:
        '''
        start adding up to targetSum if our current node is less than targetSum
        traverse down the tree, adding up from root to leaf node
        after calculating all for the root
        preorder traversal
        then we shift root to root.left and find all the path sums from there
        then we shift root to root.right and find all the path sums from there
        repeat for each node
        O(N^2) time complexity
        O(1) Space
        '''
        return self.pathSumHelper(root, targetSum, 0)
    
    def pathSumHelper(self, root: TreeNode, targetSum: int, total: int) -> int:
        total = 0
        if (root):
            ## append the total for first root
            total += self.findPathSum(root, targetSum, root.val)
            ## add the total found in the left subtree
            total += self.pathSumHelper(root.left, targetSum, total)
            ## add the total found in the right subtree
            total += self.pathSumHelper(root.right, targetSum, total)
        return total
            
   
    
    def findPathSum(self, root: TreeNode, targetSum: int, totalSum: int) -> int:
        calc_sum = 0
        ## if the current sum == target, increment the calc sum
        ## we would want to continue the recursion by checking the cases below
        ## in the case that we have a path such as targetsum = 8, 3+5+-3+5, where 3+5 would increment
        ## but 3+5+-3+5 would also work, but since they're in the same path, we need to include both
        if (totalSum == targetSum):
            calc_sum += 1
        ## if root left and root right have values, add the total sum found between the left and right subtrees
        if (root.left != None and root.right != None):
            calc_sum += self.findPathSum(root.left, targetSum, totalSum + root.left.val) + self.findPathSum(root.right, targetSum, totalSum + root.right.val)
        ## if only the left has a value, add the total sum found in the subtree
        elif (root.left != None):
            calc_sum += self.findPathSum(root.left, targetSum, totalSum + root.left.val)
        ## if only the right has a value, add the total sum found in the right
        elif (root.right != None):
            calc_sum += self.findPathSum(root.right, targetSum, totalSum + root.right.val)
        return calc_sum
    
    '''
    1st call
    10
    total_paths += (recursive call to the left, totalsum + root.val = 10)
    
    2nd call
    total_paths += (recursive call to the left, 10 + 5 = 15)
    
    3rd call
    total_paths += (recursive call to the left, 15 + 3 = 18)
    
    4th call
    total_paths += (recursive call to the left, 18 + 3 = 21)
    
    5th call
    return 0
    
    backtrack to 4th call
    total_paths += 0
    total_paths += (call to the right, 21)
    
    6th call
    total_paths += call to the left (21 + - 2)
    return total paths = 0
    
    that is none,
    
    backtrack to 4th call again
    and we've seen both left and right sides, so return total_paths, 0
    
    
    
    '''