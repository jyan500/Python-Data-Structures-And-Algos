"""
8/27/2025
Revisited 10/22/2025, reviewing the optimized solution
"""
class Solution:
    def restoreIpAddressesOptimized(self, s: str) -> List[str]:
        """
        Slightly optimized solution that avoids the O(N) work with the joins
        Instead of passing in the remaining list, keep track of the index to determine the remainder
        of the substring to recur on.
        """
        totalDots = 3
        res = []
        N = len(s)
        def isValid(sequence: str):
            # valid if the sequence is between 0 and 255, and the sequence is either a 0, or doesn't contain a leading zero
            return sequence != "" and 0 <= int(sequence) <= 255 and (sequence == "0" or sequence[0] != "0")


        def search(start, numDots, path):
            if numDots == 0:
                # check if the last remaining path is valid, if so add it to the current path
                # and the result
                last = s[start:]
                if isValid(last):
                    path = path + [last]
                    res.append("".join(path))
            
            # choose a sequence between the length 1 to 3, starting at the start index
            for i in range(1, 4):
                # if the new start extends past N, break
                if start + i > N:
                    break
                sequence = s[start:start+i]
                if isValid(sequence):
                    search(start+i, numDots-1, path + [sequence])

        start(0, totalDots, [])


    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Brute Force:

        012201
        you can put a dot after 0
        0.12201
        now you have two parts, 0 and 12201
        0 is a valid portion of an ip address, however
        12201 is not, so you can continue splitting up 12201
        12201
        1.2201 , 1 is valid, 2201 is not valid.
        can add the last . after 2
        2.201
        0.1.2.201 is a valid IP address

        you can now backtrack
        2201, we could try adding a . between 22.01 like so
        0.1.22.01, the problem with this is that 01 is not valid so this won't work.

        try
        220.1, this will work
        0.1.220.1 is valid

        Time Complexity: This is actually O(N) (even though it looks exponential), since we can only place
        at most 3 dots within the string, since you pick a segment that's either 1, 2 or 3 in length, and you can
        only place up to 3 dots, so 3^3 = 27 paths. 
        In each call, the "".join(remaining) causes it to be O(N) 
        Space Complexity: O(N)
        """
        totalDots = 3
        res = []
        def isValidIPSegment(sequence):
            return sequence.isdigit() and int(sequence) <= 255 and (len(sequence) < 2 or (len(sequence) >= 2 and sequence[0] != "0"))
        def search(remaining, numDots, cur):
            # after running out of dots, check if the remaining segment
            # is a valid, if so, add to the current IP address that is stored in cur
            remainingSegment = "".join(remaining)
            if numDots == 0 and isValidIPSegment(remainingSegment):
                res.append(".".join(cur+[remainingSegment]))
                return
            # add a "dot" by splitting everything up to i and everything after
            # if the left portion is valid, we can add that to the cur
            # and recur on the remaining portion on the right
            for i in range(len(remaining)):
                leftPart = remaining[:i+1]
                rightPart = remaining[i+1:]
                leftSequence = "".join(leftPart)
                if isValidIPSegment(leftSequence):
                    search(rightPart, numDots-1, cur+[leftSequence])
        search(list(s), totalDots, [])
        return res
            
            
        
