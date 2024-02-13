/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    /*
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    if reaching a buying point that's lower
    than our selling point, we should change the 
    buying point to be our selling point, since
    we'd be able to make a greater profit this way.
    i.e
    7,1,5,3,6,4
    if our buy point is at 7 and sell point is now 1,
    we should change the buy point to 1, so that at the next
    sell price of 5, you can make a profit this way
    
    Otherwise, we take the max between our current max
    and the selling point - buying point
    */
    let buy = prices[0]
    let max = 0
    for (let i = 1; i < prices.length; ++i){
        if (prices[i] < buy){
            buy = prices[i]
        }
        else {
            max = Math.max(max, prices[i] - buy)
        }
    }
    return max
};