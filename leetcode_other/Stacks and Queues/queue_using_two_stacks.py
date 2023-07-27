'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

'''

"""
Revisited on 7/26/2023
https://www.youtube.com/watch?v=EUNGb8PMoCc&ab_channel=HackersRealm

When pushing to the queue, we push onto the self.input stack
When peeking or popping from the queue, if the self.output stack is empty, 
we pop all the elements off of self.input stack, and onto the self.output stack, essentially pushing the elements
into self.output stack in the reverse order

From there, we can either call self.output.pop() or self.output[-1] to get the last element

To check whether the queue is empty, we check both stacks

pop() and peek() are the bottlenecks, both taking at least O(length of the input queue)

example:

enqueue 1
input = [1]
output = []

enqueue 2
input = [1, 2]
output = []

peek
input = []
output = [2, 1]

returns 1

enqueue 3
input = [3]
output = [2, 1]

pop
input = [3]
output = [2, 1]

returns 1

pop
input = [3]
output = [2]

returns 2

pop
input = []
output = [3]

returns 3

"""
class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = self.peek()
        self.output.pop()
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.output) == 0:
            while (len(self.input) != 0):
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0

'''
My initial implementation:

The idea is that a queue is essentially a stack where the items are reversed
To use two stacks, the idea was to use stack1 to keep either the
1) front of the queue or
2) all elements in the queue

Push: Whenever we push, as long as there's an element present in stack1, we push to stack2
Pop: When we pop, we pop off of stack1. 
Key point: However, in the case that our stack1 becomes empty,
we need to pop off all the items in stack2 and place them in stack1. This is because we
need stack1 to always have the front of the queue present, and doing this reverses the items in stack2 and places them in stack1. 
In the case that our stack1 is not empty, we would not need to do
this transfer of data since our stack1 already contains the front of the queue.

translating this into using two stacks,
stack1 = []
stack2 = []

if I were to push 1, put it into stack1 first
stack1 = [1]
stack2 = []

now any element onwards, push onto stack2 instead, for example to push integers 2 and 3
stack1 = [1]
stack2 = [2,3]

now to pop an element, pop 1 off of stack1 (which represents the front of the queue)
now, we also need to iterate through stack2 and pop off the elements and place them in stack1

stack1 = [3,2]
stack2 = []

now if we were to push 4 and 5
stack1 = [3,2]
stack2 = [4,5]

now if we were to pop, since there's already an element present in stack1, we just pop 2 off of stack1
and keep stack2 as is
stack1 = [3]
stack2 = [4,5]

Time complexity:

In this implementation, push would be O(1), and pop is O(N). For N pops, it would be O(N^2), because
whenever we pop, in the case where our stack1 becomes empty constantly, we'd iterate 
through stack2 in reverse each time. According to leetcode though using amortized analysis,
the number of times pop is called is limited by the number of push operations before it. Therefore,
pop is only an expensive operation once per n times (queue size), when stack1 is empty and there is a need
for data transfer between stack2 and 1. The total time complexity is n (for push operations) + 2*n(for the first pop operation)
+ n-1 (for pop operations), which is O(2N), and we divide by this by O(2N) for any remaining pop operations where the stack1 is empty,
leaving O(1) average time per operation.

Space complexity:
I think it'd be O(2N) to store queue elements
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if (len(self.stack1) == 0):
            self.stack1.append(x)
        else:    
            self.stack2.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        
        if (len(self.stack1) > 0):
            to_return = self.stack1.pop()
            if (len(self.stack1) == 0):
                while(self.stack2):
                    self.stack1.append(self.stack2.pop())
                # print('stack1: ', self.stack1)
                # print('stack2: ', self.stack2)
            return to_return

    def peek(self) -> int:
        """
        Get the front element.
        """
        if (len(self.stack1) > 0):
            return self.stack1[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()