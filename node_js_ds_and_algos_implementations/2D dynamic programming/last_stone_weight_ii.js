class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeightII(stones) {
        /* 
        initial thought was to sort descending and greedily match closest pairs,
        however, this doesn't actually work because
        1 3 4 4 6

        if you mash 4 and 4, you're left with 1 3 6
        greedily matching the closest pairs would suggest mashing 1 and 3,
        but that leaves 2 6, which results in 4
        mashing 3 and 6 is actually more optimal since it results in 1 and 3,
        which results in 2

        Another strategy is to separate the stones into two different groups,
        take the sum of those two groups and get the absolute difference
        for example:
        1 3 4 4 6
        splits into
        1 3 4 and 4 6
        the sums would be 8 and 10, for a difference of 2
        now if we did 
        1 4 4 and 3 6 instead,
        this would yield 9 and 9, for a difference of 0

        To figure out the groups, use Top Down Recursion, with knapsack

        for example
        starting at i = 0
        we decide whether we want to include the value at i = 0 or not,
        if so, we add it to the running sum

        take = search(i+1, runningSum + stones[i])
        skip = search(i+1, runningSum)

        Now at the base case,
        the insight here is that we have a runningSum of stones we selected,
        any stone that we did NOT select automatically ends up in the "second" group,
        which also has its own sum, which is just the totalSum of all the stones - runningSum

        so if i === N, we would return the difference between the total sums of the two groups
        abs(runningSum - (totalSum - runningSum))

        Now going back to our take and skip cases, since both of these would return potential
        answers, we want the MIN between them

        return min(take, skip)

        This can be further optimized with memoization, since its possible that
        you run into multiple cases where at a given i, the runningSum is the same as before,
        so cache these values based on i, runningSum

        Another optimization that can be made is that since the goal is that we want to minimize the difference, it wouldn't make sense for the running sum to go past the total sum / 2, since
        that would mean you would likely not get the smallest distance between the two groups
        if it extended past this amount

        Time: O(N * runningSum)
        Space: O(N * runningSum)
        */

        let N = stones.length
        let totalSum = stones.reduce((acc,num) => acc + num, 0)
        let target = Math.ceil(totalSum / 2)
        let memo = {}
        const search = (i, runningSum) => {
            // calculate the difference between the sums of each group
            if (runningSum >= target || i === N){
                return Math.abs(runningSum - (totalSum - runningSum))
            } 
            let key = `${i},${runningSum}`
            if (key in memo){
                return memo[key]
            }
            // include the stone into this group
            let take = search(i+1, runningSum + stones[i])
            // don't include the stone in this group (which implies in its in the other group)
            let skip = search(i+1, runningSum)
            memo[key] = Math.min(take, skip)
            return memo[key]
        }

        return search(0, 0)
    }
}
