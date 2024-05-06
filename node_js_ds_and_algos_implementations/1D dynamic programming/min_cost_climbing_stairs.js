/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
    /*
    Time Complexity:
    With memoization, it's O(N),
    with the cost of O(N) space
    Approach:
    write inner function to calculate all possibilities starting from an index
        if i >= N, this is the base case. Since we're already at the 'top floor',
        we don't need to pay anything, so return 0
        
        the recurrence relation is that we want the minimum cost between climbing one
        stair, and climbing two stairs. Therefore, the total accumulated cost would be the cost
        to get to the stair we're currently at (cost[i]) + the min of possibilities we'd get from climbing one stair, or climbing two stairs.
        
    call inner function starting at index 0
    call inner function starting at index 1
    apply memoization to avoid repeated work when recalculating for index 1
    take the min between these 
    
    example:    
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    starting at i = 0
    cost[0] + Math.min(climbStairs(1), climbStairs(2))
    
    2nd recursive call
    cost[1] + Math.min(climbStairs(2), climbStairs(3))
    
    3rd recursive call
    cost[2] + Math.min(climbStairs(3), climbStairs(4))
    
    ...
    
    cost[8] + Math.min(climbStairs(9), climbStairs(10))
    
    cost[9] + Math.min(climbStairs(10), climbStairs(11))
    
    here, climbStairs(10) and climbStairs(11) both return 0 since the base case is reached
    
    memo[9] = cost[9] + 0 = 1
    
    backtracks to 
    
    memo[8] = cost[8] + Math.min(1, 0) = 100 + 1 = 101
    
    memo[7] = cost[7] + Math.min(101, 1) = 1 + 1 = 2
    
    memo[6] = cost[6] + Math.min(2, 101) = 1 + 2 = 3
    
    memo[5] = cost[5] + Math.min(3, 2) = 100 + 2 = 102
    
    memo[4] = cost[4] + Math.min(102, 3) = 1 + 3 = 4
    
    memo[3] = cost[3] + Math.min(4, 102) = 1 + 4 = 5
    
    memo[2] = cost[2] + Math.min(5, 4) = 1 + 4 = 5
    
    memo[1] = cost[1] + Math.min(5, 5) = 100 + 5 = 105
    
    memo[0] = cost[0] + Math.min(105, 5) = 1 + 5 = 6
    
    final memo = {0: 6, 1: 105, 2: 5, 3: 5, 4: 4, 5: 102, 6:3, 7:2, 8:101, 9:1}
    This is the end of calling the recursion starting from i = 0,
    you'd repeat the same process starting at i = 1, but this time, you can refer to the memo
    dict, which would give you the min cost of getting to the top starting from that index i
    */
    let N = cost.length
    let memo = {}
    var climbStairs = function(i){
        if (i >= N){
            return 0
        }
        else if (i in memo){
            return memo[i]
        }
        memo[i] = cost[i] + Math.min(climbStairs(i+1), climbStairs(i+2))
        return memo[i]
    }
    return Math.min(climbStairs(0), climbStairs(1))
};