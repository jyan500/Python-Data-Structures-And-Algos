/**
 * @param {number} n
 * @return {number}
 */
/* 
With memoization, this is an O(N) time solution

example:
memo = {}

n = 6
fib(6)

memo[6] = fib(4) + fib(5)

		two separate calls for fib(4) and fib(5)

memo[4] = fib(2) + fib(3)      memo[5] = fib(3) + fib(4)

here you can see fib(3) would normally get calculated twice, but the memoization would store the result
of fib(3). Also, memo[4] would store the results of fib(4), so you wouldn't need to recalculate its
result in fib(5)

*/
var climbStairs = function(n) {
    let memo = {}
    var fib = function(n){
        if (n === 1){
            return 1
        }
        else if (n === 2){
            return 2
        }
        else if (n in memo){
            return memo[n]
        }
        else {
            memo[n] = fib(n-2) + fib(n-1)
            return memo[n]
        }
    }
    return fib(n)
};