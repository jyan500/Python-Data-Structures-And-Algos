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