class MyStack:

    def __init__(self):
        """
        - whenever you add an element to a queue,
        it always goes into the back first.
        The idea is that one of the queue's only
        contains one element, which would be 
        the "top of the stack", while the rest of the elements
        are in the other queue

        whenever we push a new element, we basically remove the top most element on our designated queue,
        and then push that onto the other queue with the rest of the elements, THEN we push the new element,
        so our designated queue has the element we want if we were to "pop off the stack"

        However, in the case we pop off, then the designated queue becomes empty, so we "transfer" the other elements
        from the remainder of the queue until there's only one left on that side, then the other
        side now becomes the "top of the stack", which is why the boolean variable is needed to keep track.

        One smart thing that is done in the neetcode solution is that after popping and doing the element transfer,
        we can actually "swap" the values in the two queues, so that way, we don't need to have
        a self.isLeftTop variable, since the side that represents the "top of the stack" will always be on one side.

        O(1) push and O(N) pop in order to perform the transfer of elements from one queue to the other

        """
        self.left = []
        self.right = []
        # self.isLeftTop = True

    def push(self, x: int) -> None:
        # we want to push onto the queue that is our designated "top of the stack",
        # making sure that beforehand, we pop off the element on our top, and then push that
        # onto the other queue with the rest of the elements

        """
        if self.isLeftTop:
            if len(self.left) > 0:
                top = self.left.pop(0)
                self.right.append(top)
            self.left.append(x)
        if not self.isLeftTop:
            if len(self.right) > 0:
                top = self.right.pop(0)
                self.left.append(top)
            self.right.append(x)
        """
        if len(self.left) > 0:
            top = self.left.pop(0)
            self.right.append(top)
        self.left.append(x)

    def pop(self) -> int:
        """
        element = -1
        if self.isLeftTop:
            if len(self.left) > 0:
                element = self.left.pop(0)
                # pop all other elements from the right side except the last,
                # so now the right side will only have one element left
                # and that becomes the new "top"
                while (len(self.right) > 1):
                    self.left.append(self.right.pop(0))
        else:
            if len(self.right) > 0:
                element = self.right.pop(0)
                while (len(self.left) > 1):
                    self.right.append(self.left.pop(0))
        self.isLeftTop = not self.isLeftTop
        return element
        """
        element = -1
        if len(self.left) > 0:
            element = self.left.pop(0)
            # pop all other elements from the right side except the last,
            # so now the right side will only have one element left
            # and that becomes the new "top"
            while (len(self.right) > 1):
                self.left.append(self.right.pop(0))
            
            # perform a swap, so now the right side (which only contains one element which is the "new top of the stack",
            # gets swapped back to the left, so now the left will be the "new top of the stack" once again
            self.left, self.right = self.right, self.left
        return element


    def top(self) -> int:
        """
        element = -1
        if len(self.left) > 0 and self.isLeftTop:
            element = self.left[0]
        elif len(self.right) > 0 and not self.isLeftTop:
            element = self.right[0]
        return element
        """
        element = -1
        if len(self.left) > 0:
            element = self.left[0]
        return element

    def empty(self) -> bool:
        return len(self.left) == 0 and len(self.right) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()