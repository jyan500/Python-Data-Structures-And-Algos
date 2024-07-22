/**
 * @param {string} s
 * @return {number}
 */
var maxScore = function(s) {
    /*
    https://leetcode.com/problems/maximum-score-after-splitting-a-string/
    Neetcode:
    https://www.youtube.com/watch?v=mc_eSStDrWw

    O(N) solution
    Similar idea, but instead of re-calculating the 
    entire counts for each left and right, use sliding window strategy
    where get the counts of the left and right initially splitting at i = 0, and then
    gradually update as we iterate from 1 ... s.length - 1,
    based on the element at i that will be included as part of the left 

    if i === "0", then we increment the left count (we're gaining a "0" on the left side)
    else if i === "1", then we decrement the right count (we're losing a "1" on the right side)
    
    i.e
    s = "011101"
    we get the initial window
    of "0" and "11101"
    where the left side count = 1
    right side count = 4
    total = 1 + 4 = 5
    
    from i = 1 ... s.length - 1
    we now examine i = 1, which is "1"
    this would mean we're looking at "01" and "1101"
    
    if we include i = 1 in the left window, our left window does not
    increase because it's not a zero, however our right window
    count decreases, since we're losing a "one" on the right side,
    
    therefore, the left count is now 1, and the right count is now 3 instead of 4
    
    we then take the Math.max(total, new left count + new right count),
    Math.max(5, 4), so still 5
    
    */
    let left = s.slice(0, 1)
    let right = s.slice(1, s.length)
    let countLeft = [...left].reduce((acc, obj) => {
        return obj === "0" ? acc + 1 : acc
    }, 0)
    let countRight = [...right].reduce((acc, obj) => {
        return obj === "1" ? acc + 1 : acc
    }, 0)
    let total = countLeft + countRight
    for (let i = 1; i < s.length - 1; ++i){
        if (s[i] === "1"){
            --countRight
        }
        else {
            ++countLeft
        }
        total = Math.max(total, countLeft+countRight)
    }
    return total
    /*
    Brute Force Solution
    Iterate through s and for each i until s.length - 1, calculate the 
    amount of zeroes on the left of i, and calculate the 
    amount of ones on the right of i, add them together and take the max so far
    
    O(N^2)
    */
    // let total = 0
    // // it's s.length - 1 because it cannot be split
    // // where the left side is the entire string and the right
    // // side is an empty string
    // for (let i = 0; i < s.length-1; ++i){
    //     let left = s.slice(0, i+1)
    //     let right = s.slice(i+1, s.length)
    //     let countLeft = [...left].reduce((acc, obj) => {
    //         if (obj === "0"){
    //             return acc + 1
    //         }
    //         return acc
    //     }, 0)   
    //     let countRight = [...right].reduce((acc, obj) => {
    //         if (obj === "1"){
    //             return acc + 1
    //         }
    //         return acc
    //     }, 0)
    //     total = Math.max(total, countLeft + countRight)
    // }
    // return total
};