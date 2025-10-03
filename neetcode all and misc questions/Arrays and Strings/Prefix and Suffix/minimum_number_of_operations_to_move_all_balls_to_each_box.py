class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        O(N^2) Time, O(1) space 
        nested loop method:
        res = [0, 0, 0]
        perform a nested loop, within the nested loop, check
        if boxes[j] == 1, if so take abs(j - i) to determine the amount of steps needed to move
        the ball from j to i. Then add res[i] += (j-i)
        """
        # res = [0] * len(boxes)
        # for i in range(len(boxes)):
        #     for j in range(len(boxes)):
        #         if boxes[j] == "1":
        #             res[i] += abs(j-i)
        # return res
        """
        Prefix and Suffix solution
        O(N) Time O(1) Space
        The key insight here is that we can use two loops,
        1) one loop to calculate the amount of moves necessary
        for all balls that are moving to the left towards the target
        2) another loop to calculate the amount of moves necessary for all moves moving to the right
        towards the target

        the reason this works is the idea that the amount of moves necessary "accumulates" as we calculate from one direction

        for example:
        boxes = "11001"
        at i = 0
        there's one ball here, 0 moves necessary so far
        at i = 1
        because know there's one ball to the left here, it'd take one move so far,
        but now the amount of balls total is 2
        at i = 2
        here, the accumulation occurs, so we have two balls, we add this to the number of moves so far,
        for a total of 3. This makes sense because it takes 2 steps to move i = 0 to i = 2, and 1 
        step to move i = 1 to i = 2. There's no ball at i = 2 so number of balls stays the same at 2
        at i = 3
        there's no balls here, but the accumulation occurs again because
        we have a total of 3 moves so far, plus 2 balls, for a total of 5 moves. This makes sense because
        i = 0 to i = 3 is 3 steps, i = 1 to i = 3 is 2 steps.

        This would be the example coming from left to right, we'd repeat this same thing
        iterating starting from the end of the array to the beginning to get all balls going from right to left.
        """
        res = [0] * len(boxes)
        moves = 0
        ballsBeingMoved = 0
        # calculate the amount of moves necessary to move all balls from left to right towards
        # the target at each i
        for i in range(len(boxes)):
            moves += ballsBeingMoved
            res[i] += moves
            if boxes[i] == "1":
                ballsBeingMoved += 1
        moves = 0
        ballsBeingMoved = 0
        # calculate the amount of moves necessary to move all balls from right to left towards
        # the target at each i
        for i in range(len(boxes)-1,-1,-1):
            moves += ballsBeingMoved
            res[i] += moves
            if boxes[i] == "1":
                ballsBeingMoved += 1
        return res