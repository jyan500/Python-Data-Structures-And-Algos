class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        https://dev.to/elkogit/python-ord-and-chr-3pin
        https://youtu.be/eEUjVY7wK3k
        To optimize, rather than looping through each shift array and then performing the shifts,
        keep track of how many shifts applied to a given character with prefix array. 

        Dry Run example:
        s = "abc" shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
        prefix array = [0,0,0,0]

        first subarray:
        r = 1
        l = 0
        difference value is 0, so shift backwards
        prefix[r+1] -= 1, so prefix[2] = -1
        prefix[l] += 1, so prefix[0] = 1
        prefix is now [1,0,-1,0]

        second subarray:
        r = 2
        l = 1
        difference value is 1, so shift forwards
        prefix[r+1] += 1, so prefix[3] = 1
        prefix[l] -= 1, so prefix[1] = -1
        prefix is now [1,-1,-1,1]

        third subarray
        r = 2
        l = 0
        difference value is 1, so shift forwards
        prefix[r+1] += 1, so prefix[3] = 2
        prefix[l] -= 1, so prefix[0] = 0
        prefix is now [0, -1, -1, 2]

        The second part of the algorithm is accumulating the diffs so we know
        exactly how much to shift for each index. Have to start iterating from the back of the array

        prefix = [0, -1, -1, 2]
        ["a", "b", "c"] (note that in the actual code, these are converted to their unicode number counterparts)
        i = 2
        note that c needs to shift by 2 forwards, so we end up with "e". The diff is now 2
        i = 1
        The diff is now 2 + - 1 = 1
        so b needs to shift 1 forwards, so we end up with "c". 
        i = 0
        the diff is now 1 + -1 = 0
        so a doesn't need to shift

        so the final result is "ace"

        In the actual code itself, the ["a", "b", "c"] needs to be converted to the unicode counterpart first
        by doing ord(the char) - ord("a"). For example, ord("c") - ord("a") would give 99 - 97 = 2

        The reasoning is because when we actually perform the shifts, we have to do a mod operation so that
        we guarantee that we're always within the range of a - z. 
        So for example, if we wanted to shift ord("c") - ord("a") by 2 spots forward.
        2 + 2 = 4, 4 + 26 = 30 and then 30 mod 26 is 4
        To re-convert back to the letter, we would just add ord("a") back to the number 4,
        so 97 + 4 = 101, which corresponds to "e" on the chart.

        in the case we needed to shift ord("a") backwards by 2 for example
        ord("a") - ord("a") = 0
        0 - 2 = -2.
        -2 + 26 = 24 mod 26 is 24.
        ord("a") + 24 = 97 + 24 = 121, which would be "y" according to the chart.
        """
        """
        Brute Force:
        O(N*M)
        res = list(s)
        for l, r, direction in shifts:
            for i in range(l, r+1):
                codeVal = ord(res[i])
                if (direction == 1):
                    if res[i] == "z":
                        codeVal -= 25
                    else:
                        codeVal += 1
                else:
                    if res[i] == "a":
                        codeVal += 25
                    else:
                        codeVal -= 1
                res[i] = chr(codeVal)
        return "".join(res)
        """

        # need the array length to be one more since at 0, there's not going to be any shifts applied
        # in the beginning
        prefix = [0] * (len(s)+1)
        for l, r, direction in shifts:
            prefix[r+1] += (1 if direction > 0 else -1)
            prefix[l] += (-1 if direction > 0 else 1)
        
        diff = 0
        res = [ord(c) - ord("a") for c in s]
        # once the prefix is created, start iterating from the back so that the diff gets accumulated
        # so we know exactly how many shifts are needed for each index.
        for i in range(len(prefix)-1, -1, -1):
            diff += prefix[i]
            # the additional + 26 is to avoid issues when applying mods to negative numbers
            res[i-1] = (diff + res[i-1] +26) % 26
        
        s = [chr(ord("a") + n) for n in res]
        return "".join(s)