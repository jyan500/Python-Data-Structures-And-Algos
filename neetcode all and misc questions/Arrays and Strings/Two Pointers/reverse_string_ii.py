class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        only reverse for every other 2k characters

        ab cd ef g
        -> output
        ba cd fe g

        use a loop that skips by 2, and then every other value,
        don't perform the operation. We can keep a separate
        counter that goes by 1, so we can perform the modulus operation
        to see if it's odd or even

        We then perform reverse operations for every 2k characters

        Time Complexity: still O(N), because we perform an O(K) amount of operations for a total of
        N/2K times, so N/2K * K would be O(N/K), which is still O(N), since K is constant

        Space: O(N) (conversion of the string to a list)
        """
        j = 0
        charList = list(s)
        def reverse(l, r):
            while (l <= r):
                charList[l], charList[r] = charList[r], charList[l]
                l += 1
                r -= 1
        for i in range(0, len(charList), k):
            if j % 2 == 0:
                # reverse this segment
                if i+k-1 < len(charList):
                    reverse(i, i+k-1)
                # reverse the whole string if the k value is greater than the length
                # of the whole string
                else:
                    reverse(i, len(charList)-1)
            j += 1
        return "".join(charList)