class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    nextPermutation(nums) {
        /* 
        http://youtube.com/watch?v=uCst0TJHJvg

        1) find the "pivot" where the elements no longer follow a strictly
        decreasing order 
        for example:
        1 2 3 4 5 - doesn't have a decreasing order, this is the min, starting case of permutations
        5 4 3 2 1 - it's already in a strictly decreasing order, this is the max possible permutation

        however if you have something like:
        1 3 5 4 3 2 2

        starting from the right, if you iterate and find index 1, you can see
        that every element after it is strictly decreasing, so index 1 is the pivot point here

        You would then swap the "next" greatest number that comes before it
        with this pivot point 

        1 3 5 4 3 2 1 
        becomes
        1 4 5 3 3 2 1 after index 1 swaps with index 3

        Then, reverse that strictly decreasing sequence

        1 4 5 3 3 2 1 becomes
        1 4 1 2 3 3 5,

        so this would be the "next" lexicographic sequence

        O(N) Time
        O(N) Space
        */

        let N = nums.length
        let pivot = -1
        // find pivot
        for (let i = N - 2; i >= 0; --i){
            if (nums[i] < nums[i+1]){
                pivot = i
                break
            }
        }

        // if there is no pivot, that means we are at the "max" lexicographic
        // order, so we just reverse the whole array and return it
        if (pivot === -1){
            nums.reverse()
            return
        }
        // swap pivot element with the next greatest element that's
        // greater than the pivot
        // coming from the right
        for (let i = N - 1; i >= 0; --i){
            if (nums[i] > nums[pivot]){
                [nums[i], nums[pivot]] = [nums[pivot], nums[i]]
                break
            }
        }

        // reverse the sequence from before the pivot
        let reversed = nums.slice(pivot+1, N)
        reversed.reverse()
        let j = 0;
        for (let k = pivot + 1; k < N; ++k){
            nums[k] = reversed[j]
            ++j
        }
    }
}
