'''
In general, we need to use a stack for iterative tree traversals in order to keep track of nodes to backtrack and visit nodes

Iterative In Order Tree Traversal

'''

class TreeNode:
	def __init__(self, val = 0):
		self.val = val
		self.left = None
		self.right = None

## inorder is: go left, visit current node, go right
def iterativeInorder(root):
	if (not root):
		return
	stack = []
	while (true):
		## if the root is not null, push the current root onto the stack
		## and then traverse the tree to the left child
		if (root):
			stack.append(root)
			root = root.left 
		## if our root is None
		else:
			## to break out of the if the stack is empty, break
			if (len(stack) == 0):
				break
			## else, we pop off of the stack and print our root
			root = stack.pop()
			print(root.val)
			## and then traverse the right side 
			root = root.right

## preorder is visit current node, go left, go right
def iterativePreorder(root):
	if (not root):
		return
	stack = [root]
	while (len(stack) > 0):
		root = stack.pop()
		print(root.val)
		## we check if the current node has a right child first before checking the left
		## so that when we pop off the stack, it'll pop the left child first
		if (root.right != None):
			stack.append(root.right)
		if (root.left != None):
			stack.append(root.left)
