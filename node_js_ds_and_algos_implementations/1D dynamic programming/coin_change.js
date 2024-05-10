/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    /*
    we need the fewest amount of coins,
    so at each i, we want to get the minimal amount of coins needed to make the amount 0

    Time Complexity with Memoization:
    O(N)
    Space:
    O(N)
    
    for example
    [1], amount = 2

    1st call
    minWays = positive inf
    for (let i = 0 ...) {
        i = 0
        if (2 - 1 >= 0){
            minWays = Math.min(numWays(1), minWays)
        }
    }
    2nd call
    minWays = positive inf
    for (let i = 0 ...){
        i = 0
        if (1 - 1 >= 0){
            minWays = Math.min(numWays(0), minWays)
        }
    }
    3rd call
    base case reached
    amt === 0,
    returns 0

    back to 2nd call
    we now have a value of numWays(0), which is 0
    minWays = Math.min(0, positive inf) = 0

    minWays !== number.positive inf, so add 1

    returns 1

    back to 1st call
    numWays(1) returns 1
    minWays = Math.min(numWays(1), positive inf) = 1

    minWays !== positive inf, 
    add 1
    returns 2

    if you go to the 2nd iteration of the loop, 
    for (let i = 0 ... ){
     i = 1
     minWays(numWays(1), positive inf)...
     this is where memoization comes in handy, because we've already 
     calculated this once, and we know at this i, it should equal 1 way (since the amount would be 1, and there's only one coin)
    }
    */   
    let memo = {}
    var numWays = function(amt){
        if (amt === 0){
            return 0
        }
        // we're storing the minimum ways to make each amount within each key value in the memoization,
        // so we can recall it if we reach an amount that we've already calculated
        if (amt in memo){
            return memo[amt]
        }
        let minWays = Number.POSITIVE_INFINITY
        for (let i = 0; i < coins.length; ++i){
            // continue to subtract coins from the total amount as long as we don't reach below 0
            if (amt - coins[i] >= 0){
                minWays = Math.min(numWays(amt-coins[i]), minWays)
            }
        }
        /*
        the reasoning behind this statement is because if you were able to reach amt === 0, that means
        you found a valid configuration of coins, which means the call to numWays() would've returned 0.
        So Math.min(numWays(...), Number.POSITIVE_INFINITY) would be 0,
        and because this is a valid configuration of coins, we set minWays += 1 to indicate that one valid way of 
        picking the coins was found.
        */
        if (minWays !== Number.POSITIVE_INFINITY){
            ++minWays
        }
        memo[amt] = minWays
        return minWays
    }
    let amt = numWays(amount)
    return amt !== Number.POSITIVE_INFINITY ? amt : -1
};