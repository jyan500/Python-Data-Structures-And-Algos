class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Revisited on 12/12/2025
        https://neetcode.io/problems/subsets-ii
        Time Complexity: O(NLogN + (N * 2^N))
        in order to prevent us from choosing a duplicate,
        we will sort so that after choosing all nums[i] in our subset,
        when backtracking and determining the "next" number we 
        should choose, we can perform a loop to continue
        iterating our i index until it reaches the next number != current number.
        And then continuing the recursion down that index instead. Otherwise,
        if we continued the recursion down i + 1, we'd get duplicate subsets.
        for example:
        1,2,2,3
        at i = 4, if choosing every nums[i], you'd get 1,2,2,3 in the subset.
        at i = 3, you'd get [1,2,2] by not including 3
        when backtracking to i = 2, you'd get [1,2] by not including i = 2 in the subset,
        this would get [1,2,3]
        backtracking to i = 1, this is where the while loop comes in.
        we don't want to include i = 2, otherwise this would give us duplicate subsets 
        since it "reincludes" the value of 2.
        so the while loop moves the pointer to i = 3
        so we'd start from [1] and get [1,3] once choosing the nums[i] at i = 3.

        """
        nums.sort()
        self.res = []
        self.N = len(nums)
        def search(i, cur):
            if (i >= self.N):
                self.res.append(cur)
                return
            search(i+1, cur + [nums[i]])
            k = i
            while (k < self.N and nums[k] == nums[i]):
                k+=1
            search(k, cur)
        search(0, [])
        return self.res