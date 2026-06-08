class Solution {
    /**
     * @param {string} s
     * @param {number} minJump
     * @param {number} maxJump
     * @return {boolean}
     */
    canReach(s, minJump, maxJump) {
        /*
        you can jump in the range between minJump and maxJump
        and the index you land on must have a value of 0, if its 1,
        you can't jump any further

        for example,
        00110010 where minJump = 2 and maxJump = 4, allows you to jump from
        index 0 -> 4 -> 8
        (4 spaces) then (3 spaces)

        0010 minJump = 1, maxJump = 1, this isn't valid because
        once you get to index 2 (which has a value of 1), you can't go further
        
        Brute Force solution:
        using backtracking, at each i, loop between the ranges minJump and maxJump
        and then make a recursive call at i + <range>

        To optimize, you'll need to perform memoization since there will be any repeated subcases at each i

        */
        const N = s.length
        const memo = {}
        // if it reaches the very last spot, will return true
        memo[N-1] = true
        const search = (i) => {
            if (i in memo){
                return memo[i]
            }
            memo[i] = false
            // instead of starting from the min jump,
            // we can start from the max jump and work backwards, yielding a
            // slightly more optimized approach that doesn't change the time complexity
            // but does pass on neetcode (whereas the listed memoization solution gets call stack exceeded)
            for (let k = Math.min(N-1,i+maxJump); k >= i+minJump; --k){
                // prevent the recursion from entering any cases where s[k] !== 0 to save time
                if (s[k] === "0" && search(k)){
                    memo[i] = true
                    break
                }
            }
            return memo[i]
        }
        // sanity check: if the last position is a "1",
        // we always return false since this isn't a valid position to end on
        if (s[N-1] === "1"){
            return false
        }
        return search(0)
    }
}
