"""
1/16/2026
https://neetcode.io/problems/perform-string-shifts/question


"""
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # figure out what the net shifts are to avoid
        # simulating all the steps
        # since a left shift and right shift essentially "cancels" the other out
        # for example, a left shift of 1, preceded by a right shift of 1 cancels
        # itself out, and you're just left with the original string
        netShifts = 0
        res = list(s)
        for direction, amount in shift:
            if direction == 1:
                netShifts += amount
            else:
                # left shifts will be counted as "minus" to show that it cancels out
                # the right shifts
                netShifts -= amount
        # if the netshifts is positive, that means the variable represents the amount
        # of positions to shift to the right, otherwise, it shows the amount of positions
        # to shift to the left
        newIndices = []
        if netShifts > 0:
            # calculate the new index where the last character should appear
            # since we're shifting right, we would add the total shifts and mod by the length
            for i in range(len(s)):
                newIndices.append((i + netShifts) % len(s))
        else:
            # for negative numbers, since we're shifting left,
            # in order to get the new index, we would need to add the len(s)
            # back to turn the negative back into a positive number
            # for example:
            # if the overall shift was -1
            # abc -> a would need to be at index 2, so 0 + -1 = -1 + 3 = 2
            # and then mod that by the length again
            for i in range(len(s)):
                newIndices.append((i + netShifts + len(s)) % len(s))
        # i represents the character, and newIndices[i] represents the new index
        # for that character
        # so for example in the string "abc",
        # if we have newIndices = [1,2,0]
        # we interpret this as the character at index 0 ("a") now belongs at index 1
        # so we set res[newIndices[i]] = s[i]
        for i in range(len(newIndices)):
            res[newIndices[i]] = s[i]
        return "".join(res)

class Solution:
    """ 
    Neetcode's solution is that you count all right shifts as "negative", and left shifts as positive
    So that once you can perform list slicing to get the desired shift easier.

    For example:
    abc, [0,1], [1,2], this would result in a net shift of 1 + -2, where the first left shift is considered 1,
    and the second right shift is considered -2, so you'd end up with one right shift to the right, which is 
    designated as -1
    
    You'd then convert this to a positive -1 + 3 = 2, then mod by 3, for a value of 2. So after conversion,
    it's a left shift of 2

    s[2:] + s[:2] = "c" + "ab" = cab



    Something I didn't realize while doing the problem is that you can mod negative numbers
    by positive numbers.
    so -1 mod 3 would be 2 for example, and this would fit the example where
    abc, left shift of -1, so a needs to end up in index 2.

    for example:
    -1 // 3 = .3, so a quotient of 3
    To get mod from here,
    you multiply A by the quotient: -1 * 3 = -3
    and then add to A, which calculates the remainder.

    -1 - (3 * -1) = -1 - (-3) = -1 + 3 = 2

    It doesn't seem like this is something that's consistent across languages so I'd
    still turn the negative back into a positive number first by adding len(s) to the negative number

    """
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        netShifts = 0
        res = list(s)
        for direction, amount in shift:
            if direction == 1:
                netShifts -= amount
            else:
                netShifts += amount
        netShifts = netShifts % len(s) if netShifts > 0 else ((netShifts + len(s)) % len(s))
        res = res[netShifts:] + res[:netShifts]
        return "".join(res)
            

                
            

                