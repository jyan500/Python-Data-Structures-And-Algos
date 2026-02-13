/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
/*
Approach:
Simulates by-hand multiplication
1) Multiply the digits in reverse order, for each digit of the shorter number,
multiply by the digits of the longer number
    if there's carryover, the digit to save is res % 10 (which is the last digit),
    and the digit to carryover is res // 10

    The digit we store is always carryover + (digit of shorter number * digit of longer number)

2) Save each product of each "level" to array
    At each subsequent level, we add a placeholder "0" just like in by-hand multiplication
3) Add them together

Note for javascript, you need to use BigInt() to avoid truncation

1 2 3
  1 2

2 4 6
1 2 3 0 (zero is added)

added together is

1230 + 246 = 1476


*/
class Solution {
    /**
     * @param {string} num1
     * @param {string} num2
     * @return {string}
     */
    multiply(num1, num2) {
        /*

        Revisited 2/12/2026

        This solution performs the addTwoNumbers() function of adding the individual digits and returning
        a string of the sum to avoid the BigInt() issua from the previous solution below. Otherwise,
        the solutions are the same and both perform elementary school multiplication.

        Perform elementary multiplication here with each digit
        num1 = 12
        num2 = 13

        12
        13
        --
        36
       120
        ---
       156

        what if one of the digits is longer than the other?
        num1 = 12
        num2 =  3

        You should probably pad 0's at the beginning of the shorter number to simplify the logic
        num1 = 12
        num2 = 03

        so when calculating:
        12
        09
        --
       108
       000
       ---
       108 

        */

        function trimLeadingZeroes(num){
            let newNum = []
            let firstNonZeroFound = false
            for (let i = 0; i < num.length; ++i){
                if (!firstNonZeroFound && num[i] !== "0"){
                    firstNonZeroFound = true
                }
                if (firstNonZeroFound){
                    newNum.push(num[i])
                }
            }
            // if every number is zero, newNum would have length 0,
            // so make sure to return "0" in that case
            return newNum.length > 0 ? newNum.join("") : "0"
        }

        function addTwoNumbers(numA, numB){
            let longer = ""
            let shorter = ""
            let diff = 0
            if (numA.length < numB.length){
                diff = numB.length - numA.length
                longer = numB
                shorter = numA
            }
            else {
                diff = numA.length - numB.length
                longer = numA
                shorter = numB
            }
            for (let i = 0; i < diff; ++i){
                shorter = "0" + shorter
            }
            let carryover = 0
            let digits = []
            for (let i = longer.length-1; i >= 0; --i){
                let sum = carryover + parseInt(longer[i]) + parseInt(shorter[i])
                if (sum >= 10){
                    carryover = 1
                    sum = sum - 10
                }
                else {
                    carryover = 0
                }
                digits.unshift(sum.toString())
            }
            // if there's still carryover, add the carryover
            if (carryover > 0){
                digits.unshift(carryover.toString())
            }
            return digits.join("")
        }
        // pad shorter number with zeroes
        let longer = ""
        let shorter = ""
        let diff = 0
        if (num1.length < num2.length){
            diff = num2.length - num1.length
            longer = num2
            shorter = num1
        }
        else {
            diff = num1.length - num2.length
            longer = num1
            shorter = num2

        }
        for (let i = 0; i < diff; ++i){
            shorter = "0" + shorter
        }
        /* loop from back of the lower number first like when doing elementary school multiplication,
        since you take the bottom right digit and multiply by the top right digit, then
        move towards the left
        */
        let levels = []
        let k = 0
        for (let i = shorter.length-1; i >= 0; --i){
            let curRow = ""
            // each subsequent row has one zero padded to the end
            if (k > 0){
                curRow = "".padStart(k, "0")
            }
            let carryover = 0
            for (let j = longer.length-1; j >= 0; --j){
                let digit1 = parseInt(longer[j])
                let digit2 = parseInt(shorter[i])
                let product = (digit1 * digit2) + carryover
                if (product >= 10){
                    // the carryover is the first digit of the product
                    carryover = parseInt(product.toString()[0])
                    product = product.toString()[1]
                }
                else {
                    carryover = 0
                }
                curRow = product.toString() + curRow
            }
            if (carryover > 0){
                curRow = carryover.toString() + curRow
            }
            levels.push(curRow)
            ++k
        }
        // instead of manually converting each
        // number into an integer (which may cause the integer to exceed the MAX_SAFE_INTEGER,
        // in javascript, add the individual digits instead using a separate add function)
        let curSum = ""
        for (let i = 0; i < levels.length; ++i){
            curSum = addTwoNumbers(curSum, levels[i])
        }
        return trimLeadingZeroes(curSum)
    }
}

var multiply = function(num1, num2) {
    let longer = num1 
    let shorter = num2
    if (num2.length !== num1.length){
        longer = num1.length > num2.length ? num1 : num2
        shorter = num1.length < num2.length ? num1 : num2
    }
    let levels = []
    for (let i = shorter.length-1; i >= 0; --i){
        let carryover = 0
        let level = ""
        for (let k = 0; k < shorter.length-1-i; ++k){
            level += "0"
        }
        for (let j = longer.length-1; j >= 0; --j){
            let res = carryover + (Number(longer[j]) * Number(shorter[i]))
            if (res >= 10){
                carryover = Math.floor(res/10)
                level = ((res % 10).toString()) + level
            }
            else {
                level = (res.toString()) + level
                carryover = 0
            }
        }
        if (carryover > 0){
            level = carryover.toString() + level
        }
        levels.push(level)
 
    }
    let res = BigInt(0)
    for (let i = 0; i < levels.length; ++i){
        res += BigInt(levels[i])
    }
    return res.toString()
};