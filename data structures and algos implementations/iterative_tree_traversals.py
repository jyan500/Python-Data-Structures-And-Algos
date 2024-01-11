'''
In general, we need to use a stack for iterative tree traversals in order to keep track of nodes to backtrack and visit nodes

Iterative In Order Tree Traversal
https://www.youtube.com/watch?v=nzmtCFNae9k&ab_channel=TusharRoy-CodingMadeSimple

Preorder Traversal
https://www.youtube.com/watch?v=elQcrJrfObg&ab_channel=TusharRoy-CodingMadeSimple

Postorder Traversal
https://www.youtube.com/watch?v=xLQKdq0Ffjg&ab_channel=TusharRoy-CodingMadeSimple
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

## postorder is go left, right and then visit node
## note that this implementation uses 2 stacks (we'll call it S1 and S2)
## the idea is that you first put the root into S1, pop it and then push it into S2
## eventually, all the nodes that were visited will be in S2, and if you were to pop off
## every node in S2, it'd print out in postorder traversal

def iterativePostorder(root):
	if (not root):
		return
	s1 = [root]
	s2 = []

	while (len(s1) > 0):
		root = s1.pop()
		s2.append(root)
		if (root.left != None):
			s1.append(root.left)
		if (root.right != None):
			s1.append(root.right)
			
	while (len(s2) > 0):
		root = s2.pop()
		print(root.val)
