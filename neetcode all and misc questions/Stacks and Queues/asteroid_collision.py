"""
Revisited on 3/3/2025, 
this is a much cleaner solution by
appending the current asteroid first. And then, performing the while loop, 
checking if there's at least two asteroids in the stack first, and then checking
if the top 2 asteroids in the stack are colliding (i.e 2nd to top is positive, and top is negative,
meaning it's a right - left collision)

O(N) Time
O(N) Space
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            stack.append(asteroids[i])
            while (len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0):
                first = stack.pop()
                second = stack.pop()
                if abs(first) > abs(second):
                    stack.append(first)
                elif abs(second) > abs(first):
                    stack.append(second)
                # if they're the same, the asteroids explode
                # and there's no need to re-add to the stack
        return stack
"""
Revisited on 1/13/2025
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if len(stack) > 0:
                # the asteroids only collide if the top of the stack is positive (moving right)
                # and the current asteroid is negative (moving left)
                while (len(stack) > 0 and stack[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i]) > abs(stack[-1])):
                    stack.pop()
                if len(stack) > 0:
                    # if the current asteroid is the same and moving in opposite directions, pop()
                    if stack[-1] > 0 and asteroids[i] < 0 and abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop()
                    # if the current asteroid is moving in the same direction
                    # or the top most is negative and the current is positive (Which means
                    # they are not going to collide), append
                    elif (asteroids[i] < 0 and stack[-1] < 0) or (asteroids[i] > 0 and stack[-1] > 0) or (asteroids[i] > 0 and stack[-1] < 0):
                        stack.append(asteroids[i])
                    continue

                    
            stack.append(asteroids[i])
        return stack
"""
https://leetcode.com/problems/asteroid-collision/
Time: O(N)
Space: O(N)

1) Add elements to the stack, but whenever we reach a case
where the top of our stack is positive and the element we want to add
is negative, this indicates a collision
2) Compare the absolute value of both elements to see which asteroid will overtake the other, and
become the new top of the stack
Note that if the absolute values are the same, set to 0 as they will cancel each other out, and
don't add it to the stack

"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            if len(stack) > 0:
                # check for collision
                newTop = asteroids[i]
                while len(stack) > 0 and stack[-1] > 0 and newTop < 0:
                    top = stack.pop()
                    if abs(top) > abs(newTop):
                        newTop = top
                    elif abs(top) == abs(newTop):
                        newTop = 0
                if newTop != 0:
                    stack.append(newTop)
                continue
            stack.append(asteroids[i])
        return stack