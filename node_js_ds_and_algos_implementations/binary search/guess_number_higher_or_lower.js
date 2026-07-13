/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * function guess(num) {}
 */

class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    guessNumber(n) {
        // binary search, call guess() and see what it returns
        // is 0, that means return the guess, we've found the number
        // if 1, guess is too low, that means we search the right side to get a bigger number
        // if -1, guess is too high, that means we search the left side to get a smaller number
        let l = 1
        let r = n
        while (l <= r){
            // calculate mid first
            let mid = l + Math.floor((r-l)/2)
            // call guess(mid) to see whether the guess we made is smaller, greater or equal to target
            let res = guess(mid)
            if (res === 0){
                return mid
            }
            // search the left side because the guess is bigger than the target
            else if (res === -1){
                r = mid - 1
            }
            // search the right side because the guess is smaller than the target
            else {
                l = mid + 1
            }
        }
    }
}
