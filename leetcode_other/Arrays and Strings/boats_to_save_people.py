class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        https://www.youtube.com/watch?v=XbaxWuHIWUs&ab_channel=NeetCode

        Should try to optimize the amount of people per boat to be closest
        to the limit
        
        sort + greedy approach 
        O(NLogN)
        
        After sorting:
        1) if you have two pointers, you can try adding the smallest
        and biggest number together to see if they're under the limit, this way we're making the best
        use of space.
        If so, this will be one boat, and we can move both pointers inwards
        2) If the sum of both numbers exceeds the limit, the right side (which is the greater number
        since it's sorted) will be one boat. We then decrement only the right side, since we
        still need to see if the current left side + another right side element could fit into one boat.
        
        Example:
        1 2 2 3 (limit = 3)
        l = 0
        r = 3
        3 + 1 is greater, so fit 3 in one boat, res = 1, r is now 2
        1 + 2 fits in one boat, res = 2, l = 1, r is now 1
        
        l and r are now the same (points to 2), so we just include the last person
        on their own boat by default and break the loop.
        
        res = 3
        
        1 2 4 5 6 (limit = 6)
        l = 0
        r = 4
        6 + 1 exceeds the limit for one boat, put 6 in one boat, res = 1, r = 3
        
        1 + 5 fits the boat, res = 2, l = 1, r = 2
        2 + 4 fits the boat, res = 3, l = 2, r = 1
        
        loop ends
        
        res = 3
        
        """
        people.sort()
        l = 0
        r = len(people)-1
        res = 0
        while (l <= r):
            if l == r and people[r] < limit:
                res += 1
                break
            if people[r] + people[l] > limit:
                res += 1
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1
        return res