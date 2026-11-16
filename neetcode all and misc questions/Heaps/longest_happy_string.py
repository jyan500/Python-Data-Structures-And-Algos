class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        max heap problem
        trying to apply the cooldown logic from reorganize string, but 
        using the two consecutive rule of checking
        len(res) >= 2 and res[-1] == res[-2] and res[-1] == element

        the tricky part is recognizing that the min heap can be empty, so the loop relies on both the 
        max heap and cooldown being empty. 
        For the edge case c: 5, b: 1, "ccbcc" as the answer, because we get into a situation where
        c is on cooldown, and gets pushed back onto the max heap, with one remaining, once we pop it out,
        we cannot push that onto the res, that would break the two consecutive rule, hence the 
        if (not (....)) condition before res.append

        Time Complexity: O(N), even though there are heappush/heappop operations which are normally O(LogK), 
        the heap is always has a max length of 3 since there are only 3 characters.

        N = a + b + c, the maximum possible length of the output string. 
        The loop runs once per character appended (or a small constant number of times per character, 
        since you sometimes pop two entries when the top letter is blocked by the “no three in a row” rule). That gives:

        O(N) iterations
        O(1) heap work per iteration (at most a couple of pushes/pops on a 3-element heap)
        Total: O(N) × O(log 3) = O(N)

        Space: O(1) (aside from the output string)

        """
        import heapq
        maxHeap = []
        counter = {"a": a, "b": b, "c": c}
        for key in counter:
            if counter[key] > 0:
                heapq.heappush(maxHeap, (-counter[key], key))
        res = []
        cooldown = None
        while maxHeap or cooldown:
            count = 0
            if len(maxHeap) > 0:
                count, element = heapq.heappop(maxHeap)
                count = (count * -1) - 1
                # as long as we do not have two of the same consecutive character, add it to the result
                # for example:
                # c: 5, b: 1, the max we can make is ccbcc, so the extra c can't be added since
                # it would break the two consecutive rule. So when the last c gets pushed back onto
                # the max heap from cooldown, after we pop it out, we cannot add it to the result.
                if (not (len(res) >= 2 and res[-1] == res[-2] and res[-1] == element)):
                    res.append(element)
            # if there's something on cooldown, put it back on the heap as long as its count is not 0
            if cooldown:
                if (-1 * cooldown[1]) > 0:
                    heapq.heappush(maxHeap, (cooldown[1], cooldown[0]))
                    cooldown = None
            if count > 0:
                # if we have two of the same consecutive character already, put it onto cooldown
                if len(res) >= 2 and res[-1] == res[-2] and res[-1] == element:
                    cooldown = (element, -1 * count)
                # otherwise, we put it back on the max heap so it can be re-chosen for a second time if needed
                else:
                    heapq.heappush(maxHeap, (-1 * count, element))
        return "".join(res)

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
            
            
            