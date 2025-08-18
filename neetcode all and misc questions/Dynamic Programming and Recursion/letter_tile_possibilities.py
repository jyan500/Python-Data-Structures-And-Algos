class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        https://leetcode.com/problems/letter-tile-possibilities/
        similar to permutations
        
        keep track of global result set and used set as memoization

        add the current permutation in the parameter to our result set
        within a for loop of elements:
            if index has not been chosen:
                can choose the element at i and then mark it as used 
                recur and keep a parameter with the current
                mark the element at i as false again so another recursive path can take it into account

        Time: O(N*N!) (the process of finding permutations follows a pattern that's similar to n * (n-1) * (n-2) ..., which is N!) within a loop
        Space: O(N*N!)

        Example:
        "AAB"

        Call 1
        choose index 0
        mark it as used
        [True, False, False]

        cur = [A]
        
        Call 2
        add A to res set, {"A"}
        in the loop, index 0 is already used
        try using index 1
        cur = [A, A]
        [True, True, False]

        Call 3
        Add AA to res set {"A", "AA"}
        in the loop, index 0 and index 1 are already used
        try using index 2
        cur = [A, A, B]
        [True, True, True]

        Call 4
        Add AAB to res set, {"A", "AA", "AAB"}
        every index is already used, so there's nothing left to loop and goes back to the previous call

        Call 3
        we unmark index 2 as being used
        [True, True, False]

        Call 2
        Unmark index 1 as being used
        [True, False, False]
        we can now use index 2
        picking "B"
        mark index 2 as used
        cur = [A, B]
        [True, False, True]

        Call 5
        Add AB to res set ("A","AA", "AAB", "AB")
        since we've unmarked index 1 as being used, we can re-use index 1
        picking "A"
        mark index 1 as used
        [True, True, True]

        cur = [A, B, A]

        Call 6
        Add ABA to res set {"A", "AA", "AAB", "AB", "ABA"} 
        every index is used, goes back to recursive call

        Call 5
        we can unmark index 1, but now we have no more indices to use, so go back to Call 2
        [True, False, True]

        Call 2
        unmark index 2 
        index 0 is still marked, so we've explored everything here
        [True, False, False]

        Call 1
        Unmark index 0
        [False, False, False]
        can now try index 1

        cur = ["A"]
        mark index 1 as used
        [True, True, False]

        Call 7
        Add "A" to the res set {"A", "AA", "AAB", "AB", "ABA"}
        we can try index 2 "AB"

        cur = [AB]
        mark index 2 as used
        [True, True, True]

        Call 8
        Add AB to the res set {"A", "AA", "AAB", "AB", "ABA"}
        everything is used

        Call 7
        there's nothing to add here, it'll go all the way back to Call 1, unmarking index 1 and 2 along the way


        Call 1:
        [False, False, False]
        The loop should now be at index 2,
        so we can start at "B"
        [False, False, True]

        Call 9
        Add "B" to the res set, {"A", "AA", "AAB", "AB", "ABA", "B"}
        We can explore 0
        cur = [B, A]
        Mark 0 as used
        [True, False, True]

        Call 10
        Add "BA" to the res set, {"A", "AA", "AAB", "AB", "ABA", "B", "BA"}
        Can explore 1
        cur = [B, A, A]
        Mark 1 as used
        [True, True, True]

        Call 11
        Add "BAA" to the res set, {"A", "AA", "AAB", "AB", "ABA", "B", "BA", "BAA"} 

        Everything is now used across all recursive calls, and back to call 1,
        it will unmark everything and the final loop will end

        Final result of length 8 

        """
        N = len(tiles)
        # keep track of a memoization table that tracks which indices we've already used
        self.used = [False] * len(tiles)
        self.res = set()
        def search(elements, cur):
            # don't add the case where you don't choose any elements to include in the result
            if len(cur) > 0:
                self.res.add("".join(cur))
            for i in range(len(elements)):
                if not self.used[i]:
                    self.used[i] = True
                    search(elements, cur + [elements[i]])
                    self.used[i] = False
 
        search(tiles, [])
        return len(self.res)