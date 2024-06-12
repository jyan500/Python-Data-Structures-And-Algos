/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    /*
    https://leetcode.com/problems/gas-station/discuss/805989/brute-force-one-pass-step-by-step-explanationwith-proof-graph-and-code-beginners-friendly
    Greedy Solution
    Similar to Kadane's Algorithm:

    1) 1st check is realizing that if the total gas < total cost, there is no valid answer.
    The reason is because if total gas < total cost, you will eventually get to a point
    where you don't have enough gas to leave one of the stations.

    2) 2nd part is similar to Kadane's. Keep track of the total amount of gas that would remain
    after getting to a station and attempting to leave (total += gas[i] - cost[i])

        if total < 0, that means that we know that any starting point up to this point would not be valid,
        as it'd run out of gas trying to leave station i. Therefore, we can reset the total gas to 0,
        and then set i + 1 to be the new starting point, since we know i won't work.

    Example:
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]

    Time: O(N)
    Space: O(1)
    */
    let totalGas = gas.reduce((acc, x) => acc + x, 0)
    let totalCost = cost.reduce((acc, x) => acc + x, 0)
    if (totalGas < totalCost){
        return -1
    }
    totalGas = 0
    start = 0
    for (let i = 0; i < gas.length; ++i){
        // calculate the remaining gas after arriving at station i
        totalGas += (gas[i] - cost[i])
        // If the totalGas < 0, that means it's impossible to arrive at this station - it will be an unsuccessful route.
        if (totalGas < 0){
            start = i + 1
            totalGas = 0
        }
    }
    return start
};

var canCompleteCircuit = function(gas, cost) {
    /*
    This isn't a very intuitive solution, so it's better to stick with the greedy approach above
    Top Down Recursive Solution
    O(N^2) Time 
    O(N) Space
    https://leetcode.com/problems/gas-station/discuss/3014300/DP-%2B-Recursion

    Approach:
    1) initially, loop through all the stations and start our recursion starting at station i

    2) At station i, IF our current tank + gas[cur] >= cost[cur], this means we have enough gas
    to leave the station. Therefore, we want to try the next station i + 1

    The problem states that at each i, we must go in a clockwise direction, meaning that 
    if we're at i, we are limited to i+1,... length-1, and cannot go backwards (i.e i-1)
    Therefore, if we're at i=length-1, in order for the indices to "loop" back around, 
    we need to use the % operator. 
    
    So at each recursive call, we pass in (i+1) % length, and then for the gasAmt,
    we take the gasAmt + gas[cur] - cost[cur] to show the amount of gas we have left after leaving the station

    3) Base Case: 
    If we have enough gas to leave the current station, (gas[cur] + gasAmt >= cost[cur]), 
        If the next station is the starting point((cur+1)%gas.length === startingPoint), 
        this means we were able to complete the cycle. return true

    Memoization:
    This isn't very intuitive, but
    at each cur, we want to store the amount of gas left
    memo[cur] = gasAmt

    if we've already seen this station, AND the amount of gas 
    that we had at the first time we've been to this station exceeds the amount of gas we have now,
    that means that there's no point in continuing, as we're not going to have enough gas to continue
    anyway.

    This doesn't seem like something you could come up with in an interview setting since it 
    does not match how memoization is normally used for recursive/DP style problems, so the greedy approach
    is better.

    */
    let N = gas.length
    let memo = {}
    var search = function(startingPoint, cur, gasAmt){
        if (cur in memo && memo[cur] >= gasAmt){
            return false
        }
        memo[cur] = gasAmt
        if (gas[cur] + gasAmt >= cost[cur]){
            if ((cur + 1) % gas.length === startingPoint){
                return true
            }
            return search(startingPoint, (cur + 1) % gas.length, gasAmt + gas[cur] - cost[cur])
        }
        return false
    }
    for (let i = 0; i < gas.length; ++i){
        if (search(i, i, 0)){
            return i
        }
    }
    return -1

};