class Solution {
    /**
     * @param {number[]} piles
     * @return {boolean}
     */
    stoneGame(piles) {
        /*
        4/16/2026
        Was able to figure this one out after recalling similarities with stone game II

        Dynamic Programming + Reverse Thinking

        you have 2 choices
        take from the beginning of the pile
        or take from the end of the pile 
        will probably need two pointers as well
        so if i is chosen, advance the i pointer but keep j the same
        if j is chosen, decrease the j pointer by one but keep i the same

        the general recurrence relation:
        pile[i] + search(i+1, j)
        pile[j] + search(i, j-1)

        we also track another boolean that determines whether it's alice's turn or not,
        which is important because:

        At the end, we actually only care about alice's score, which is why
        when it's not alice's turn, we actively try and minimize her score 
        (so bob plays optimally that turn). If it's her turn, we maximize it.
        This way, we don't need to track both players' scores and simplifies the code.

        At the end, we would sum up the total for the entire pile and just subtract
        it from the answer get from the recursion to get the amount bob made.
        if the answer from the recursion > the amount bob made, that means alice won!

        To optimize this, we can use memoization and store the states (i,j, isAliceTurn)
        if we've already calculated it

        for example:
        piles = [1,2,3,1]
        if Alice takes from i = 0, bob takes from j = 3
        then Bob takes from i = 1, Alice takes j = 2
        This is the same as if :
        Alice took j = 3, Bob takes i = 2
        Alice takes j = 2 and Bob takes i = 1,
        we've already calculated 1,2,isAliceTurn to know that Alice wins in this combination,
        so we can just re-reference it
        */
        let i = 0
        let j = piles.length-1
        let memo = {}
        const search = (i,j, isAliceTurn) => {
            // if i has exceeded the midpoint, we return 0 because there's no points
            // that can be gained
            if (i > j){
                return 0
            }
            let key = `${i},${j},${isAliceTurn}`
            if (key in memo){
                return memo[key]
            }
            // take the value of the beginning and increment from the beginning pointer
            let takeBeginning = piles[i] + search(i+1, j, !isAliceTurn)
            // the value of the ending and decrement from the ending pointer
            let takeEnd = piles[j] + search(i, j-1, !isAliceTurn)
            // if it's alice turn, we'd want to maximize the result
            // if it's not, we'd want to minimize it.
            let res = 0
            if (isAliceTurn){
                res = Math.max(takeBeginning, takeEnd)
            }
            else {
                res = Math.min(takeBeginning, takeEnd)
            }
            memo[key] = res
            return res

        }
        let aliceScore = search(i,j,true)
        let totalPile = piles.reduce((acc,num) => acc+num, 0)
        return aliceScore > (totalPile - aliceScore)
    }
}
