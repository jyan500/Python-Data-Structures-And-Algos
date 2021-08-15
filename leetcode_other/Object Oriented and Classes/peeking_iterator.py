'''
Design an iterator that supports the peek operation on a list in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(int[] nums) Initializes the object with the given integer array nums.
int next() Returns the next element in the array and moves the pointer to the next element.
bool hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
 

Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False

https://leetcode.com/problems/peeking-iterator/

Initial Approach was to convert the iterator into a linked list, which supports the peek
and next operations easily since there's always a pointer to the next node

Optimized:
but its possible to do this by just keeping track of the one pointer which is the peeking element
this peeking element will be equal to the value of self.iterator.hasNext() initially, unless
there's no next value, then it'll be None

Time complexity: O(1)
Space: O(1) (No extra space, just the iterator)

'''
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
# class ListNode:
#     def __init__(self, val = 0):
#         self.val = val
#         self.next = None
        

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        # self.root = ListNode()
        # cur = self.root
        ## set our first node to be 0, so once we begin iteration, we'll start at the first element
        ## otherwise our first call to our next() will end up getting the 2nd element instead of the first
        # while (self.iterator.hasNext()):
        #     cur.next = ListNode(self.iterator.next())
        #     cur = cur.next
        self.peeking_element = None
        if (self.iterator.hasNext()):
            self.peeking_element = self.iterator.next()
        
    ## we just need to return the peeking element since this already represents our next element
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # if (self.root.next != None):
        #     return self.root.next.val
        # return None
        return self.peeking_element
    
    ## since our self.peeking_element represents our next element, we would want to store the current value in a temp variable
    ## then, we need to see if our iterator.hasNext()
    ## returns true, if true we can set the peeking element to be the next element of our iterator.
    ## otherwise we would need to set peeking element to None
    ## then return our temp variable
    def next(self):
        """
        :rtype: int
        """
        # if (self.root.next != None):
        #     temp = self.root.next.val
        #     self.root = self.root.next
        #     return temp
        # return None
        temp = self.peeking_element
        if (self.iterator.hasNext()):
            self.peeking_element = self.iterator.next()
        else:
            self.peeking_element = None
        return temp
    
    ## if the peeking element (which represents the next element) is not equal to none
    ## then hasNext should return True
    def hasNext(self):
        """
        :rtype: bool
        """
        # return self.root.next != None
      
        return self.peeking_element != None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].