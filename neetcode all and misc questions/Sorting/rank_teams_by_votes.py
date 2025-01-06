class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        https://leetcode.com/problems/rank-teams-by-votes/
        https://leetcode.com/problems/rank-teams-by-votes/solutions/1429852/python-o-n-logn-solution-explained-easy-understanding

        ** How Python compares lists using greater than or less than operators **
        https://stackoverflow.com/questions/62406227/how-does-python-compare-two-lists-of-unequal-length

        Approach:
        Custom Sorting + understanding how Python compares to integer lists together.

        1) Create a ranking system for each char of each string in the array
        i.e ["ABC","ACB","ABC","ACB","ACB"]
        d = {
            "A": [0, 0, 0],
            "B": [0, 0, 0],
            "C": [0, 0, 0]
        }
        2) For each char in the string, we add 1 to the position they are ranked

        i.e d["A"] = [5, 0, 0] because A is ranked first 5 times, second 0 times and third 0 times
        d["B"] = [0, 2, 3] because B is ranked second 2 times and third 3 times
        d["C"] = [0, 3, 2] because C is ranked second 3 times, and third 2 times

        3). Sort d.keys() based on their ranking values in dictionary, in descending order.
        In case of equal votes, we initially order the keys first using .sort()

        i.e
        when doing comparison of the keys, it will compare the ranking arrays to each other.
        initially when sorting the letter keys by alphabetical order first in case of equal votes
        sortedKeys = ["A","B","C"]
        then
        if we compare the ranking array of A to ranking array of B
        [5, 0, 0] compared to [0, 2, 3]
        in Python, when comparing two lists to each other, it compares the elements
        at each index together until one of the lists ends.
        So [5, 0, 0] > [0, 2, 3] because at index 0, 5 > 0
        [0, 3, 2] > [0, 2, 3], index 0 values are the same, but at index 1, 3 > 2,
        That's why the sorted keys ends up being "A", "C" ,"B"

        4) Join elements in the sorted list into a string and return

        time: O(num of strings * length of each string + NLogN), because
        the length of each string is at most 26 characters as stated in the problem,
        this causes num of strings * length of each string to be considered constant.
        So it's actually O(NlogN)

        space: O(N*S)
        """
        from collections import defaultdict
        d = {}
        for vote in votes:
            for i, char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1
        votedNames = sorted(d.keys())
        return "".join(sorted(votedNames, key=lambda x: d[x], reverse=True))
        