class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        /*
        revisited 4/1/2026
        Binary search on range

        we're optimizing on K, therefore, our lower and upper bounds
        should be the K values, and then we use the K value to calculate
        how long it'd take to eat all the bananas

        if the time exceeds h, we need a bigger K
        if the time is smaller than h, we can see if we can decrease the value of K
        so we eat banas at a slower rate

        lower bound of K = 1 banana per hour
        upper bound of K = the max amount of bananas in the pile per hour
        */

        let l = 1
        let r = Math.max(...piles)

        const calculateTime = (k) => {
            let totalTime = 0
            for (let i = 0; i < piles.length; ++i){
                totalTime += Math.ceil(piles[i]/k)
            }
            return totalTime
        }

        let res = 0
        while (l <= r){
            let mid = l + Math.floor((r-l)/2)
            // calculate time taken
            let totalTime = calculateTime(mid)
            // if we're able to eat all the bananas <= the specified time,
            // store our result (since this is a potential answer)
            // see if we can optimize by searching the left side for a smaller K value
            if (totalTime <= h){
                res = mid
                r = mid - 1
            }
            // otherwise, if we weren't able to eat all bananas by specified time,
            // search the right side
            else {
                l = mid + 1
            }
        }
        return res
        
    }
}
