class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        Optimal:
        Using Max Heap
        Time: O(NLogN)
        Space: O(N)
        Neetcode https://youtu.be/zyTeznvXCtg
        When using a max heap, the goal is to push the height distance between heights[i+1] and heights[i], assuming that this is the
        amount of bricks that will be required to cross.
        We continue pushing the height difference onto the max heap until the brick count becomes negative, and we can no longer
        use bricks. At this point, we'd pop off the max heap to indicate that we will expend "one" ladder, which then frees us
        the same amount of bricks as the value of max heap pop(). 
        We'd add the value of bricks back to the brick count since we've freed up those resources now that we've used a ladder
        instead of bricks there, and decrement ladder count by 1

        If there's a height difference, we also need to check if the brickCount - height difference < 0 and ladder count is also 0. If so,
        we can't continue
        heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
        i = 0
        maxHeap = []
        4 > 2, so we don't need to use bricks or ladders here
        
        i = 1
        maxHeap = []
        2 < 7, so there's a height difference of 5
        bricks - height difference = 0 (5-5)
        append 5 to maxHeap
        bricks is now set to 0
        
        i = 2
        maxHeap = [5]
        7 > 6, so we don't need to use bricks or ladders here
        
        i = 3
        maxHeap = [5]
        6 > 9, so there's a height difference of 3
        bricks - height difference = -3 (0 - 3),
        add 3 to the maxHeap 
        
        at this point, bricks < 0, so pop out of the maxHeap and add back into the bricks count
        maxHeap = [5, 3], pops out becomes [3]
        uses 1 ladder here, so ladders = 0
        bricks = -3 + 5 = 2, so now there are 2 bricks available to use
        
        i = 4
        9 < 14, so there's a height difference of 5,
        append 5
        maxHeap = [3, 5]
        
        2 - 5 = -3, so we'd need to pop out the max heap,
        however, we also have no ladders this time, so we can't pop out.
        
        Therefore, because both brick count < 0 and ladder count == 0, we can't continue
        so we'd return 4
        
        
        """
        import heapq
        maxHeap = []
        brickCount = bricks
        ladderCount = ladders
        i = 0
        while ( i < len(heights)-1):
            # if there's a height difference ...
            if heights[i+1] > heights[i]:
                difference = heights[i+1] - heights[i]
                # note that if there's not enough bricks to account for the height difference, and no more ladders,
                # we can't continue
                if (brickCount - difference < 0 and ladderCount == 0):
                    break
                # note for the max heap, we push negative values based on the height difference
                heapq.heappush(maxHeap, -1 * difference)
                brickCount -= difference
                # if there are ladders that can be used, we will pop out of the max heap and use up one ladder,
                # and then add the amount of bricks we saved from using the ladder back into the brick count
                # and decrement ladder count
                while (brickCount < 0 and ladderCount > 0):
                    brickAmt = heapq.heappop(maxHeap)
                    brickCount += (-1 * brickAmt)
                    ladderCount -= 1
            i += 1
        return i
        
        """
        heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
        4 to 2, no need for bricks/ladder because heights[0] >= heights[1]
        2 to 7, can use bricks or ladder. Here the height difference (heights[2] - heights[1] is 5), so 5 bricks
                2 different paths
            used 5 bricks        used 1 ladder
        
        0 bricks, 1 ladder
        7 to 6, no need for bricks/ladder because heights[2] >= heights[3]
        0 bricks, 1 laddder
        6 to 9, no more bricks, so use 1 ladder
        0 bricks, 0 ladder
        9 to 14. No more resources, we've traveled up to heights[4]
        
        going back to the other option of using 1 ladder instead of 5 bricks from earlier ...
        5 bricks, 0 ladder
        7 to 6, no need for bricks/ladder because heights[2] >= heights[3]
        5 bricks, 0 ladder
        6 to 9, use 3 bricks
        2 bricks, 0 ladder
        9 to 14, the height difference is 5, but because we only have 2 bricks, it's not enough,
        so we can only travel up to heights[4] in this case
        
        Looks like a recursion problem? If heights[i+1] > heights[i], we'd have subproblems from here,
        either picking ladder or bricks to use. Likely Brute Force
        
        This seems like a valid solution but it TLE's on leetcode

        """
        # def search(i, bricks, ladders):
        #     if (i < len(heights) - 1):
        #         if heights[i+1] > heights[i]:
        #             difference = heights[i+1] - heights[i]
        #             indexUsingBricks = i
        #             indexUsingLadders = i
        #             # return the max index between using bricks or using a ladder
        #             if (difference <= bricks):
        #                 indexUsingBricks = search(i+1, bricks - difference, ladders)
        #             if (ladders > 0):
        #                 indexUsingLadders = search(i+1, bricks, ladders - 1)
        #             return max(indexUsingBricks, indexUsingLadders)            
        #         else:
        #             return search(i+1, bricks, ladders)
        #     return i
        # return search(0, bricks, ladders)
        
            
            