class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        string cannot contain the substring with three of the same characters consecutively
        each character cannot exceed the amount listed for each parameter
        (count of char "a" cannot exceed the value in parameter "a")
        
        get the longest possible happy string
        
        In a similar way to the problem "Reorganize string",
        we can try a similar strategy where you start with the character
        that appears the most. If you reach a point where
        two characters (i.e "aa") have been added, you need to put
        pick the next most frequent character
        """
        import heapq
        maxHeap = []
        options = {"a": a, "b": b, "c": c}
        for key in options:
            if (options[key] != 0):
                heapq.heappush(maxHeap, (-options[key], key))
        cur = ""
        while (maxHeap):
            count, char = heapq.heappop(maxHeap)
            count = -1 * count
            # if we have two consecutive characters already, we cannot
            # add the third, so we have to pick to the next most frequently
            # occuring character instead
            if len(cur) >= 2 and cur[-1] == cur[-2] and cur[-1] == char:
                # if there is no "next" frequently occurring character,
                # break
                if (not maxHeap):
                    break
                count2, char2 = heapq.heappop(maxHeap)
                count2 = -1 * count2
                cur += char2
                count2 -= 1
                # if there are still characters left for the "next" frequently
                # occurring character, push back into the heap
                if count2 > 0:
                    heapq.heappush(maxHeap, (-1 * count2, char2))
            # if we did not reach the condition where we've added two characters in a row (or the max amount of characters we could've added for this character)
            else:
                count -= 1
                cur += char    
            # push back into the heap with the updated value for count
            if (count > 0):
                heapq.heappush(maxHeap, (-1 * count, char))
        return cur
            
            
            