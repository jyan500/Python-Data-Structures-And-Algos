class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        /*
        Revisited 4/24/2026 with while loop solution

        Need to find the inflection point, since in un-rotated arrays,
        the right side is always greater, and the left side is always less
        than the current number
        however, in the rotated array, there's a certain point where
        in the inflection, the left side suddenly becomes greater, and the
        right side is also greater
        for example,
        [3,4,5,6,1,2], 1 would be the inflection point, since 
        3 is greater than 1, and 2 is greater than 1 as well

        use binary search to find the inflection point

        l = 0
        r = 5
        mid = 5//2 = 2
        nums[2]

        note that nums[5] < nums[2] (2 < 5), so search the right side
        l = 2 + 1 = 3

        l = 3
        r = 5

        mid = 3 + (5-3)//2 = 3 + 1 = 4
        nums[4] = 1
        note here that nums[5] is actually greater than nums[4], so we search left
        2 > 1

        r = 4
        l = 3
        mid = 3 + (4-3) = 4//2 = 2

        nums[r] < nums[mid], nums[4] < nums[2] = 1 < 5
        search right side again

        l = mid + 1 = 4
        now l is no longer less than r, so the while loop breaks

        so we return nums[l]
        */
        const findInflectionPoint = () => {
            let l = 0
            let r = nums.length - 1
            while (l < r){
                let mid = l + Math.floor((r-l)/2)
                // search right side, since in normal array, nums[r] should be greater than mid, and not less
                if (nums[r] < nums[mid]){
                    l = mid + 1
                }
                else {
                    // unlike most binary search problems, you need to include mid as the right boundary
                    // when searching the left side. This is because there are cases where mid might 
                    // be the minimum we're looking for
                    r = mid
                }
            }
            return nums[l]
        }
        let inflectionPoint = findInflectionPoint()
        return inflectionPoint
    }
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    /*
    in a normal sorted array:
    you'd expect the elements to be strictly increasing going to the right,
    and strictly decreasing going to the left
    in rotated sorted array however:
    for one element, the element to the right will have a decreased value
    , and the element on the left will have an increased value, this is where the "rotation" point was
    
    for example:
    4 5 6 7 0 1 2 3
    the rotation point is where the value of 0 was, since it goes
    from value of 7 to value of 0
    
    Therefore, to find the minimum value, we do a binary search where
    given mid, if right side is less than mid,  we should do a binary search on this side since in a normal sorted array, the right side should never be less than the mid
   if the right side is greater than mid though, that means the right side has the "proper" sorting order, so the reflection point must be on the left side
    
    */
    const helper = (l, r, nums) => {
        let mid = l + Math.floor((r-l)/2)
        if (l >= r){
            return nums[l]
        }
        else if (nums[mid] > nums[r]){
            return helper(mid+1, r, nums)
        }
        else{
            // unlike regular binary search,
            // make sure we include mid as a right most,
            // since there's an edge case where the mid
            // may already be our minimum, so we have to include it
            // in our search space.
            return helper(l, mid, nums)
        }
    }
    return helper(0, nums.length-1,nums)
};