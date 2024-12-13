class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        https://leetcode.com/problems/maximum-swap/
        Time: O(N^2), since we have to perform max() on each iteration potentially.
        Space: O(N) to convert the number into a character list

        figure out the largest digit in the number and its index and try to swap it with the first digit of the number
        if there are multiple large digits that have the same value,
        
        1 2 3 9 9
        
        in this case, you have a choice of swapping index 3 or index 4
        
        swapping index 3 would result in:
        9 2 3 1 9
        swapping index 4 would result in:
        9 2 3 9 1
        
        in this case, since we want the maximum value of the number, we'd pick index 4 instead of index 3,
        such that the smaller number goes further back
        
        8 2 3 9 9
        
        swapping index 3
        9 2 3 8 9
        
        vs 
        
        swapping index 4
        9 2 3 9 8
        
        EDGE CASE:
        However, there are cases where the max value is already at the first index, so you would need to locate the 
        "next" biggest max value
        
        98368
        
        for example, 9 is the max value, and it's already at index 0
        
        so when iterating, you would take the max values of everything after i, [8 3 6 8] instead
        
        in this case, you can see that the "next" greater value is 8, but it's already at index 1, which is 
        where we would want to swap to make the next biggest number, so we continue to iterate and find the next greatest value
        after i, [3 6 8]
        
        here the max value is at 8, and the value at index 2 is 3, so we've found a potential place to swap
        
        in this case, we swap 3 and 8 to form 98863
        
        
        """
        strNum = str(num)
        digits = list(strNum)
        # find the max val that can be swapped to the front
        curMax = 0
        # find the index of the first non-max value
        toSwapIndex = 0
        for i in range(len(digits)):
            # the idea is that if the max value is already at the first index,
            # we have to find the "next" greatest max value, as well as the increment the next spot
            # where you'd potentially swap to (see above example)
            maxVal = max([int(n) for n in digits[i:]])
            if maxVal != int(digits[i]):
                curMax = maxVal
                toSwapIndex = i
                break
        # note that if the max values are already all the first possible positions they can be at,
        # curMax and toSwapIndex would end up both as 0, so we'd just return the number as is.
        if curMax == 0 and toSwapIndex == 0:
            return num
        indices = []
        for i in range(len(strNum)):
            if strNum[i] == str(curMax):
                indices.append(i)
        # pick the greater indices in the case there are multiple, since we want the smaller number to go further back
        # in the number so the bigger number can be in front of it, creating a bigger number overall
        toSwap = max(indices)
        # swap the index where the first non-max value occurred with the indices that would create the biggest number
        digits[toSwapIndex], digits[toSwap] = digits[toSwap], digits[toSwapIndex]
        # convert back to int
        return int("".join(digits))
        