/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    /*
    merge sort
    O(NLogN) Time
    O(N) space
    1) recursively split the array in half until it can no longer be split
    2) merge the two halves together into the sorted version and return
    */
    var merge = function(arr1, arr2){
        let i = 0
        let j = 0
        let res = []
        // only increment the pointer for a given list if
        // it's been pushed to the res array
        while (i < arr1.length && j < arr2.length){
            if (arr1[i] < arr2[j]){
                res.push(arr1[i])
                ++i
            }
            else if (arr2[j] < arr1[i]){
                res.push(arr2[j])
                ++j
            }
            else {
                res.push(arr1[i])
                res.push(arr2[j])
                ++i
                ++j
            }
        }
        // if one of the arrays is longer than the other, concatenate the remaining elements
        // to the list
        if (i < arr1.length){
            for (let k = i; k < arr1.length; ++k){
                res.push(arr1[k])
            }
        }
        else if (j < arr2.length){
            for (let k = j; k < arr2.length; ++k){
                res.push(arr2[k])
            }
        }
        return res
    }
    var split = function(nums){    
        let left = 0
        let right = nums.length-1
        // if the array can no longer be split, just return the array itself
        if (nums.length <= 1){
            return nums
        }
        let mid = Math.floor(nums.length/2)
        let leftHalf = nums.slice(0, mid)
        let rightHalf = nums.slice(mid, nums.length)
        let sortedLeft = split(leftHalf)
        let sortedRight = split(rightHalf)
        return merge(sortedLeft, sortedRight)
    }
    return split(nums)
    
};