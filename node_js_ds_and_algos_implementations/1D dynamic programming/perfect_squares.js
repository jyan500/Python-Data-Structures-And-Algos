class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    numSquares(n) {
        /*
      
        alternative BFS solution, treating this as a shortest paths problem.
        You start at 0, and then each step adds a perfect square. If you reach the target N,
        that means by default, you've explored the shortest way to get to n as a property of BFS.

        Also track a visited set to avoid going down recursive paths based on the total sum that we've already calculated


        time complexity: O(N * sqrt(N))
        space complexity: O(N)
        */
        const q = new Queue()
        const seen = new Set()

        let res = 0
        q.push(0)
        while (!q.isEmpty()){
            ++res
            for (let i = q.size(); i > 0; --i){
                const cur = q.pop()
                for (let s = 1; (s**2) + cur <= n; ++s){
                    let next = cur + (s**2)
                    if (next === n){
                        return res
                    }
                    if (!seen.has(next)){
                        q.push(next)
                        seen.add(next)
                    }
                }
            }
        }
        return res
    }
}
class Solution {

    numSquares(n) {
    /*

        Alternative Recursive Top Down Solution: 
        the baseline default answer is always just n itself,
        because n can consist of n amount of 1's
        i.e 3 = 1 + 1 + 1

        cannot pick a perfect square that's greater than n itself
        bounded by 1 ... biggest perfect square that's not greater than n

        using recursion, we can brute force all different combinations
        but to optimize this, we should use memoization, where at a given i,
        we already know what the "minimum" length sum is that equals n

        The problem with this solution is that it times out on neetcode,
        presumably because the recursive stack becomes too large 

        */
        let k = 1
        let squaredValue = 1
        while (k**2 <= n){
            squaredValue = k**2
            k++
        }
        // subtract one from k since we're one over
        k--
        let minLength = n
        let memo = new Map()
        const search = (curSum) => {
            // if the currentSum is already at n, that means
            // the length to reach the sum is 0
            if (curSum === n){
                return 0
            }
            if (curSum in memo){
                return memo[curSum]
            }
            let minLength = n
            for (let i = 1; i <= k; ++i){
                if ((i**2) + curSum <= n){
                    // we add one to the recursive result to show that
                    // this one additional number to add to the combination of numbers that sums
                    // up to n
                    let len = 1 + search(curSum + (i**2))
                    minLength = Math.min(len, minLength)
                }
            }
            memo[curSum] = minLength
            return minLength
        }
        return search(0, 0)
    }
}
