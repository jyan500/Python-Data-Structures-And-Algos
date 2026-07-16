class Solution {
    /**
     * @param {number[]} digits
     * @return {number[]}
     */
    plusOne(digits) {
        // revisited 7/16/2026
        let carryover = 0
        // if the last digit is 9, there will be carryover
        if (digits[digits.length-1] === 9){
            let i = digits.length-1
            // here, we assume that we add "plus one", so since we're starting from 
            // the last element, we can just assume a carryover of 1 to simulate that
            let carryover = 1
            while (i >= 0){
                let res = digits[i] + carryover
                if (res >= 10){
                    carryover = 1
                    digits[i] = res - 10
                    --i
                }
                else {
                    digits[i] = res
                    carryover = 0
                    break
                }
            }
            if (carryover === 1){
                digits.unshift(1)
            }
        }
        else {
            digits[digits.length-1] += 1
        }
        return digits
    }
}

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let i = digits.length-1
    // initially add one to the last digit
    let carryover = 0
    if (digits[i] + 1 >= 10){
        carryover = 1
        digits[i] = 0
    }
    else {
        carryover = 0
        digits[i] = digits[i] + 1
    }
    --i
    // if we're not at the front of the array, and there's carryover,
    // continuing adding the carryover until it's no longer 1
    // for example: 1, 9, 9
    // 2, 0, 0,
    // where the 1 is carried over after the initial addition of 1 to 9
    while (i >= 0 && carryover === 1){
        if (digits[i] + carryover >= 10){
            carryover = 1
            digits[i] = 0
        }
        else {        
            digits[i] = digits[i] + carryover
            carryover = 0
        }
        --i
    }
    // if there's still carryover, but we've run out of digits, we just add the carryover
    // to the beginning of the array
    // i.e [9], we'd add 1 to get 10, but there's a carryover of 1 and we're at the front of the array,
    // so this would be [1, 0]
    if (carryover === 1){
        digits.unshift(carryover)
    }
    return digits
};