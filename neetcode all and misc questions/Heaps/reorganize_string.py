# revisited on 1/28/2025 with a similar solution
class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        1) keep track of the counts of characters using hashmap
        2) Place the counts and the character as a tuple onto a max heap.
        3) since none of the characters can be next to each other,
        you'd want to keep track of the previous character that was picked,
        and then choose a different character. Another condition is that you want
        to pick a different character that has the highest count among all the others, since
        you don't want to end up in a situation where you still have only one type of
        character left, and end up having to place them all next to each other.
        4) If the result string == original string, that means we were able to successfully place all characters
        alternately, otherwise return ""
        """
        from collections import Counter
        import heapq
        counter = Counter(s)
        maxHeap = []
        for key, value in counter.items():
            # negative value because it's a max heap
            heapq.heappush(maxHeap, (-value, key))
        prev = tuple()
        res = []
        while (maxHeap):
            count, char = heapq.heappop(maxHeap)
            count = -1 * count
            # if the previous character has a count greater than 0,
            # add it back to the max heap
            if (len(prev) > 0):
                prevCount = -1 * prev[0]
                if prevCount > 0:
                    heapq.heappush(maxHeap, prev)
            prev = (-1 * (count-1), char)
            res.append(char)
        return "".join(res) if len(res) == len(s) else ""

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Optimized Approach:
        Neetcode: https://youtu.be/2g_b1aYTHeg
        Time: O(NLogN)
        Space: O(N)
        What if instead of backtracking and trying to find each combination, we just started from the character
        with the highest frequent in string s? This way, you first pick the character with the highest frequency,
        then try to alternate with a different character with the next highest frequency, and so on. The tricky part though
        is that after you pick a character, it needs to be "put on hold" until you pick another character. For example:
        "aaabc",
        if you were to pick "a", then "b", then "c", you'd then pick two more "a", which would create "abcaa", which is invalid, when the answer is in fact "abaca".
        To get the valid answer, you'd pick "a", then "b", and then "a" again, then "c", then "a". Essentially,
        once you pick the most frequently occurring char, you have to put that one on hold for one iteration,
        and pick the NEXT most frequently occurring, and at each point, decrement the counts of each character until
        there are no more characters to select.
        
        for example s = "aaabbbc", a result of "abababc" is a valid answer ("ababacb" is also valid)
        pick "a" (count a is now 2) ("a")
        "a" on hold now
        pick "b" (count b is now 2) ("ab")
        "b" on hold now
        pick "a" (count a is now 1) ("aba")
        "a" on hold now
        pick "b" (count b is now 1) ("abab")
        "b" on hold now
        pick "a" (count a is now 0) ("ababa")
        "b" on hold now
        pick "b" (count b is now 0) ("ababab")
        pick "c"
        
        In order to figure out the "next" most frequently recurring character, you could take the max of the hashmap each time, excluding the character that is on hold. But a max heap seems like a more appropriate solution, similar to the task scheduling, you take the element out of the heap when it's on hold, and then after, you can put it back in. A max heap
        also allows you to pop out the top element to get the next frequently reoccuring.
        
        This would take the time complexity down from finding the max of the hashmap each time (O(N^2)) to O(NLogN)
        
        Also, the ordering doesn't matter if two characters have the same count, since we only need to return one valid
        result, and not a particular ordering.
        """
        import heapq
        from collections import Counter
        counter = Counter(s)
        maxHeap = []
        for char in counter:
            heapq.heappush(maxHeap, (-counter[char], char))
        res = ""
        onHold = ()
        while (maxHeap and len(res) < len(s)):
            count, char = heapq.heappop(maxHeap)
            # convert back to positive number
            count = count * -1
            res += char
            # put the previous onHold element back into the maxHeap if it's not zero, converting back to negative
            if (len(onHold) > 0 and onHold[0] != 0):
                heapq.heappush(maxHeap, (onHold[0]*-1, onHold[1]))
            # use the current character, decrement count and put on hold
            onHold = (count-1, char)
        return res if len(res) == len(s) else ""
        """
        Brute Force:
        get all unique combinations of the string and see if any of them have are arranged such that
        any two adjacent characters are not the same. If so, return that string
        
        s = "aab"
        for example:
        "aab", "aba", "baa"
        
        when generating "aba", it would return that string immediately since no adjacent characters are the same
        
        Two check for this condition, we'd have to iterate through the string and check if s[i-1] != s[i],
        and s[i+1] != s[i]
        
        O(N*N!), where N is the length of S, TLE's at test case 22
        
        Slight optimization:
        Instead of getting all combinations and then checking at the end once we've received a combination, we attempt to pick characters that are different from the current character, so we add the check inside the for loop inside
        the permutations algorithm.
        
        for example, given i = 0, inside "aab",
        instead of picking index 1 where (a == a, which breaks the condition), we'd pick index 2 as a != b.
        
        This ensures that the combination make will always end up as valid, so we don't need the extra O(N) to check for adjacency. We can also add a check at the top of the recursion that checks if we've found a valid solution, if so
        just return so we don't continue the recursion any further. This is a slight improvement, but still TLE's, this time at test case 27
        """
        
        """
        self.N = len(s)
        self.res = ""
        def areNeighborsDifferent(substr):
            for i in range(1, len(substr)-1):
                isAdjacencyRule = substr[i] != substr[i-1] and substr[i] != substr[i+1]
                if not isAdjacencyRule:
                    return False
            return True
    
        # same algorithm as permutations
        def search(searchSpace, cur):
            # if we've found a solution, just return
            if (self.res != ""):
                return
            if (searchSpace == ""):
                self.res = cur
            for i in range(len(searchSpace)):
                # if the current character at i is different from the last character of cur, we search
                if (len(cur) == 0 or (len(cur) > 0 and searchSpace[i] != cur[-1])):
                    # the search space is everything up to i and everything after, excluding the element at i
                    search(searchSpace[:i]+searchSpace[i+1:], cur + searchSpace[i])
        search(s, "")
        return self.res
        """

       
      
            
            
                
                    
            