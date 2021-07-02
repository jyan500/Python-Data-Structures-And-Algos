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
