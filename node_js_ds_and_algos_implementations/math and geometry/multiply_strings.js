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