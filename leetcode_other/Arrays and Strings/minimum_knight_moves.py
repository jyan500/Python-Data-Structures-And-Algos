"""
https://leetcode.ca/all/1197.html
https://www.youtube.com/watch?v=OgPUNRLSp_c&ab_channel=HappyCoding
https://stackoverflow.com/questions/76545893/why-is-knights-shortest-path-algorithms-time-complexity-om-n-with-breadth-f
Time Complexity: O(X^2 + Y^2) 
Space Complexity: O(X^2 + Y^2)
See the explanation on stackc overflow about the complexity
"""

class Solution:
	def __init__(self):
		pass

	def minimumKnightMoves(self, targetX: int, targetY: int) -> int:
		from collections import deque
		"""
		One trick is that because the board is symmetric, we can reduce the search space
		by converting the targets to be positive, so that we only need to search the top right quadrant.
		We still need 8 directions below though since it's possible we could be moving in all 8 directions
		within the top right quadrant
		""" 
		targetX = abs(targetX)
		targetY = abs(targetY)

		# knight starts from 0, 0
		knightDirections = [(1,2), (2,1), (1, -2), (2, -1),
		(-1, 2), (-2, 1), (-2, -1), (-1, -2)]

		# Perform BFS, keeping track of number of moves made, along with the current position within the queue
		q = deque()
		q.append((0,0,0))
		visited = set()
		visited.add((0,0))

		while (q):
			i, j, numMoves = q.popleft()
			if i == targetX and j == targetY:
				return numMoves
			for x, y in knightDirections:
				newX, newY = i+x, j+y
				"""
				assuming our target is always in the top right quadrant
				and the fact that a knight can move at most 2 squares,
				if the proposed position (newX, newY) is in bounds such that you're moving at most one knight move out of the top right
				quadrant (which is newX = -2, newY = -2), and one knight move away from our target (which is targetX + 2, targetY + 2),
				move the knight to that position.
				this to prevent us from moving in a direction that wouldn't help reach the target.

				-2 is to help the knight move backwards, and then forwards again towards the target
				targetX/targetY + 2 is to help the knight move forwards, and then backwards towards the target
				"""
				if (newX, newY) not in visited and -2 <= newX <= targetX + 2 and -2 <= newY <= targetY + 2:
					q.append((newX, newY, numMoves + 1))
					visited.add((newX, newY))

s = Solution()
print(s.minimumKnightMoves(1, 1)) # expect 2
print(s.minimumKnightMoves(-3, 0)) # expect 3
print(s.minimumKnightMoves(5, 5)) # expect 4
			

