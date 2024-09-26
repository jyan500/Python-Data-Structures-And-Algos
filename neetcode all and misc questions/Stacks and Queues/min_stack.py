class MinStack:
    """
    Revisited 9/26/2024
    https://neetcode.io/problems/minimum-stack
    (
    *** Note there's a slight difference between the leetcode version where in this problem,
    the pop() return is void 
    instead int ***)

    use 2 stacks, one that keeps track of the order of the elements
    and the other that keeps track of the current minimum

    Whenever we push an element onto the stack, we check to see if 
    that element is smaller than the top of the min stack. If so,
    then we push the element onto the min stack. Otherwise, we just push another copy
    of the top of the min stack onto itself. This way, it's like a simulation, where
    at each point, we know what the minimum value was.

    push 1
    stack = [1]
    minStack = [1]
    push 2
    stack = [1, 2]
    here, minStack[-1] is 1, 1 < 2, so we push 1 again since 1 is still the min
    minStack = [1, 1]
    push 0
    stack = [1, 2, 0]
    here, minstack[-1] is 1, but 0 < 1, so we push 0 this time
    minStack = [1,1,0]
    Here, get min would return 0
    pop()
    [1, 2]
    [1, 1]
    when we get min, 1 is now the min stack, since at this period of time (After 2 was pushed in),
    1 was still the min.
    """
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minStack) > 0):
            self.minStack.append(val if val < self.minStack[-1] else self.minStack[-1])    
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if (len(self.stack) > 0):
            self.stack.pop()
        if (len(self.minStack) > 0):
            self.minStack.pop()


    def top(self) -> int:
        if (len(self.stack) > 0):
            return self.stack[-1]


    def getMin(self) -> int:
        if (len(self.minStack) > 0):
            return self.minStack[-1]

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