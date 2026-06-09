class Solution {
    /**
     * @param {number[]} weights
     * @param {number} days
     * @return {number}
     */
    shipWithinDays(weights, days) {
        /*
        what we're looking for here is that on any given day,
        we want to find the smallest possible weight capacity that allows us
        to ship all packages <= days limit

        for example
        weights = [2,4,6,1,3,10] days = 4
        the upper bound possible is just the sum of the list, meaning
        we guarantee everything is shipped under the possible days amount (in one day),
        but it's the max we can possibly have.
        the lower bound is just the max(weights), meaning that
        if we were to go under this number, it's likely we won't be able to ship
        everything out under the amount of days. This number isn't necessarily
        the answer either, as its possible we can't even ship everything out using this capacity,
        so the answer may need to be bigger 

        As a brute force solution,
        since we know our lower and upper bounds
        we can iterate from our lower to upper, and for each capacity that we choose,
        we write a separate function that determines how many days it takes 
        given the capacity we chose.

        For example:
        [1,5,4,4,2,3] days = 3
        if we chose 5

        days = 0
        window = 0
        for i ... weights

            // if we can still fit items in the window,
            // continue
            if weights[i] + window <= capacity
                window += weights[i]
            // we've reached our max for the window, so increase the days amount
            // and reset the window to the current weight instead
            else
                window = weights[i]
                days += 1
        // return whether we completed under the time limit
        return days < time limit

        Instead of brute forcing, we can apply binary search on the lower
        and upper bound. If we find that the capacity is not big enough,
        then you'd need to search the right side to find a bigger number, otherwise search the left
        side to see if we can get a smaller number. If it's a valid,
        we save the answer in a variable that will be overwritten if we hit isValid(mid) again
        during the binary search

        Time: O(NLogN) (LogN for the binary search, but O(N) for the day checking)
        Space: O(1)
        */

        const isValid = (capacity) => {
            let curDays = 0
            let window = 0
            for (let i = 0; i < weights.length; ++i){
                if (weights[i] + window <= capacity){
                    window += weights[i]
                }
                else {
                    window = weights[i]
                    curDays += 1
                }
            }
            return curDays < days
        }

        let l = Math.max(...weights)
        let r = weights.reduce((acc,num) => { return acc + num }, 0)

        let res = 0
        while (l <= r){
            let mid = l + Math.floor((r-l)/2)
            if (isValid(mid)){
                // since this is a possible capacity we could've chosen, save it
                // as a possible answer
                res = mid
                r = mid - 1
            }
            else {
                l = mid + 1
            }
        }
        return res
    }
}
