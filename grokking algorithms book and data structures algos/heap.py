'''
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
'''