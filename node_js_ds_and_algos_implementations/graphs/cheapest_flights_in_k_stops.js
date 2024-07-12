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

/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    // Modified Djikstra's Algorithm
    // By @PippyPattyPatterson, from youtube comment on Neetcode's Channel for
    // the solution to this problem: https://www.youtube.com/watch?v=5eIK3zUdYmE&ab_channel=NeetCode
    // the difference is that we need to account for the amount of stops taken, both in the min heap,
    // and also the visited dictionary (vertexToSteps)
    // Time Complexity: O(E*LogV)
    // Space: O(E+V)
    let adjacency = {}
    for (let i = 0; i < n; ++i){
        adjacency[i] = []
    }
    for (let [from, to, price] of flights){
        adjacency[from].push([to, price])
    }
    let heap = new MinPriorityQueue({priority: (element) => element[0]})
    // enqueue the weights (price), num steps taken, and current node (which is src initially)
    // the num steps starts at -1 since 
    // one stop (k) travels across two cities, so it's actually k + 1
    heap.enqueue([0, -1, src])
    // this acts as a "memoization", mapping
    // the current node to the amount of steps needed to reach it from src
    let vertexToSteps = {}
    while (!heap.isEmpty()){
        let [weight, steps, node] = heap.dequeue().element
        // if we've surpassed k or we've visited
        // this node AND we've surpassed k in this path, continue
        if (steps > k || (node in vertexToSteps && steps > vertexToSteps[node])){
            continue
        }
        vertexToSteps[node] = steps
        if (node === dst){
            return weight
        }
        // iterating through all neighbors
        for (let [dest, destWeight] of adjacency[node]){
            let element = [destWeight + weight, steps + 1, dest]
            heap.enqueue(element)
        }
    }
    // if dest cannot be reached in k stops, return -1
    return -1
};