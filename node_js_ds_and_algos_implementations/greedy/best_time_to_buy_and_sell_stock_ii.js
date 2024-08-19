/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
     
    /*  https://www.youtube.com/watch?v=3SJ3pUkPQMc&ab_channel=NeetCode
        Concept:
        1) As seen in the neetcode vid, we only turn a profit when 
        going from a lower to a higher price.
        2) Loop through the array and see if the previous price is higher, if so
        add the difference between the current and previous price to our total profit

        Key is that we want to maximize the amount of profitable transactions we have,
        rather than holding at the lowest and buying at the highest later, so whenever
        we see that the current price is greater than previous, we treat this as if we bought at the previous price
        and sold at the current price, for a profit of current price - previous price.

        For example:
        7 1 5 3 6 4 

        if you bought at 1 and sold at 6, you'd gain 5

        but if you bought at 1 and sold at 5, that gains 4
        and then bought at 3 and sold at 6, gains another 3,
        for a total of 7

        So it's better to maximize the amount of profitable transactions here, since you can buy/sell multiple
        times according to the problem statement.

    */
    let profit = 0
    for (let i = 1; i < prices.length; ++i){
        if (prices[i] > prices[i-1]){
            profit += (prices[i] - prices[i-1])
        }
    }
    return profit
};