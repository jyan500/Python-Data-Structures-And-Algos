"""
https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode

Floyd's Cycle Detection Algorithm

Example: [1, 3, 4, 2, 2] (where 2 is our answer)
Explanation:

i 0 1 2 3 4
n 1 3 4 2 2

1) Although this is an array, we can treat this as a linked list, where each
value of n points to a particular index i

i.e 
n = 1, points to the value at i = 1 (3)
n = 3, points to the value at i = 3 (2)
n = 4, points to the value at i = 4 (2)
n = 2, points to the value at i = 2 (4)
n = 2, points to the value at i = 2 (4)

0 -> 3 -> 2 -> 4
           \ /

cycle starting from 2

0 cannot be a part of the cycle because the values only go from 1 ... n

2) If there are multiple pointers going to the same node, there will be a cycle

We want to find the start of the cycle and return it using Floyd's algorithm:

- Use fast and slow pointer, starting from 0
- Finds the first position that the fast and slow pointer intersect
- Then, take another slow pointer, and find out where this second slow pointer
and the original slow pointer intersect. This will be the start of the cycle

Explanation behind this:
1) We do the first step (w/ fast and slow pointer) because the distance between the intersection
point found AND the actual beginning of the cycle is the SAME as the distance between the start of the
linked list and the actual beginning of the cycle.
2) That is why we do the second part which starts at the beginning of the cycle again with another slow pointer,
and then moving both slow pointers to find the beginning of the cycle

Watch Neetcode's vid in the link above for the mathematical proof behind why this works

Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      	slow, fast = 0, 0 
      	# find the intersection of the slow and fast pointer
      	while True:
      		slow = nums[slow]
      		fast = nums[nums[fast]]
      		if slow == fast:
      			break

      	slow2 = 0


