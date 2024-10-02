'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Revisited 10/1/2024
        Another O(N^2) solution due to the deserialize involving the buildTree
        https://neetcode.io/problems/serialize-and-deserialize-binary-tree

        can serialize into a string containing the preorder and inorder traversals,
        convert each traversal into a string, with a delimiter in between to separate the two
        """
        self.preorder = []
        self.inorder = []
        def preorder(root):
            if (root):
                self.preorder.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
        def inorder(root):
            if (root):
                inorder(root.left)
                self.inorder.append(str(root.val))
                inorder(root.right)
        preorder(root)
        inorder(root)
        return ",".join(self.preorder) + ";" + ",".join(self.inorder)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        parse the serialized string containing the preorder and inorder traversals
        back into the original tree
        """
        preOrderString, inOrderString = data.split(";")
        if preOrderString == "" and inOrderString == "":
            return None
        preOrder = preOrderString.split(",")
        inOrder = inOrderString.split(",")
        def buildTree(preOrder, inOrder):
            if len(preOrder) > 0:
                root = preOrder[0]
                inOrderRoot = inOrder.index(root)
                # inorder determines the left and right subtrees
                inOrderLeft = inOrder[:inOrderRoot]
                inOrderRight = inOrder[inOrderRoot+1:]
                # the preorder left and right determines where the roots are within
                # the left and right subtrees as defined by the inorder left and right
                preOrderLeft = preOrder[1:len(inOrderLeft)+1]
                preOrderRight = preOrder[len(preOrder)-len(inOrderRight): ]
                left = buildTree(preOrderLeft, inOrderLeft)
                right = buildTree(preOrderRight, inOrderRight)
                return TreeNode(int(root), left, right)
        return buildTree(preOrder, inOrder)

## Very slow solution (O(N^2))
## My idea was to use level order traversal to get a tree with similar configuration to the array
## and then use level order insertion to get back the tree
class Codec:
    def __init__(self):
        self.res = []
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if (root != None):
            self.level_order_traversal(root)
            return ','.join(self.res)
        else:
            return ''
        
    
    def checkAllNoneQueue(self, l):
        for i in l:
            if (i != None):
                return False
        return True
    def level_order_traversal(self, root):
        queue = []
        queue.append(root)
       
        while (len(queue) != 0 and not self.checkAllNoneQueue(queue)):
            n = len(queue)
            current_level = []
            for i in range(n):
                cur = queue.pop(0)
                
                if (cur != None):
                    queue.append(cur.left)
                    queue.append(cur.right)
                    self.res.append(str(cur.val))
                else:
                    self.res.append('X')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        """
        if (data != ''):
            self.res = data.split(',')
            root = TreeNode()
            n = len(self.res)
            i = 0
            if (len(self.res) != 0):
                root = self.insert_level_order(root, i, n)
            return root
        else:
            return None
    def insert_level_order(self, root, i, n):
        if i < len(self.res):
            temp = TreeNode()
            if (self.res[i] == 'X'):
                temp.val = 'null'
            else:
                temp.val = self.res[i]
            root = temp
            
            # insert left child
            root.left = self.insert_level_order(root.left, 2 * i + 1, n)
            root.right = self.insert_level_order(root.right, 2 * i + 2, n)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


### O(N) solution
### Turns out that a pre-order traversal can be used to create a copy of the binary treee
### that can be turned into the string

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = self.preorder(root, [])
        return ','.join(result)

    def preorder(self, root, l):
    	if (root is None):
    		l += ['null']
    	else:
    		l += [str(root.val)]
    		self.preorder(root.left, l)
    		self.preorder(root.right, l)
    	return l


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        """
        if (data != ''):
            l = data.split(',')
            print(l)
            return self.construct_tree(l) 
        else:
            return None

    def construct_tree(self, l):
    	if l[0] == 'null':
            l.pop(0)
            return None
    	else:
    		root = TreeNode(l[0])
    		l.pop(0)
            ## construct the left until 'null' is reached
    		root.left = self.construct_tree(l)
            ## then construct right until 'null is reached'
    		root.right = self.construct_tree(l)
    	return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
