class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        /*
        Using two pointers, because the array is already sorted in ascending order,
        and we know that the first index is always less than the second,
        we can start one pointer at the left, and one pointer at the right.
        We then check the sum of the values of the left and right. If its bigger than the target,
        we have to shift the right pointer inwards (r--) so the total sum becomes less, since
        the right side number should be smaller since it's sorted. Vice versa, if the sum
        is less than the target, we have to move the left side by one to increase the total sum 
        */
        let l = 0
        let r = numbers.length - 1
        while (l <= r){
            let sum = numbers[l] + numbers[r]
            if (sum === target){
                return [l+1,r+1]
            }
            else if (sum < target){
                ++l
            }
            else if (sum > target){
                --r
            }
        }
        
    }
}

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    /*
    O(N) Time O(1) Space
    Because the array is sorted,
    if we use two pointers, one in the back
    and one in the front, we can try adding the values together 
    and seeing if the sum > or < target, if so we can move one of the pointers
    back or forward to work towards finding our target.
    
    sum = numbers[left] + numbers[right,
    if sum === numbers[left]{
        we've found the pair
    }
    else if sum > numbers[left]{
        we need a smaller number, so we need to shift our
        right pointer - 1
    }
    else if sum < numbers[left]{
        we need a bigger number, so we need to shift our 
        left pointer + 1
    }
    */
    l = 0
    r = numbers.length-1
    while (l < r){
        sum = numbers[r] + numbers[l]
        if (sum === target){
            // return index + 1, as the problem states the indices are one indexed
            return [l+1, r+1]
        }
        else if (sum < target){
            ++l
        }
        else if (sum > target){
            --r
        }
    }
};