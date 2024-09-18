/**
 * @param {number[]} nums
 * @return {number[]}
 */
/*
2 pointer solution
O(N) Time O(1) Space
[3, 4, 1, 2]
even pointer starts 0
if an even number is seen, swap the positions of num[i] and num[evnPointer]
increment even pointer to show where the next even number should go

i = 0, evnPointer = 0
nums[0] is 3, odd so we don't do anything here

i = 1, evnPointer = 0
nums[1] is 4, even so we swap nums[evnPointer] with nums[i]
increment evnPointer to 1
[4, 3, 1, 2]

i = 2, evnPointer = 1
nums[2] is 1, odd so we don't do anything here

i = 3, evnPointer = 1
nums[3] is 2, even so we swap nums[evnPointer] with nums[i]
increment evnPointer by 1
[4, 2, 1, 3]

this is a valid answer because all the even numbers come before
the odd numbers

*/
var sortArrayByParity = function(nums) {
    let evnPointer = 0
    for (let i = 0; i < nums.length; ++i){
        if (nums[i] % 2 === 0){
            let temp = nums[i]
            let temp2 = nums[evnPointer]
            nums[i] = temp2
            nums[evnPointer] = temp
            ++evnPointer
        }
    }
    return nums
};