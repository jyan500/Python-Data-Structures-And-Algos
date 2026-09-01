class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    tribonacci(n) {
        /* 
        Instead of fibonacci where the current fibonacci number
        equals the sum of the two previous numbers,
        for tribonacci, it's the sum of the three previous numbers
        base case
        if i == 1 or i === 2, since there are only up to two previous numbers here,
        the sum is 1, since tribonacci of 1 is 1 (same as fibonacci), and tribonacci of 2
        is just 0 and 1
        if i === 0, for both fibonacci and tribonacci, it's always 0 since there's no numbers
        that come before it

        Use memoization similar to fibonacci
        */
        let memo = {}
        let search = (i) => {
            if (i <= 0){
                return 0
            }
            if (i === 1 || i === 2){
                return 1
            }
            if (i in memo){
                return memo[i]
            }
            memo[i] = search(i-1) + search(i-2) + search(i-3)
            return memo[i]
        }
        return search(n)
    }
}
