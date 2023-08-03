"""
https://www.youtube.com/watch?v=qkLl7nAwDPo&ab_channel=NeetCode
https://leetcode.com/problems/min-stack/

Concept:
Keep two stacks
1) One to keep track of regular push, pop, top operations
2) The minStack keeps track of the minimum element at a given point
after a push, pop operation was made
-if a push operation is made, check if the value we just inserted
is less than the top of our min stack
    if so, push the val to the top
    otherwise, add the existing min value again
-if a pop operation is made, pop off the min stack to get the new current min value

Example:
insert 1
stack = [1] minStack = [1]

insert 2, because the top of minStack is 1 and 1 < 2, 1 is still our min element
at this point
stack = [1, 2] minStack = [1, 1]

insert 0, because the top of the minStack is 1, and 0 < 1, 0 is our new min Element
at this point, insert 0
stack = [1, 2, 0] minStack = [1, 1, 0]

pop 0, when popping 0, also pop off the top of the min Stack
stack = [1, 2], minStack = [1, 1]

getMin()
1 is still the min element in our stack which is correct

Time Complexity: O(1) for each operation
Space Complexity: O(2N)
"""

import heapq
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        
        element = self.stack.pop()
        self.minStack.pop()
        return element

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()