'''
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

https://leetcode.com/problems/binary-search-tree-iterator/

Concept:
Use an iterative-in order traversal which utilizes a pointer to our root, and a stack.
Whenever we call next(), it will begin the iteration down the left side of the tree, pushing the node we visit to the stack
Until our current pointer is None, it will pop off the stack, save the value that was popped off, set the pointer to the right child,
and return our value.

Although the iteration occurs in a while true loop, since our stack and pointer are class variables,
it will remain intact between each of our next() calls so we can simply resume at the last point in our iteration.

For the hasNext(), we simply need to check if our stack is empty, if the stack is empty, that means
that we're visiting a node we haven't seen yet (the right child), so we just need to check if our current pointer is not None

if our stack is not empty, then we know that there's more nodes to be seen, so just return True
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: TreeNode):
        ## convert the level-order into an inorder traversal
        ## 
        self.pointer = root
        self.stack = []
        
    ## in the worst case, next() would take O(Height of the Tree), because
    ## we could end up continually traverse until the bottom of the tree for one next() call
    ## subsequent calls should take O(1) to pop off our stack
    ## Space Complexity: O(N), to keep track of our stack
    def next(self) -> int:
        ## print('self.stack: ', self.stack)
        ## print('self.pointer.val: ', self.pointer.val)
        ## we can perform an inorder traversal iteratively,
        ## so that at each iteration we can simply return our value
        ## and the next time that next() is called, we can simply resume the iteration
        ## with our self.pointer and self.stack values intact.
        while True:
            if (self.pointer):
                self.stack.append(self.pointer)
                self.pointer = self.pointer.left
            else:
                if (len(self.stack) == 0):
                    return None
                else:
                    self.pointer = self.stack.pop()
                    temp = self.pointer.val
                    self.pointer = self.pointer.right
                    return temp
    ## O(1) time, since this just checks if our stack is empty and if our pointer is not None
    def hasNext(self) -> bool:
        ## if our stack is empty, that means we're traversing into nodes we haven't explored
        ## yet in our tree, so we need to check if our current node is not null
        if (len(self.stack) == 0):
            return self.pointer
        ## if our stack is not empty, that means that we're in the process of popping off,
        ## and our current pointer value is probably at None, so we know there's another node
        ## to be seen, just return True
        else:
            return len(self.stack) != 0

    '''
    test case
    [[7,3,15,null,null,9,20]]
    first call to next()
    self.pointer = 7
    self.stack = []
    first iteration
    -------
    self.stack = [7]
    self.pointer = self.pointer.left = 3
    second iter
    ---------
    self.stack = [7,3]
    self.pointer = self.pointer.left = None
    third iter
    ------------
    self.pointer = self.stack.pop() = 3
    temp = 3
    self.pointer = self.pointer.right = None
    return temp (which is 3)
    
   
    
    second call to next()
    starting values:
    self.stack = [7]
    self.pointer = None
    
    self.pointer = self.stack.pop() = 7
    temp = self.pointer = 7
    self.pointer = self.pointer.right = 15
    return 7
    
    hasNext()
    self.pointer = 15
    self.stack = []
    15 has both left and right child so it should return True
    
    third call to next()
    self.pointer = 15
    self.stack = []
    first iter
    -----------------
    self.stack.append(15) = [15]
    self.pointer = self.pointer.left = 9
    second iter
    -----------------
    self.stack.append(9) = [15,9]
    self.pointer = self.pointer.left = None
    
    third iter
    --------------------
    self.pointer = self.stack.pop() = 9, self.stack = [15]
    temp = 9
    self.pointer = self.pointer.right = None
    return 9
    
    self.stack = [15]
    
    hasNext
    --------------------
    should return true here, even though our current pointer is at None
    we will still pop off and get 15 at the next iteration
    
    fourth call to next()
    ----------------------------------------------------
    self.pointer = self.stack.pop() = 15, self.stack = []
    temp = 15
    self.pointer = self.pointer.right = 20
    return 15
    
    hasNext
    ----------------
    should return true here, our stack is empty, but our pointer is currently at a value
    '''
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()