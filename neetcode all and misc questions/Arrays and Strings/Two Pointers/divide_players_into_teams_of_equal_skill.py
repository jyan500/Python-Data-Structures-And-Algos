class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        Sorting makes sense here as a greedy approach, because
        in order to find the pairs that equal to the same sum, you need to find the smallest and largest element first and
        attempt to add them,
        and then see if the 2nd smallest and 2nd largest numbers also sum to the same value as before, and so on.

        After sorting, you can use two pointers starting from opposite ends of the array, and then
        moving the pointers inwards to see if the sum of the values at each pointer are equal to each other.

        3 2 5 1 3 4 -> 1 2 3 3 4 5

        1      5
         2    4
           33

        Here, sorting makes it apparent that the pairs (1, 5), (2, 4), (3, 3) are all equal to 6,
        
        from there, you just need to multiply each pair together as you iterate and add to the current sum

        Time: O(NLogN)
        Space: O(1)
        """
        skill.sort()
        prev = 0
        curSum = 0
        l = 0
        r = len(skill) - 1
        while (l <= r):
            if prev != 0 and skill[l] + skill[r] != prev:
                return -1
            prev = skill[l] + skill[r]
            curSum += (skill[l] * skill[r])
            l += 1
            r -= 1
        return curSum