class Solution {
    /**
     * @param {string} s
     * @param {string[]} dictionary
     * @return {number}
     */
    minExtraChar(s, dictionary) {
        /*
        6/15/2026
        first attempt:
        check each window for the presence of the substring 
        anytime you find the window, replace those characters with asterisks

        the issue with this solution is in cases like so:
        s="minminaabcu"
        dictionary=["a","min","abc"]
        you can't remove all the instances of "a", and then
        attempt to check all instances of "abc", since you would've caused
        a side effect by replacing those characters, so "abc" is no longer found.

        As a result, this problem requires backtracking to solve.
        
        Solution: 
        at each position in the string, you can either
        1) skip the current character (count it as extra)
        2) try to match a dictionary word starting at this position

        If a word matches, jump past it without counting those characters as extra
        note that since we try each word in the dictionary, we also have to
        have MIN (choosing this match, current best match)

        in the recurrence relation, you want to check the MIN( skipping current char, matching a dictionary word )
        so we get the most optimal solution

        base case: if i >= len(s) return 0 (no extra characters and no characters to match)

        To memoize, at each i, we store the best possible result (least amount of extra characters based
        on whether we skip or attempt a match) so we don't recalculate if we visit the same index i multiple times

        Time: O(N*M*k), where M is the amount of words in the dictionary and N is the size of the string, and k is the length of the given word in the dictionary
        that we're slicing
        Space: O(N)
        */
        let N = s.length
        let memo = {}
        const dfs = (i) => {
            if (i >= N){
                return 0
            }
            if (i in memo){
                return memo[i]
            }
            // skip results in one extra character added so add 1 to the recurrence relation
            let skip = 1 + dfs(i+1)
            let match = Number.POSITIVE_INFINITY
            for (let word of dictionary){
                let substring = s.slice(i, i+word.length)
                if (substring === word){
                    // determine the best word to choose that yields
                    // the least extra characters
                    match = Math.min(dfs(i+word.length), match)
                }
            }
            memo[i] = Math.min(match, skip)
            return memo[i]
        }
        return dfs(0)
        
    }
}
