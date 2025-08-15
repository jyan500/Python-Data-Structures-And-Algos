class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/defuse-the-bomb/
        
        because the array wraps around, we can make a copy of the array and append it
        to handle the wrap around (so we can just get the next k indices). If K is negative,
        we add the array beforehand, and then we start at the offset instead.
        for example
        [5 7 1 4] k = 3
        5 7 1 4 5 1 7 4
        ^     
        starts at 0

        [2,4,9,3] k = -2
        2 4 9 3 2 4 9 3
                ^
                starts at k = 4
         
        However, we only iterate up to the original length of N, where N is the len of code

        since we are looking at a specific window of either K ahead (or K behind if
        K is negative), we can start a cumulative sum, but whenever we get the next index,
        we just remove the leftmost pointer's value from the sum, so we don't need to 
        recalculate the sum of K ahead (or K behind) each time.
        
        Time: O(N)
        Space: O(1) (no additional space)
        """
        arrayCopy = code + code
        res = [0] * len(code)
        curSum = 0
        if k < 0:
            # find it easier to think of it like subtracting rather than adding,
            # so converting k to a positive number to subtract
            k = abs(k)
            for i in range(len(code), len(arrayCopy)):
                if i == len(code):
                    curSum += sum(arrayCopy[i-k:i])
                    res[i-len(code)] = curSum
                else:
                    # take the previous window and shift it over, removing
                    # the left most element
                    curSum -= arrayCopy[i-1-k]
                    curSum += arrayCopy[i-1]
                    res[i-len(code)] = curSum
        elif k > 0:
            for i in range(1, len(code)+1):
                if i == 1:
                    curSum += sum(arrayCopy[i:i+k])
                    res[i-1] = curSum
                else:
                    # take the previous window and shift it over, removing
                    # the left most element
                    curSum -= arrayCopy[i-1]
                    curSum += arrayCopy[i+k-1]
                    res[i-1] = curSum
        return res
        