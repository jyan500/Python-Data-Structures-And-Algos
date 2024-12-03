"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal

    https://www.youtube.com/watch?v=_8yW-dQVJHM&ab_channel=CrackingFAANG
    https://www.lintcode.com/problem/651/

    The intuition here is that you need to map each node to a set of "indices",
    where root starts at 0, 0.

             3
        9        8             
    4       0 1      7

    *3 would be (0,0)
     9 would be (-1,-1)
     4 would be (-2,-2)
    *0 would be (-2, 0)
    *1 would ALSO be (-2, 0)
     8 would be (-1, 1)
     7 would be (-2, 2)

    because 3, 0 and 1 are all share the same Y value (of 0), that means
    they are in the same column, so in that case, in the output, these would need to
    be in sorted order by their "X" coord. So in this case, 3 would come first since it's at 0,
    and then 1, 0 come after since their X is at -1

    Approach:
    1) Create defaultdict that maps the X, Y value coordinate to a list of nodes that have that coordinate
    2) Apply tree traversal, but pass in X, Y and root as parameters
    3) At each recursive call, when going to the left, you'd decrease the Y values. When going right, you'd increase Y.
        also map a tuple of (node, X value) to the defaultdict based on the current Y value.
    4) Sort by the keys in the default dict to get the column values starting from the left, and parse out the values. If the value of the defaultdict
    has more than one item, sort it by the X coord value

    A slight optimization:

    To avoid having to apply a sort to get the outer keys, you can also get the smallest and largest column that was found by
    tracking a global variable when doing the traversal, and getting the min and max col. Then looping through the dict,
    we can just loop from range(min, maxCol+1) to get the proper range

    This can bring the time complexity down to O(N + (K * MLog(M)), where K is the width of the tree (i.e amount of cols), and M is the 
    amount of values that share the same column value

    Space: O(N)


    """
    def verticalOrder(self, root):
        from collections import defaultdict 
        if not root:
            return []
        mapping = defaultdict(list)

        def traverse(x, y, root):
            if root: 
                mapping[y].append((root.val, x))
                traverse(x-1, y-1, root.left)
                traverse(x-1, y+1, root.right)
        traverse(0, 0, root)
        res = []
        sortedCols = sorted(mapping.keys())
        for i in range(len(sortedCols)):
            col = sortedCols[i]
            if len(mapping[col]) > 0:
                # since the X values are in negative, we have to apply -1 * X to get positive
                # in order to sort it in ascending order. 
                sortedSharedColumnValues = sorted(mapping[col], key = lambda x: -1 * x[1])
                res.append([c[0] for c in sortedSharedColumnValues])
            else:
                res.append(mapping[col][0])
        return res

    def verticalOrder2(self, root):
        from collections import defaultdict 
        if not root:
            return []
        mapping = defaultdict(list)

        minMax = [float("inf"), float("-inf")]
        def traverse(x, y, root):
            if root: 
                minMax[0] = min(y, minMax[0])
                minMax[1] = max(y, minMax[1])
                mapping[y].append((root.val, x))
                traverse(x-1, y-1, root.left)
                traverse(x-1, y+1, root.right)
        traverse(0, 0, root)
        res = []
        minCol, maxCol = minMax
        for i in range(minCol, maxCol+1):
            if len(mapping[i]) > 0:
                # since the X values are in negative, we have to apply -1 * X to get positive
                # in order to sort it in ascending order. 
                sortedSharedColumnValues = sorted(mapping[i], key = lambda x: -1 * x[1])
                res.append([c[0] for c in sortedSharedColumnValues])
            else:
                res.append(mapping[i][0])
        return res
            
