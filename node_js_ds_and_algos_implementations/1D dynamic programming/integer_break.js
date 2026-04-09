class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    /* 
    O(N^2) Time
    O(N) Space
    */
    integerBreak(n) {
        const dp = new Map();
        dp.set(1, 1);

        const dfs = (num) => {
            if (dp.has(num)) {
                return dp.get(num);
            }
            // in the recursion tree, this statement means
            // we need to always break the original number n,
            // so that's why the res is 0 so there will always be new value
            // for max here. But in cases where we are not required to split,
            // there could be a case where it's advantageous to NOT accept the new val
            // as max, which is why we set res = num instead of 0
            let res = num === n ? 0 : num;
            for (let i = 1; i < num; i++) {
                const val = dfs(i) * dfs(num - i);
                res = Math.max(res, val);
            }

            dp.set(num, res);
            return res;
        };

        return dfs(n);
    }
}