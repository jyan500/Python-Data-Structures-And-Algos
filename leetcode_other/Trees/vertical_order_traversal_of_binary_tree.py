# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## concept is that we use level order traversal using BFS to get the nodes
## and their indices, and store these values in a hashmap
## then based on the column values j within (i,j), iterate through our levels map column wise
## and get the nodes that have a key with that column value j and put them in our result list to return
## Time complexity:
## O(num of nodes) for BFS + O(max_cols * number nodes in our levels map * KLogK), where K is the number
## node values that share the same indices
## Space Complexity:
## O(N) for num of nodes stored in our hash map and queue

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ## level order traversal to get the nodes into a hashmap, storing the indices as a tuple and 
        ## the node's values either as an integer, or a list if two nodes share the same (i,j) value 
        q = deque()
        levels_map = dict()
        q.append((root, (0,0)))
        while (q):
            ## n is the amount of nodes in the queue
            n = len(q)       
            ## for the amount of nodes in the queue
            ## and then for each node, see if there's a left and right, add those to the queue
            for i in range(n):
                node, indices = q.popleft()
                i,j=indices
                ## if the indices are already in our levels map
                if ((i,j) in levels_map):
                    ## check to see if we've started a growing list for shared indices,
                    ## if we have append
                    if (type(levels_map[(i,j)]) == list):
                        levels_map[(i,j)].append(node.val)
                    ## else create the list with the two nodes that are sharing the same indices
                    else:
                        temp = levels_map[(i,j)]
                        levels_map[(i,j)] = [temp,node.val]
                else:
                    levels_map[(i,j)]=node.val
                ## put left children and right children in the queue
                ## and for the left child, it will have indices (i+1,j-1)
                ## for the right child, it will have indices (i+1,j+1)
                if (node.left):
                    q.append((node.left, (i+1,j-1)))
                if (node.right):
                    q.append((node.right, (i+1,j+1)))
        
        ## find the minimum and maximum column values based on the (i,j) keys
        ## that we stored in our levels_map
        min_col = 0
        max_col = 0
        for i, j in levels_map.keys():
            min_col = min(min_col, j)
            max_col = max(max_col, j)
        result = []
        ## iterate through our levels map column-wise
        ## while the min_col is less than or equal to the max column + 1 (less than or equal because
        ## we need to include the value at max_col)
        while (min_col <= max_col):
            ## return a list of lists containing the node values at each column
            inner = []
            for key in levels_map:
                i,j = key
                if (j == min_col):
                    ## one of the requirements is that if there are more than one node
                    ## that share the same indices, we need to return them in sorted order in our result list
                    if (type(levels_map[key]) == list):
                        sorted_list = sorted(levels_map[key])
                        for k in range(len(sorted_list)):
                            inner.append(sorted_list[k])
                    else:
                        inner.append(levels_map[key])
            result.append(inner)
            min_col+=1
        return result
