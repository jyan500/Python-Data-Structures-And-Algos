class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {boolean}
     */
    search(nums, target) {
        /* 
        in search in rotated sorted array I, you would first find the pivot point
        where the elements on the left are sorted in ascending, and same with the right, then apply the search in both areas.
        However, because there are non-distinct elements, there's not really a sense
        of "pivot" point, so instead, we have to find determine based on the midpoint,
        if the left half of the array is sorted or the right half,
        and then try to find the target, or we move to a different midpoint
        where it follows this property.
        
        The edge case involving the duplicate check where nums[mid] === nums[left]
        means that you can't safely eliminate one half or the other, so you would
        just increment left by one. For example,

        nums = [3,1,1,1,1,2] target = 2
        l = 0
        r = 5
        mid = 2
        is nums[l] < nums[mid]? False
        that means the right half is sorted
        is target > nums[mid] && target <= nums[r]? 
        2 > 1 and 2 <= 2, TRUE
            search the right side
        
        l = mid + 1 which is 3
        r = 5
        mid = (5+3)/2=4

        note that because nums[mid] == nums[l] (1 === 1),
        we increment l by one since it's not possible to tell which half is sorted
        this way.
        l = 4
        r = 5
        mid = 4
        
        nums[mid] == nums[l] again, so we increment l again
        l = 5
        r = 5
        now mid is 5, which equals our target

        Because some aspect of the problem is linear due to the duplicate case,
        the worst case is we end up with an O(N) algorithm,
        but on average, it will be O(LogN)
        
        */

        let l = 0
        let r = nums.length - 1
        while (l <= r){
            let mid = l + Math.floor((r-l)/2)
            if (nums[mid] === target){
                return true
            }
            if (nums[mid] === nums[l]){
                // duplicates check
                ++l
            }
            // this means the left half is sorted
            else if (nums[l] < nums[mid]){
                // if the target is in this range, we search the left
                if (nums[l] <= target && target < nums[mid]){
                    r = mid - 1
                }
                else {
                    l = mid + 1
                }
            }
            // this means the right half is sorted
            else {
                // search the right if the target is in the range between
                // nums[mid] < target < nums[r]
                if (target > nums[mid] && target <= nums[r]){
                    l = mid + 1
                }
                // otherwise, search the left side
                else {
                    r = mid - 1
                }
            }
        }
        return false
    }
}
