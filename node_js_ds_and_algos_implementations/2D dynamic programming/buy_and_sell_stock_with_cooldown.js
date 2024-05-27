/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    /*
    keep track of two params, current day i, and boolean
    on whether you can buy stocks or not
    each time you sell, add to profit
    each time you buy, subtract from profit
    
    if (canBuy)
        can buy, or cooldown
    else
        can only sell or cooldown
    
    when selling, you have to increment to i+2, since you won't be able to perform
    an action for one day after selling

    Time Complexity (With Memoization): O(N)
    Space Complexity: O(N) 
    */
    N = prices.length
    let memo = {}
    var search = function(i, canBuy){
        if (`${i},${canBuy}` in memo){
            return memo[`${i},${canBuy}`]
        }
        if (i >= N){
            return 0
        }
        if (canBuy){
            let buy = search(i+1, !canBuy) - prices[i]
            let cooldown = search(i+1, canBuy)
            let res = Math.max(buy, cooldown)
            memo[`${i},${canBuy}`] = res
            return res
        }
        else {
            let sell = search(i+2, !canBuy) + prices[i]
            let cooldown = search(i+1, canBuy)
            let res = Math.max(sell, cooldown)
            memo[`${i},${canBuy}`] = res
            return res
        }
    }
    return search(0, true)
};