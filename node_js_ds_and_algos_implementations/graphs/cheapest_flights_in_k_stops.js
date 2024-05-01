/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    /*
    Bellman Ford Algorithm
    https://www.youtube.com/watch?v=5eIK3zUdYmE
    O(E*K), k is the max amount of stops
    */  
    let prices = []
    for (let i = 0; i < n; ++i){
        prices.push(Number.POSITIVE_INFINITY)
    }
    prices[src] = 0
    
    for (let i = 0; i < k + 1; ++i){
        let tmp = [...prices]
        for (let [from, to, price] of flights){
            if (prices[from] === Number.POSITIVE_INFINITY){
                continue
            }
            if (prices[from] + price < tmp[to]){
                tmp[to] = prices[from] + price
            }
        }
        prices = tmp
    }
    return prices[dst] !== Number.POSITIVE_INFINITY ? prices[dst] : -1
};