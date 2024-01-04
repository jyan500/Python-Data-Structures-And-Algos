# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Neetcode Solution:
		https://www.youtube.com/watch?v=kn0Z5_qPPzY&ab_channel=NeetCodeIO
		
        Time Complexity: O(N^2), because go through every node in the Tree of N nodes
        , and then the actual serialization of each string takes O(N)

        Space Complexity: O(N), there could be N different serializations for each node, which would 
        all be unique keys in the hashmap

        1) Going through each node in the tree, serialize it's subtree starting from the node (as the root)
        as a string using PreOrder Traversal
        2) Use a hashmap where we map the serialized string as a key, and then the value is a list of 
        all the root nodes where their subtree matches this serialization. That way, we can tell if two subtrees mapped to the same thing,
        they must've been duplicates.
        
        - A key with the serialization is that you also need to include the left and right children if they are None,
        otherwise you won't be able to tell the ordering of the roots within the subtree
         i.e 
           1            1
         2   3   VS       2
                            3
                            
        you need to include the empty left and right children of the leaf nodes in the serialization to distinguish these two cases.
       
        the first one using preorder:
        1 2 null null 3 null null
        the second one:
        1 null 2 null 3 null null
        
        Example:
        
             2
           2   2
         3    3
         
        1st recursive call
        s = "2" ... 
        preorder left
        
        2nd recursive call
        s = "2" ...
        preorder left
        
        3rd recursive call
        s = "3" ...
        preorder left
        
        4th recursive call
        there's no left child, so this returns the string "null"
        
        back to the 3rd recursive call
        s = "3", "null"
        preorder right
        
        5th recursive call
        there's no right child, so this returns the string "null"
        
        back to the 3rd recursive call
        s = "3", "null", "null"
        we can now add this subtree into our defaultdict,
        with the serialization as the key and the root node within the list
        
        self.record = { "3,null,null": [root 3]}
        
        back to the 2nd recursive call
        s = "2", "3,null,null", 
        still needs to preorder right
        
        6th recursive call
        There's no right child, so we return the string "null"
        
        back to the 2nd recursive call
        s = "2", "3,null,null", "null"
        
        add this subtree into our default dict
        
        self.record = {
        "3,null,null": [root 3],
        "2,3,null,null,null": [[root 2]]
        }

        back to the 1st recursive call
        s = "2", "2, 3, null, null, null"
        still needs to preorder right
        
        7th recursive call
        s = "2", ...
        preorder left
        
        8th recursive call
        s = "3", ...
        preorder left
        
        9th recursive call
        theres no child here, so return "null"
        
        back to the 8th recursive call
        s = "3", "null"
        still needs to preorder right
        
        10th recursive call
        there's no right child, so return "null"
        
        back to the 8th recursive call
        s = "3","null","null"
        
        we can now add this to self.record, but this time
        *** we meet the condition of duplicates, because
        our serialized string already exists as a key,
        
        self.record = {
        "3,null,null": [root 3],
        "2, 3, null, null, null": [root 2]
        }
        
        therefore we can now add root 3 to our final result array.
        
        ***
        
        back to the 7th recursive call
        s = "2", "3, null, null", 
        preorder right
        
        11th recursive call,
        there's no right child, returns "null"
        
        back to the 7th recursive call,
        s = "2", "3, null, null", "null"
        
        ** once again, we've reached another case where this serialization
        has been found in self.record **
        
        self.record = {
            "3, null, null": [root 3],
            "2, 3, null, null, null": [root 2]
        }
        
        therefore we add root 2 to the final result
        
        back to the 1st recursive call now
        
        s = ["2", "2,3,null,null,null", "2,3,null,null,null"]
        we add "2,2,3,null,null,null,2,3,null,null,null"
        as the last serialization in our self.record
        
        this doesn't have any matching
        
        and then our recursion ends
        
        ******* Returns the final result of [root 3, root2], in leetcode it writes out all the children of the root
        so [3, [2,3]] ************
        """
        
        from collections import defaultdict
        self.record = defaultdict(list)
        self.res = []
        def preorder(root):
            if root:
                s = ",".join([str(root.val), preorder(root.left), preorder(root.right)])
                if len(self.record[s]) == 1:
                    self.res.append(root)
                self.record[s].append(root)          
                return s
            else:
                return "null"
        preorder(root)
        return self.res
        
        