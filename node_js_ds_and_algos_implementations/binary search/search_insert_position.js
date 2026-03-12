class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    searchInsert(nums, target) {
        /*
        binary search because the input is already sorted
        and we need O(LogN) time.

        we keep a result that's initially nums.length. This gets around an edge
        case like so:
        nums=[-1,0,2,4,6,8]
        target=10

        where our expected result is 6 (which is out of bounds)

        in this example, if we were to attempt to find 10,
        we would get the first midpoint
        (5)//2 = index 2, which is value of 2
        we would then search again on the right 
        with l = mid + 1 = 3 and r = 5
        (3 + (5-3)//2) = 3 + 1 = 4
        nums[4] = 6 which is still less than target
     
        l = mid + 1 = 5

        now the mid is 5, and it's still less than target
        at this point, we'd get l = 6, which exceeds l >= r
        and breaks the loop

        so our initial result of 6 holds.
        */

        let res = nums.length
        let l = 0
        let r = nums.length - 1
        while (l <= r){
            const mid = l + Math.floor((r-l)/2)
            if (nums[mid] === target){
                return mid
            }
            if (nums[mid] > target){
                /* 
                the reason why we set our potential result to mid here is because
                if our midpoint is greater than our target, that means that we've gone
                "too far" to the right, and need to search the left. But this represents
                a potential result as our result will always be to the right of where
                our target should be, and continue searching left for a smaller valid index.
                */ 
                res = mid
                r = mid - 2
            }
            else {
                l = mid + 1
            }
        }
        return res
    }
}

