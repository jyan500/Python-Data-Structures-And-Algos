class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = 0
        r = 0
        # to alternate between words, first add word1[l] to res, then word2
        # then increment both pointers
        while (l < len(word1) and r < len(word2)):
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1
        if l == len(word1):
            for k in range(r, len(word2)):
                res.append(word2[k])
        else:
            for k in range(l, len(word1)):
                res.append(word1[k])
        return "".join(res)