class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        knapsack + sorting (similar to subsets II)
        sorting helps to make the solution more efficient since if we determine
        if curSum + current number > target, we can short-circuit from there without
        needing to explore any more possibilities for this combination

        similar to subsets ii, we have a "choose the next index" option, but also the skip option.
        However, in the case of the skip option, we also need to include a loop that skips over an
        index that would cause us to go down the same recursive path and pick a redundant option

        target = 5
        [1,1,4]

        in this example, you could make [1,4] with index 0 and index 2 AND
        [1,4] with index 1 and index 2, but you should only include one of these combinations.
        Therefore:

        let's say you went down the path 0 -> 1 -> 2, which equaled 6, backtracked once, skipped and
        got [1,4] with index 0 and index 2. Now if we were to backtrack to index 0, skip index 0,
        and start from 1, we'd get [1,4] again. To prevent this from happening, we would loop until
        we have a starting point that was not equal to the current number.

        [1,1,4]
             ^ instead of skipping and adding + 1 to the index, we'd skip here instead

        Time complexity: O(NLogN) + O(2^N)
        """
        candidates.sort()
        N = len(candidates)
        self.res = []
        def search(i, cur, curSum):
            if i >= N or curSum == target:
                if curSum == target:
                    self.res.append(cur)
                return
            # if adding the current exceeds target, break
            if i < N and curSum + candidates[i] > target:
                return
            # take the current
            search(i+1, cur + [candidates[i]], curSum + candidates[i])
            # skip, but make sure we don't reanalyze values that are the same as the current
            # note that this doesn't mean we only take unique values in our combination!
            # because the case above actually handles that for us (like having [1,1,6] as a legitimate combination)
            k = i
            while (k < N - 1 and candidates[k] == candidates[k+1]):
                k += 1
            # note that we increment k once more so that we end up on the first element that's not actually
            # equal to the value at k
            # i.e if [1,1,4], if the previous loop landed us at index 1, we need to increment once more
            # for the "starting" point to be index 2
            search(k+1, cur, curSum)
        search(0, [], 0)
        return self.res


            