class Solution {
    /**
     * @param {number} amount
     * @param {number[]} coins
     * @return {number}
     */
    change(amount, coins) {
        /*
        Revisited 7/27/2026 with a different, but less efficient solution
        O(amount * coins.length^2), because
        you are doing O(coins.length) amount of work in each recursive call due to the inner for loop

        DP
        distinct combinations
        in order to prevent previous elements from being chosen, we pass along
        the starting index k in the recursion, and then start the loop at k so we don't
        start back from index 0 again,
        (i.e we're picking index 1, but we want to prevent index 0 from being chosen
        in order to avoid a duplicate, since we would've already found that combination
        when starting at index 0,
        for example 1,2,3, amount = 4, we can choose 1,1,2, but when have 2 at the starting point,
        we want to prevent picking "1", such as 2,1,1)

        To memoize, you would need to account for the total and k (the last index picked),
        since there can be cases where you have the same total, as well as the last index picked,
        and would be doing redudant work without memoization. For example,
        if the amount is 8 and coins = [1,2,3]
        could you have 1,1,1,1,2
        and 2,2,2
        both sum to 6 and have their last index picked as index = 1
        anything else done after that point to reach the total 8 is the same on both paths,
        so it makes sense to memoize them.
        */
        let memo = {}
        const search = (total, k) => {
            if (total === 0){
                return 1
            }
            let key = `${total},${k}`
            if (key in memo){
                return memo[key] 
            }
            let res = 0
            for (let i = k; i < coins.length; ++i){
                if (total - coins[i] >= 0){
                    res += search(total - coins[i], i)
                }
            }
            memo[key] = res
            return res
        }
        return search(amount, 0)
    }
}

/**
 * @param {number} amount
 * @param {number[]} coins
 * @return {number}
 */
/* 
Approach:
2-D Dynamic Programming, where you track the index and the total amount remaining (initially
starts the same as the "amount" parameter but gets decremented until it reaches 0)
This is a knapsack relation, where the recurrence relation is that
A) You can keep choosing the same coin (keeping index the same), but decreasing the total
B) Skip this coin and move to the next index, which keeps the total the same

The number of ways is the sum of the recursive results of A and B

Base Case:
if we reached the end of the array, if the current is 0, return 1 as this is a valid combination,
else return 0 

For A), you can continue doing this as long as cur - current coin >= 0

Time Complexity: O(M*N), where M is the amount, and N is the size of coins array
Space Complexity: O(M*N)

The reason why it's O(M*N) time is because the recursion (With memoization) is simulating
a nested for loop, where you start from i = 0, and then keep picking the same index until
you can't, and then eventually, it will start over but at i = 1

Example:
amount = 5 coins = [1,2,5]

continually pick 1 until you cannot pick 1 anymore, (1 1 1 1 1)
this backtracks to
1 1 1 1, if skipping to 2, you cannot pick 2 or 5 either, so this backtracks to 
1 1 1, at this point you can pick 2 (but not 5) (1 1 1 1 1, 1 1 1 2)
this will backtrack to 
1 1, and you can try picking 2. Note that because we're at the index = 1 (value 2), we can't
go back and pick 1 (index 0) again, this prevents us from getting duplicates. Therefore, you won't
be able to make another combination like this

This eventually backtracks to 
1, where you can pick 2, and then pick another 2 for another unique combination (1 1 1 1 1, 1 1 1 2, 1 2 2)

backtracking to 1, this will now skip to 2 and attempt to get unique combinations starting from 2
without picking 1, but it's not possible

This then skips to 5, and picks 5, for the last unique combination (1 1 1 1 1, 1 1 1 2, 1 2 2, 5)

This returns 4

referenced solution from: https://leetcode.com/problems/coin-change-ii/discuss/1932377/Top-Down-Memo-technique

*/
var change = function(amount, coins) {
    let memo = {}
    let N = coins.length
    var search = function(i, cur){
        // if decreased the cur to zero, this is a valid combination
        if (i >= N){
            return cur === 0 ? 1 : 0
        }
        if (`${i},${cur}` in memo){
            return memo[`${i},${cur}`]
        }
        else {
            // we can continue to choose the same coin and subtract from the total OR
            // skip to the next coin (knapsack relation)
            let ways1 = 0
            if (cur - coins[i] >= 0){   
                ways1 = search(i, cur - coins[i])
            }
            let ways2 = search(i+1, cur)
            memo[`${i},${cur}`] = ways1 + ways2
            return ways1 + ways2
        }
    }
    return search(0, amount)
};