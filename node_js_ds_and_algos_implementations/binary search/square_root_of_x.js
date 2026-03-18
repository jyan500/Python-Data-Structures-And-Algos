class Solution {
    /**
     * @param {number} x
     * @return {number}
     */
    mySqrt(x) {
        /*
        use binary search to figure out whether the current number squared
        is equal to the target

        lower bound = 1
        upper bound is the target itself 

        if we can't find a perfect square, binary search should bring us to the closest
        possible number, but because its rounded down, the answer is the smaller
        number, likely on the right boundary
        (after l exceeds r and the while loop ends)
        */

        let l = 0
        let r = x
        while (l <= r){
            let mid = l + Math.floor((r-l)/2)
            let square = mid * mid
            if (square === x){
                return mid
            }
            else if (square > x){
                r = mid - 1
            }
            else if (square < x){
                l = mid + 1
            }
        }
        return r
    }
}
