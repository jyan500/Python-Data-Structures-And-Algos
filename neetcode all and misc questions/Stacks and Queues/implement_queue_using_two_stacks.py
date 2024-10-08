"""
https://leetcode.com/problems/implement-stack-using-queues/

Not the fully amortized version, but you can find that 
at neetcode: https://www.youtube.com/watch?v=eanwa3ht3YQ&ab_channel=NeetCodeIO

This version is O(N) pop and peek, while O(1) push and O(1) empty

Revisited 10/8/2024
"""
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
            
    def pop(self) -> int:
        # we need to pop off all the elements in stack 1,
        # and append to stack 2 to reverse the order,
        # this way the last element in stack 2 will act as the "front" of the queue
        while (self.s1):
            self.s2.append(self.s1.pop())
        element = self.s2.pop()
        # then we need to add all the elements back to stack 1 in their original order
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return element
        
    def peek(self) -> int:
        while (self.s1):
            self.s2.append(self.s1.pop())
        element = self.s2[-1]
        # then we need to add all the elements back to stack 1 in their original order
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return element

    def empty(self) -> bool:
        return len(self.s1) == 0 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)
            
    def pop(self) -> int:
        """ Using 2 queues (use the other queue to hold the elements that were getting popped off
        in order to get to the "actual" item that needed to be popped at the very right side)"""
        # self.q2 = []
        # while len(self.q1) > 1:
        #     self.q2.append(self.q1.pop(0))
        # # because we can only pop out on the left side of a queue,
        # # continue to pop until we reach the last element. We save
        # # these elements in the other queue so we can set that back to 
        # # q1 later.
        # # finally, pop the last element and return that
        # last = self.q1.pop(0)
        # self.q1 = self.q2.copy()
        # return last
        
        """
        Using one queue
        save the index at the end of the queue
        While we pop, just append the item to the back
        finally pop one last time to get the element we need to pop (which is the top of the stack)
        
        [1, 2, 3]
        
        pop 1, append 1 to the back:
        [2, 3, 1]
        
        pop 2, append 2 to the back
        [3, 1, 2]
        
        pop 3, return 3
        
        """
        end = len(self.q1) - 1
        last = 0
        i = 0
        while (i < end):
            self.q1.append(self.q1.pop(0))
            i += 1
        # once we get to the end, pop one last time
        last = self.q1.pop(0)
        return last
            
    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()