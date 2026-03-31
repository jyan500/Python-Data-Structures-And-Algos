class Solution {
    /**
     * @param {number[]} piles
     * @return {number}
     */
    stoneGameII(piles) {
        /* 
            3/31/2026
            
            M represents the max amount of iles that can be taken on the players' turn
            so initially M = 1,

            whereas X represents the amount of piles that were taken.
            
            For example:
            1 <= X <= 2M

            if Alice goes first, she can take either 1 pile or 2 piles

            if she takes two, that also means the opponent, Bob can take up to 2

            the question is always: 
            do you take a lot now (which also increases M for your opponent), 
            or take less to keep M small and limit what they can grab?

            This naturally leads to dynamic programming in order to check whether
            taking 1, 2, up to ... 2M. 

            Another aspect of the problem is that we have to track whether its Alice's turn
            or Bob's. 
            
            On Alice's turn, we want to maximize the result. However on Bob's turn,
            (since Bob also wants to play optimally), you'd instead return
            the minimum result instead. As long as we know that Alice is getting the minimum she could get on Bob's turn,
            that means Bob played optimally (reverse thinking), 
            so we don't actually need to track or return Bob's score
            in the code

            Finally to optimize, we'd track the current index, current M value, and whether it's Bob or Alice's turn
            as a key for a memo dict, and the max value for Alice as value.
        */
        let memo = {}
        const dfs = (i, M, isAliceTurn) => {
            // if it's bob's turn, we're trying to minimize Alice's score,
            // so we need to initialize as POSITIVE_INFINITY
            let res = !isAliceTurn ? Number.POSITIVE_INFINITY : 0
            let total = 0
            // base case, if we're already past the pile length, there's no 
            // value to return, so return 0
            if (i >= piles.length){
                return 0
            }
            let key = `${i},${M},${isAliceTurn}`
            if (key in memo){
                return memo[key]
            }
            // same conditional as in the problem statement, we can pick from 1 <= x <= 2*M
            for (let x = 1; x <= (2*M); ++x){
                // make sure that we don't extend further than the pile length
                if (x+i-1 === piles.length){
                    break
                }
                // because x starts at 1, you need to subtract 1 to get the actual index
                // that's represented within the piles array
                total += piles[x+i-1]
                // alice's turn
                if (isAliceTurn){
                    // we set the max(x, N) so on Bob's turn can pick up to the same amount as Alice did
                    // and then we would see whether the total we have is greater than the max
                    // outcome we could get from the different combinations
                    res = Math.max(res, total + dfs(x+i, Math.max(x, M), !isAliceTurn))
                }
                else {
                    res = Math.min(res, dfs(x+i, Math.max(x, M), !isAliceTurn))
                }
            }
            memo[key] = res
            return res
        }

        // M always starts at 1, and Alice always moves first
        return dfs(0, 1, true)

    }
}
