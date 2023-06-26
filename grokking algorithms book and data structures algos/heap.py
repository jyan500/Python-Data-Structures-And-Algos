'''
https://www.youtube.com/watch?v=HqPJF2L5h9U&t=1822s&ab_channel=AbdulBari

Heap is a complete binary tree

## Array representation of Heap ## 

if a node is at index i
its left child is at 2 * i
its right child is at 2 * i
its parent is at floor(i/2)

if a node does not have a child, the array must have a "blank" spot in that index

## Complete binary Tree ##

at each height, the binary tree has the maximum number of nodes.
If a node is added, then the height of the tree would be increased.

A node can either have two children or no children to be considered complete,
if you represent the complete binary tree as an array, it should not have any "blank" spots in the array between
existing array elements

## Inserting elements into Heap ##

example for max heap:

	     50
	   /   \
	  30   20
	  /\   / \
	15 10  8  16

[ 50 | 30 | 20 | 15 | 10 | 8 | 16 ]
   
Array representation of the max heap above

To insert the number 60, we'd insert in the first empty position of the array, in this case at the end

[ 50 | 30 | 20 | 15 | 10 | 8 | 16 | 60 ]

             50
	   /   \
	  30   20
	  /\   / \
	15 10  8  16
        /
       60

However, since this no longer meets the condition of a max heap, we need to bubble the node upwards, while
shifting the other elements downwards

            60
	   /   \
	  50   20
	  /\   / \
	30 10  8  16
        /
      15

[ 60 | 50 | 20 | 30 | 10 | 8 | 16 | 15 ]

O(Log(N)) operation, since it depends on the height of the tree

## Deleting Elements in Heap ## 

example for max heap:

	     50
	   /   \
	  30   20
	  /\   / \
	15 10  8  16

[ 50 | 30 | 20 | 15 | 10 | 8 | 16 ]

we always remove the root first (50)

and then take the last element of the array to take its place

             16
	   /   \
	  30   20
	  /\   / \
	15 10  8  16

[ 16 | 30 | 20 | 15 | 10 | 8 |  ]

after that, the element that took the root's place will bubble down, shifting the other element up
until the heap property is met

             30 
	   /   \
	  16   20
	  /\   / 
	15 10  8  

(this is still a complete binary tree)

[ 30 | 16 | 20 | 15 | 10 | 8 |  ]

also a O(Log(N)) operation

## Heap Sort ##  

One important thing to note is that if we were to remove the root and place it as the last element of the array,
if we keep doing this, we'll eventually change the array into sorted order 
(because we'll always take either the next max element for max heap/min element for min heap and place it at the back)
(after deleting 50)
[ 30 | 16 | 20 | 15 | 10 | 8 |  50 ]
 
(after deleting 30)
[ 20 | 16 | 15 | 10 | 8 | 30 | 50 ]

(after deleting 20)

[ 16 | 15 | 10 | 8 | 20 | 30 | 50 ]

This is the basis for heap sort.
In heap sort, we build a heap from the array and then delete the nodes one by one starting from the root,
storing the deleted element in the last free space within the array.
in the end, the array will be sorted

The time complexity of heap sort is O(NLog(N)) because the process of inserting nodes into heap is O(NLogN), and
the process of deleting each node from the heap is also O(NLogN)

## Heapify ##

Heapify is the process of converting a complete binary tree into either a max/min heap
by bubbling down elements (and shifting the resulting elements upwards)

O(N) time process (which is faster than creating a heap which is O(NLogN)) because 
we may iterate through every node once and perform an O(1) swapping operation

Example if we want to build a max heap from this complete binary tree

            10 
	   /   \
	  20   15
	  /\   / \
	12 40 25 18 

(this is still a complete binary tree)

[ 10 | 20 | 15 | 12 | 40 | 25 | 18 ]

Iterate through the array in reverse (starting from right to left)

notice that 12, 40, 25, 18 would be considered heaps (a single node)

once the iteration reaches 15 however, we notice that 25 and 18 are the children, which doesn't meet the requirements
of a max heap

we need to swap 15 and 25

[ 10 | 20 | 25 | 12 | 40 | 15 | 18 ]

now for 20, the children are 12 and 40, we need to swap 20 and 40 to meet the max heap requirements

[ 10 | 40 | 25 | 12 | 20 | 15 | 18 ]

now for 10, the children and 40 and 25, so we need to swap 10 with 40

[ 40 | 10 | 25 | 12 | 20 | 15 | 18 ]

However, we're still not meeting the min heap requirements, so we need to check the children of 10, which is 12 and 20,
so we need to swap 10 and 20 

before additional swap: [ 40 | 10 | 25 | 12 | 20 | 15 | 18 ]
after additional swap: [ 40 | 20 | 25 | 12 | 10 | 15 | 18 ]

Now we are finished 


## Priority Queue ##

FIFO, but each element in the queue has a priority

for min heap, smaller number = higher priority
for max heap, larger number = higher priority

for example, in this queue
Queue = [8 | 6 | 3 | 10 | 5 | 4 | 9 ]

if we were to construct a min heap from this queue, we'd notice 3 is the root
which would be the highest priority.

constructing a priority queue using a heap would allow for O(LogN) insertion and O(LogN) deletion

'''


