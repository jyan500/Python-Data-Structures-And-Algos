"""
https://leetcode.com/problems/design-circular-queue/
See https://www.youtube.com/watch?v=aBbsfn863oA&ab_channel=NeetCode
for in depth explanation and illustration


left dummy 
          ->
          <- 
                node
                      ->
                      <- 
                           right dummy

Note that the problem mentions the benefit of using a circular queue is that it makes use of the spaces in front of the queue,
but the solution below "cheats" in that it's not really circular, it's a double linked list where you can simply "shift" the pointers
whenever you need to add or remove something. It might be worth looking at how the problem should be done without a doubly linked list
(i.e when using an array like mentioned by Neetcode)

left dummy 
        <-
        ->
           node #1
                <-
                -> 
                  node #2
                      <-
                      -> 
                         right dummy

adding nodes would start from the right dummy and go backwards by one (say adding a node #3 after node #2)
removing nodes would start from the left dummy and go forwards (say remove node #1)
"""
class ListNode:
    def __init__(self, val, nextNode = None, prevNode = None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.leftHead = ListNode(0)
        self.rightHead = ListNode(0)
        # initially, the left head's next will point to the right head
        # and the right head's prev points to the left head
        self.leftHead.next = self.rightHead
        self.rightHead.prev = self.leftHead

    def enQueue(self, value: int) -> bool:
        # we can only add if there's enough space
        if (self.isFull()):
            return False
        # whenever we add an element to the queue
        # we add it to the back of the queue
        # we set the next Node of the new Node to be the dummy right
        # and the prev Node to be the previous node of the dummy right
        """
        dummy 
        left -> 
             <- prev node 
                          ->
                          <- 
                             New Node
                                      ->
                                      <-  dummy right
        """
        newNode = ListNode(value, self.rightHead, self.rightHead.prev)
        # before we re-assign self.right.prev,
        # update the self.right.prev so it points to the new node
        previousNode = self.rightHead.prev
        previousNode.next = newNode
        # now assign self.right.prev to be the newNode
        self.rightHead.prev = newNode
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        # we can only dequeue if the queue is not empty
        if (self.isEmpty()):
            return False
        # we always remove elements from the front, so we find the node after the left dummy
        """
        dummy left
                  ->
                  <-
                     node to remove
                                     ->
                                     <-
                                        node after
                                                   ->
                                                   <-
                                                      dummy right
        if we remove "node to remove", we set
        dummy.left.next = dummy.left.next.next
        
        after we set dummy left to "node after" in the image, we'd need to set
        "node after" to dummy left
        """
        self.leftHead.next = self.leftHead.next.next
        self.leftHead.next.prev = self.leftHead
        self.space += 1
        return True

    def Front(self) -> int:
        # the front of the queue should be one space after the dummy left node
        if (self.isEmpty()):
            return -1
        return self.leftHead.next.val

    def Rear(self) -> int:
        # the back of the queue should be one space before the dummy right node
        if (self.isEmpty()):
            return -1
        return self.rightHead.prev.val

    def isEmpty(self) -> bool:
        # if the left head's next points to the right head
        # and the right head's prev points to the left head, that means there's no nodes between them, so the queue is empty
        return self.leftHead.next == self.rightHead and self.rightHead.prev == self.leftHead

    def isFull(self) -> bool:
        # if the original space has been decremented to 0, should be full
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()