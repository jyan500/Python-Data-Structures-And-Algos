"""
https://www.youtube.com/watch?v=b1WpYxnuebQ&ab_channel=NeetCode
Revisited on 11/13/2024 with the same solution
Key Concepts:
1) Preorder Traversal
Node -> Left Subtree -> Right Subtree
2) Important is that each subtree gets wrapped around a set of parenthesis,
however because we don't want the outermost tree with a set of parenthesis (i.e starting with 1 within the representation of 1(2()) ),
we remove the outermost layer after we're doing with the recursion by slicing away the first and last character.
3) Another important edge case for this problem is that if there's a left subtree but no right subtree, we don't need to 
append an extra set of parenthesis. 
*** However, if there's no left subtree but there's a right subtree, we DO need to
append an extra set of parenthesis.

Example:
    1
   2  3
 4

root = [1, 2, 3, 4]

1st recursive call
self.s = ["(", "1"]

goes down the left side

2nd recursive call
self.s = ["(", "1", "(", "2"]

goes down the left

3rd recursive call
self.s = ["(", "1", "(", "2", "(", "4"]

goes down the left,

4th recursive call,
root is None here

goes back to the 3rd recursive call
self.s = ["(", "1", "(", "2", "(", "4"]
this time we go right

5th call
root is None here, return to 3rd recursive call

back to the 3rd call,
we add the closing brace here after the right subtree recursion has been finished
self.s = ["(", "1", "(", "2", "(", "4", ")"]

back to the 2nd call,
we try and visit the right side but there's nothing,
so we add the closing brace here
self.s = ["(", "1", "(", "2", "(", "4", ")", ")"]

back to the 1st call
we visit the right now

6th call:
adds 3
self.s = ["(", "1", "(", "2", "(", "4", ")", ")", "(", "3"]

goes left, nothing
goes right, nothing again, so we add the closing brace
self.s = ["(", "1", "(", "2", "(", "4", ")", ")", "(", "3", ")"]

goes back to the 1st call and adds a closing final brace
self.s = ["(", "1", "(", "2", "(", "4", ")", ")", "(", "3", ")", ")"]

Now after the recursion is done,
we now remove the first and last characters in self.s for our final answer

self.s = ["1", "(", "2", "(", "4", ")", ")", "(", "3", ")"],
after joining = 1(2(4))(3)

2nd Example:

    1
  2   3
   \ 
   4

root = [1, 2, 3, null, 4]

1st call
goes left
self.s = ["(", "1"]

2nd call
self.s = ["(", "1", "(", "2"]

the edge case is reached where root.left does not exist, but root.right does exist (Since root.right is 4)
therefore we append an extra set of parenthesis 
self.s = ["(", "1", "(", "2", "()"]

we go down left but there's nothing, so we return to 2nd call and go down right side

3rd call
self.s = ["(", "1", "(", "2", "()", "(", "4"]

we go down the left and right but there's nothing here, so we return to the 3rd call
and append the closing brace
self.s = ["(", "1", "(", "2", "()", "(", "4", ")"]

we go back to the 2nd call, since we've gone down right, append the closing brace
self.s = ["(", "1", "(", "2", "()", "(", "4", ")", ")"]

the remainder is the same as the first problem

final result is 1(2()4)(3)



"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.s = []
        def construct(root):
            if root:
                self.s.append("(")
                self.s.append(str(root.val))
                if not root.left and root.right:
                    self.s.append("()")
                construct(root.left)
                construct(root.right)
                self.s.append(")")
   
        construct(root)
        return "".join(self.s)[1:-1]

                
                